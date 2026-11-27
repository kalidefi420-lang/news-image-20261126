"""Hand in the newspaper front page for Thursday 26 November 2026.

The finished page ships with this entry at output/entry.png, next to this
file. This program only copies those bytes to the place the grader reads.
It uses nothing but the standard library, so it runs in a bare container
with nothing installed. Before copying it checks the file is a real PNG
of the right size, and after copying it verifies the copy is identical
by comparing SHA-256 digests.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

MAX_BYTES = 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _check_png(path):
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or head[:8] != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(
            f"entry.png is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )


def main():
    source = Path(__file__).resolve().parent / "output" / "entry.png"
    if not source.is_file():
        raise SystemExit("output/entry.png is missing")
    if source.stat().st_size > MAX_BYTES:
        raise SystemExit("entry.png is over the 1 MiB limit")
    _check_png(source)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    before = _sha256(source)
    after = _sha256(target)
    if before != after:
        raise SystemExit("copy failed verification: digests differ")
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("copy failed verification: sizes differ")
    print(f"entry.png: {target.stat().st_size} bytes copied to {target} "
          f"(sha256 {before[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
