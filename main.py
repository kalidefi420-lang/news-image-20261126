"""Copy the pre-built 26 November 2026 news image to the output directory.

The finished infographic ships with this entry at output/entry.png, next to
this file. This program only copies those bytes to the location the grader
reads. It uses nothing but the standard library, so it runs in a bare
container with nothing installed. Before copying it checks the file is a
real PNG within the size limit, and after copying it verifies the copy is
byte-identical to the source.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

MAX_BYTES = 1048576


def read_png_size(data: bytes) -> tuple:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("source is not a PNG file")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    source = Path(__file__).resolve().parent / "output" / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1
    data = source.read_bytes()
    if len(data) > MAX_BYTES:
        print(f"source image is {len(data)} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    width, height = read_png_size(data)
    if width > 1024 or height > 1024:
        print(f"source image is {width}x{height}, over the 1024x1024 limit",
              file=sys.stderr)
        return 1
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    if hashlib.sha256(destination.read_bytes()).hexdigest() != \
            hashlib.sha256(data).hexdigest():
        print("copy failed the byte-identity check", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({len(data)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
