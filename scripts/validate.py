from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
EXPECTED_CASES = 5
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def markdown_files() -> list[Path]:
    return [ROOT / "README.md", *sorted(CASES.glob("*.md"))]


def main() -> None:
    files = markdown_files()
    case_count = len(files) - 1
    if case_count != EXPECTED_CASES:
        raise SystemExit(f"expected {EXPECTED_CASES} case studies, found {case_count}")

    failures: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            failures.append(f"empty file: {path.relative_to(ROOT)}")
        for raw_link in LINK_RE.findall(text):
            link = raw_link.split()[0].strip("<>")
            parsed = urlparse(link)
            if parsed.scheme in {"http", "https", "mailto"} or link.startswith("#"):
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if ROOT not in target.parents and target != ROOT:
                failures.append(f"link escapes repository: {path.name} -> {link}")
            elif not target.exists():
                failures.append(f"broken local link: {path.name} -> {link}")

    if failures:
        raise SystemExit("\n".join(failures))
    print(f"validated {len(files)} markdown files and {case_count} case studies")


if __name__ == "__main__":
    main()
