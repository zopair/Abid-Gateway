#!/usr/bin/env python3
"""Validate the static NexaPay prototype without requiring a package manager."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.language = ""
        self.direction = ""
        self.has_main = False
        self.has_viewport = False
        self.title_depth = 0
        self.title = ""
        self.local_references: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        if tag == "html":
            self.language = values.get("lang", "")
            self.direction = values.get("dir", "")
        elif tag == "main":
            self.has_main = True
        elif tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = bool(values.get("content"))
        elif tag == "title":
            self.title_depth += 1
        for key in ("src", "href"):
            value = values.get(key, "").strip()
            if not value or value.startswith(("#", "data:", "mailto:", "tel:")):
                continue
            parsed = urlparse(value)
            if not parsed.scheme and not parsed.netloc:
                self.local_references.append(value.split("?", 1)[0].split("#", 1)[0])

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title += data


def validate_site(root: Path) -> dict:
    errors: list[str] = []
    index = root / "index.html"
    if not index.is_file():
        return {"valid": False, "errors": ["index.html is missing"]}

    parser = SiteParser()
    try:
        parser.feed(index.read_text(encoding="utf-8"))
        parser.close()
    except Exception as exc:
        errors.append(f"HTML parsing failed: {type(exc).__name__}")

    if parser.language != "ar":
        errors.append("The document must declare lang='ar'.")
    if parser.direction != "rtl":
        errors.append("The document must declare dir='rtl'.")
    if not parser.has_main:
        errors.append("The document must contain a main landmark.")
    if not parser.has_viewport:
        errors.append("A viewport meta tag is required for mobile layout.")
    if not parser.title.strip():
        errors.append("The document title is missing.")

    for reference in parser.local_references:
        if reference and not (root / reference).is_file():
            errors.append(f"Local asset does not exist: {reference}")

    readme = root / "README.md"
    if not readme.is_file():
        errors.append("README.md is missing.")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        if "تصور" not in readme_text or "افتراضية" not in readme_text:
            errors.append("README must disclose that this is a proposal with simulated data.")

    return {
        "valid": not errors,
        "errors": errors,
        "language": parser.language,
        "direction": parser.direction,
        "has_main": parser.has_main,
        "title": parser.title.strip(),
        "checked_local_references": len(parser.local_references),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = validate_site(args.root.resolve())
    if result["valid"]:
        print(
            "Static site validation passed: "
            f"lang={result['language']}, dir={result['direction']}, "
            f"local references={result['checked_local_references']}."
        )
        return 0
    for error in result["errors"]:
        print(f"ERROR: {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
