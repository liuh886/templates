#!/usr/bin/env python3
"""Create a new app by merging common files with one starter.

This script intentionally does not make product decisions, install packages,
create compatibility layers, or mutate existing projects.
"""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STARTERS = {"minimal", "interactive", "content-data"}
TEXT_SUFFIXES = {
    ".md", ".html", ".css", ".js", ".mjs", ".json", ".ts", ".tsx", ".astro", ".yml", ".yaml", ".txt"
}


def copy_tree(source: Path, destination: Path) -> None:
    for path in source.rglob("*"):
        relative = path.relative_to(source)
        target = destination / relative
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)


def replace_tokens(destination: Path, app_name: str, app_title: str) -> None:
    replacements = {
        "{{APP_NAME}}": app_name,
        "{{APP_TITLE}}": app_title,
        "{{YEAR}}": str(datetime.now().year),
    }
    for path in destination.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for token, value in replacements.items():
            text = text.replace(token, value)
        path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new Hao app starter")
    parser.add_argument("--type", required=True, choices=sorted(STARTERS), dest="starter_type")
    parser.add_argument("--name", required=True, help="Repository/package name, e.g. rhythm-lab")
    parser.add_argument("--title", required=True, help="Human product name")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    output = args.output.expanduser().resolve()
    if output.exists():
        if not output.is_dir():
            raise SystemExit(f"Refusing to overwrite non-directory path: {output}")
        if any(output.iterdir()):
            raise SystemExit(f"Refusing to modify non-empty directory: {output}")

    output.mkdir(parents=True, exist_ok=True)
    copy_tree(ROOT / "common", output)
    copy_tree(ROOT / "starters" / args.starter_type, output)
    replace_tokens(output, args.name, args.title)

    print(f"Created {args.title} from '{args.starter_type}' in {output}")
    print("Next: complete PRODUCT.md, replace the neutral vertical slice, then verify the quality baseline.")


if __name__ == "__main__":
    main()
