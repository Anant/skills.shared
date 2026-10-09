#!/usr/bin/env python3
"""Validate the skills in this repository and package them for distribution.

Usage:
  python3 scripts/build_skills.py check
  python3 scripts/build_skills.py build [--out dist]

`build` writes, for every skill, `skills/<name>.zip` and an identical
`skills/<name>.skill` (a zip whose single top-level folder is the skill), and
for every marketplace plugin, `plugins/<plugin>.zip` containing a portable
`plugin.json`, a `.claude-plugin/plugin.json`, and `skills/<name>/...`.
Standard library only.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
REPOSITORY_URL = "https://github.com/Anant/skills.shared"
HOMEPAGE_URL = "https://anant.co/labs"
LICENSE_ID = "MIT"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED_WORDS = ("anthropic", "claude")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
REFERENCE_RE = re.compile(
    r"`((?:references|scripts|templates|rubrics|examples|assets|agents)/[A-Za-z0-9_./-]+)`"
)
PROVIDER_RE = re.compile(r"\bClaude\b")
ALWAYS_EXCLUDE = ("__pycache__/", "*.py[cod]", ".DS_Store", ".gitignore")
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the flat `key: value` YAML frontmatter used by SKILL.md files."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening '---' frontmatter delimiter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise ValueError("missing closing '---' frontmatter delimiter") from None

    data: dict[str, str] = {}
    body = lines[1:end]
    i = 0
    while i < len(body):
        line = body[i]
        i += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0].isspace():
            raise ValueError(f"unexpected indented line: {line!r}")
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"expected 'key: value', got {line!r}")
        key, value = key.strip(), value.strip()
        if not value and i < len(body) and body[i][:1].isspace():
            nested = []
            while i < len(body) and (not body[i].strip() or body[i][0].isspace()):
                nested.append(body[i])
                i += 1
            value = "\n".join(nested)
        elif value[:1] in (">", "|"):
            block = []
            while i < len(body) and (not body[i].strip() or body[i][0].isspace()):
                block.append(body[i].strip())
                i += 1
            joiner = " " if value[0] == ">" else "\n"
            value = joiner.join(part for part in block if part).strip()
        elif value[:1] in ('"', "'"):
            quote = value[0]
            if len(value) < 2 or value[-1] != quote:
                raise ValueError(f"unterminated quoted value for {key!r}")
            value = value[1:-1]
            value = value.replace("''", "'") if quote == "'" else value.replace('\\"', '"')
        data[key] = value
    return data


def load_ignore_patterns(skill_dir: Path) -> list[str]:
    patterns = list(ALWAYS_EXCLUDE)
    gitignore = skill_dir / ".gitignore"
    if gitignore.is_file():
        for raw in gitignore.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
    return patterns


def is_ignored(rel: str, patterns: list[str]) -> bool:
    parts = rel.split("/")
    for pattern in patterns:
        if pattern.endswith("/"):
            if any(fnmatch.fnmatch(part, pattern[:-1]) for part in parts[:-1]):
                return True
        elif "/" in pattern.strip("/"):
            if fnmatch.fnmatch(rel, pattern.lstrip("/")):
                return True
        elif fnmatch.fnmatch(parts[-1], pattern):
            return True
    return False


def skill_files(skill_dir: Path) -> list[Path]:
    patterns = load_ignore_patterns(skill_dir)
    files = []
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file() and not is_ignored(path.relative_to(skill_dir).as_posix(), patterns):
            files.append(path)
    return files


def load_marketplace(report: Report) -> dict:
    try:
        return json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report.error(f"{MARKETPLACE.relative_to(ROOT)}: {exc}")
        return {}


def validate_skill(skill_dir: Path, report: Report) -> dict[str, str] | None:
    rel = skill_dir.relative_to(ROOT).as_posix()
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        report.error(f"{rel}: missing SKILL.md")
        return None
    text = skill_md.read_text(encoding="utf-8")
    try:
        meta = parse_frontmatter(text)
    except ValueError as exc:
        report.error(f"{rel}/SKILL.md: {exc}")
        return None

    name = meta.get("name", "")
    description = meta.get("description", "")
    if name != skill_dir.name:
        report.error(f"{rel}: frontmatter name {name!r} does not match directory {skill_dir.name!r}")
    if not NAME_RE.match(name) or len(name) > MAX_NAME:
        report.error(f"{rel}: name must be lowercase letters, digits and single hyphens, at most {MAX_NAME} characters")
    if any(word in name for word in RESERVED_WORDS):
        report.error(f"{rel}: name must not contain {', '.join(RESERVED_WORDS)}")
    if not description:
        report.error(f"{rel}: description is required")
    elif len(description) > MAX_DESCRIPTION:
        report.error(f"{rel}: description is {len(description)} characters (max {MAX_DESCRIPTION})")
    if "<" in description or ">" in description:
        report.error(f"{rel}: description must not contain angle brackets")

    for ref in sorted(set(REFERENCE_RE.findall(text))):
        if not (skill_dir / ref.rstrip("/")).exists():
            report.error(f"{rel}/SKILL.md: referenced file {ref} does not exist")

    packaged = {p.relative_to(skill_dir).as_posix() for p in skill_files(skill_dir)}
    for ref in sorted(set(REFERENCE_RE.findall(text))):
        if (skill_dir / ref).is_file() and ref not in packaged:
            report.error(f"{rel}/SKILL.md: referenced file {ref} is excluded by .gitignore")

    for lineno, line in enumerate(text.splitlines(), 1):
        if PROVIDER_RE.search(line):
            report.warn(f"{rel}/SKILL.md:{lineno}: provider-specific wording ('Claude')")
    return meta


def validate(report: Report) -> tuple[dict, dict[str, dict[str, str]]]:
    skills: dict[str, dict[str, str]] = {}
    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        meta = validate_skill(skill_dir, report)
        if meta is not None:
            skills[skill_dir.name] = meta

    marketplace = load_marketplace(report)
    if not marketplace:
        return marketplace, skills
    for key in ("name", "owner", "plugins"):
        if key not in marketplace:
            report.error(f"marketplace.json: missing {key!r}")
    if not re.match(r"^\d+\.\d+\.\d+$", str(marketplace.get("metadata", {}).get("version", ""))):
        report.error("marketplace.json: metadata.version must be MAJOR.MINOR.PATCH")

    assigned: dict[str, str] = {}
    plugin_names = set()
    for plugin in marketplace.get("plugins", []):
        pname = plugin.get("name", "")
        if not NAME_RE.match(pname):
            report.error(f"marketplace.json: invalid plugin name {pname!r}")
        if pname in plugin_names:
            report.error(f"marketplace.json: duplicate plugin name {pname!r}")
        plugin_names.add(pname)
        if not plugin.get("description"):
            report.error(f"marketplace.json: plugin {pname!r} needs a description")
        for path in plugin.get("skills", []):
            skill_name = Path(path).name
            if not (ROOT / path / "SKILL.md").is_file():
                report.error(f"marketplace.json: plugin {pname!r} lists {path}, which has no SKILL.md")
            elif skill_name in assigned:
                report.error(f"marketplace.json: {skill_name} is in both {assigned[skill_name]!r} and {pname!r}")
            else:
                assigned[skill_name] = pname
    for skill_name in skills:
        if skill_name not in assigned:
            report.error(f"marketplace.json: skills/{skill_name} is not listed in any plugin")
    return marketplace, skills


def write_zip(dest: Path, entries: list[tuple[str, bytes, int]]) -> None:
    """Write a reproducible zip: sorted entries, fixed timestamps."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for arcname, data, mode in sorted(entries):
            info = zipfile.ZipInfo(arcname, ZIP_EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100000 | mode) << 16
            zf.writestr(info, data)


def file_entries(skill_dir: Path, prefix: str) -> list[tuple[str, bytes, int]]:
    entries = []
    for path in skill_files(skill_dir):
        mode = 0o755 if os.access(path, os.X_OK) else 0o644
        arcname = f"{prefix}/{path.relative_to(skill_dir).as_posix()}"
        entries.append((arcname, path.read_bytes(), mode))
    return entries


def plugin_manifests(plugin: dict, marketplace: dict, version: str) -> dict[str, bytes]:
    owner = marketplace.get("owner", {})
    author = {"name": owner.get("name", ""), "url": HOMEPAGE_URL}
    common = {
        "name": plugin["name"],
        "version": version,
        "description": plugin["description"],
        "author": author,
        "homepage": HOMEPAGE_URL,
        "repository": REPOSITORY_URL,
        "license": LICENSE_ID,
    }
    portable = {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", **common}
    claude = dict(common)

    def dump(obj: dict) -> bytes:
        return (json.dumps(obj, indent=2) + "\n").encode("utf-8")

    return {"plugin.json": dump(portable), ".claude-plugin/plugin.json": dump(claude)}


def build(out: Path, marketplace: dict, skills: dict[str, dict[str, str]]) -> list[Path]:
    version = marketplace["metadata"]["version"]
    if out.exists():
        shutil.rmtree(out)
    built: list[Path] = []
    license_entry = [("LICENSE", (ROOT / "LICENSE").read_bytes(), 0o644)] if (ROOT / "LICENSE").is_file() else []

    for name in skills:
        entries = file_entries(SKILLS_DIR / name, name)
        zip_path = out / "skills" / f"{name}.zip"
        write_zip(zip_path, entries)
        skill_path = zip_path.with_suffix(".skill")
        shutil.copyfile(zip_path, skill_path)
        built += [zip_path, skill_path]

    for plugin in marketplace["plugins"]:
        entries = list(license_entry)
        for arcname, data in plugin_manifests(plugin, marketplace, version).items():
            entries.append((arcname, data, 0o644))
        for path in plugin["skills"]:
            skill_name = Path(path).name
            entries += file_entries(SKILLS_DIR / skill_name, f"skills/{skill_name}")
        plugin_path = out / "plugins" / f"{plugin['name']}.zip"
        write_zip(plugin_path, entries)
        built.append(plugin_path)

    sums = out / "SHA256SUMS"
    sums.write_text(
        "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(out).as_posix()}\n" for p in built),
        encoding="utf-8",
    )
    return built + [sums]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="validate skills and marketplace.json")
    build_cmd = sub.add_parser("build", help="validate, then write packages")
    build_cmd.add_argument("--out", type=Path, default=ROOT / "dist")
    build_cmd.add_argument("--expect-version", help="fail unless metadata.version equals this (e.g. from a git tag)")
    args = parser.parse_args(argv)

    report = Report()
    marketplace, skills = validate(report)
    if args.command == "build" and args.expect_version and not report.errors:
        expected = args.expect_version.removeprefix("v")
        actual = marketplace["metadata"]["version"]
        if expected != actual:
            report.error(f"marketplace.json: metadata.version {actual} does not match {expected}")

    for msg in report.warnings:
        print(f"warning: {msg}", file=sys.stderr)
    for msg in report.errors:
        print(f"error: {msg}", file=sys.stderr)
    if report.errors:
        return 1
    print(f"ok: {len(skills)} skills, {len(marketplace['plugins'])} plugins")

    if args.command == "build":
        for path in build(args.out, marketplace, skills):
            print(path.relative_to(args.out.parent) if args.out.is_absolute() else path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
