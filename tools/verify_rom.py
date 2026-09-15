#!/usr/bin/env python3
"""Verify a local Pokémon Ruby ROM against committed target metadata.

Retail ROM images stay outside the repository. This tool only reads a user-supplied
local file, checks its GBA header, computes SHA-1, and compares the result with
manifests/versions.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifests" / "versions.json"


def sha1_file(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def decode_ascii(raw: bytes) -> str:
    return raw.rstrip(b"\0").decode("ascii", errors="replace")


def read_gba_header(path: Path) -> dict[str, object]:
    with path.open("rb") as handle:
        header = handle.read(0xC0)
    if len(header) < 0xC0:
        raise ValueError("file is too small to contain a complete GBA header")
    return {
        "title": decode_ascii(header[0xA0:0xAC]),
        "game_code": decode_ascii(header[0xAC:0xB0]),
        "revision": header[0xBC],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a local ROM against a decompilation target")
    parser.add_argument("rom", type=Path, help="path to a local .gba image")
    parser.add_argument("--target", help="target id from manifests/versions.json")
    args = parser.parse_args()

    if not args.rom.is_file():
        parser.error(f"ROM not found: {args.rom}")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    target_id = args.target or manifest["active_target"]
    try:
        target = manifest["targets"][target_id]
    except KeyError:
        parser.error(f"unknown target: {target_id}")

    actual_size = args.rom.stat().st_size
    actual_header = read_gba_header(args.rom)
    actual_sha1 = sha1_file(args.rom)

    expected_size = target["rom_size"]
    expected_header = target["header"]
    expected_sha1 = target["hashes"]["sha1"]

    checks = {
        "size": actual_size == expected_size,
        "title": actual_header["title"] == expected_header["title"],
        "game_code": actual_header["game_code"] == expected_header["game_code"],
        "revision": actual_header["revision"] == expected_header["revision"],
        "sha1": actual_sha1 == expected_sha1,
    }

    print(f"Target:    {target_id}")
    print(f"ROM:       {args.rom}")
    print(f"Size:      {actual_size} bytes")
    print(f"Title:     {actual_header['title']}")
    print(f"Game code: {actual_header['game_code']}")
    print(f"Revision:  {actual_header['revision']}")
    print(f"SHA-1:     {actual_sha1}")
    print()

    for name, passed in checks.items():
        print(f"[{'OK' if passed else 'FAIL'}] {name}")

    if all(checks.values()):
        print("\nMATCH: local ROM matches the selected decompilation target.")
        return 0

    print("\nMISMATCH: local ROM does not match the selected target.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
