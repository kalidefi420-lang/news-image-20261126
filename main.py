"""Copy the pre-built 26 November 2026 news image to the output directory.

The entry ships the finished image at output/entry.png. This program only
copies it to the output location the grader reads, using the standard
library so it runs in a bare container with nothing installed. Before
copying, it checks the file is a real PNG within the size limit and, after
copying, verifies the copy is byte-identical to the source.
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
    source_dir = Path(os.environ.get("MAKEFUN_BOT_DIR", "/bot"))
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    source = source_dir / "output" / "entry.png"
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
