#!/usr/bin/env python3
"""Copy the pre-built 26 November 2026 news image to /output/entry.png.

Standard library only. The grading container installs nothing, so this
program must not import anything beyond the standard library. The image
itself is drawn locally before submission and committed in
output/entry.png; this program only copies those exact bytes to the
output directory, after checking the file is a whole PNG within the
size limits (at most 1 MiB, at most 1024 by 1024 pixels).
"""
import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "output" / "entry.png"
DEST = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width and height from the PNG IHDR chunk (bytes 16-24)."""
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    data = SOURCE.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("source image is not a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"source image is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    width, height = png_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"source image is {width}x{height}, over the 1024x1024 limit", file=sys.stderr)
        return 1
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    if hashlib.sha256(DEST.read_bytes()).hexdigest() != hashlib.sha256(data).hexdigest():
        print("copy failed: hash mismatch", file=sys.stderr)
        return 1
    print(f"wrote {DEST} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
