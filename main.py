"""Hand in the v8 newspaper front page for 26 November 2026.

The finished page ships beside this file at output/entry.png. This
program only moves those bytes into the grader's output directory: it
checks the picture is a genuine PNG of the right size, copies it, and
then proves the copy is identical by comparing SHA-256 digests.

Nothing but the standard library is used, so it runs in a bare
container with nothing installed.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "output" / "entry.png"
MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(65536)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    if SOURCE.stat().st_size > MAX_BYTES:
        print("source image is larger than 1 MiB", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as handle:
        magic = handle.read(8)
    if magic != PNG_MAGIC:
        print("source image is not a PNG file", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as handle:
        header = handle.read(33)
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if (width, height) != (1024, 1024):
        print(f"expected a 1024x1024 image, got {width}x{height}",
              file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)

    before = sha256_of(SOURCE)
    after = sha256_of(target)
    if before != after:
        print("copy failed the digest check", file=sys.stderr)
        return 1
    size = target.stat().st_size
    if size != SOURCE.stat().st_size:
        print("copy size does not match the source", file=sys.stderr)
        return 1
    print(f"entry.png: {size} bytes copied to {target} "
          f"(sha256 {after[:12]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
