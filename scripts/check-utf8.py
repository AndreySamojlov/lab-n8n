#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(__file__).resolve().parents[1]
CHECK_EXTENSIONS = {
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yml",
    ".yaml",
    ".py",
    ".ps1",
    ".sh",
}
SKIP_DIR_NAMES = {
    ".git",
    ".obsidian",
    "__pycache__",
}
DEFAULT_TARGETS = (
    REPO_ROOT,
    WORKSPACE_ROOT / "AGENTS.md",
    WORKSPACE_ROOT / "CLAUDE.md",
    WORKSPACE_ROOT / "docs" / "Codex-generated",
)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIR_NAMES for part in path.parts)


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(WORKSPACE_ROOT))
    except ValueError:
        return str(path)


def iter_files(target: Path) -> list[Path]:
    if not target.exists():
        return []
    if target.is_file():
        return [target] if target.suffix.lower() in CHECK_EXTENSIONS else []
    return [
        path
        for path in sorted(target.rglob("*"))
        if path.is_file()
        and path.suffix.lower() in CHECK_EXTENSIONS
        and not should_skip(path)
    ]


def resolve_targets(argv: list[str]) -> list[Path]:
    if not argv:
        return [path for path in DEFAULT_TARGETS if path.exists()]

    resolved: list[Path] = []
    for raw in argv:
        candidate = Path(raw)
        if not candidate.is_absolute():
            candidate = (WORKSPACE_ROOT / candidate).resolve()
        if candidate.exists():
            resolved.append(candidate)
        else:
            print(f"Warning: target does not exist: {raw}", file=sys.stderr)
    return resolved


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    targets = resolve_targets(argv)
    if not targets:
        print("No valid targets to check.", file=sys.stderr)
        return 1

    bad_files: list[str] = []
    checked_files = 0
    seen: set[Path] = set()

    for target in targets:
        for path in iter_files(target):
            if path in seen:
                continue
            seen.add(path)
            checked_files += 1

            raw = path.read_bytes()
            shown = display_path(path)

            if raw.startswith(b"\xef\xbb\xbf"):
                bad_files.append(f"{shown}: UTF-8 BOM is forbidden")
                continue

            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError as exc:
                bad_files.append(f"{shown}: invalid UTF-8 at byte {exc.start}")
                continue

            if "\r\n" in text or "\r" in text:
                bad_files.append(f"{shown}: CRLF is forbidden, use LF")

    if bad_files:
        print("Encoding check failed:", file=sys.stderr)
        for item in bad_files:
            print(f"- {item}", file=sys.stderr)
        return 1

    print(f"Encoding check passed. Checked {checked_files} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
