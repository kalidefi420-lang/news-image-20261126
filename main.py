"""Hand in the newspaper front page for Thursday 26 November 2026.

The finished page is shipped with this entry as output/entry.png, next to
this file. This program places an identical copy of that picture in the
grader's output directory. It uses only the standard library, so it runs
in a bare container with nothing installed.

Before copying, it checks the picture is a genuine PNG and small enough
to hand in. After copying, it hashes both files and refuses to finish
unless the copy matches the original byte for byte.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "output" / "entry.png"
MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def digest(path):
    """SHA-256 of a file, read in 64 KiB chunks."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            block = fh.read(65536)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    if not SOURCE.is_file():
        print(f"missing: {SOURCE}", file=sys.stderr)
        return 1
    size = SOURCE.stat().st_size
    if size == 0 or size > MAX_BYTES:
        print(f"entry.png is {size} bytes, outside the 1..{MAX_BYTES} range", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        print("entry.png does not start with the PNG signature", file=sys.stderr)
        return 1

    shutil.copyfile(SOURCE, target)
    src_hash = digest(SOURCE)
    dst_hash = digest(target)
    if src_hash != dst_hash:
        print("copy failed verification: hashes differ", file=sys.stderr)
        return 1
    if target.stat().st_size != size:
        print("copy failed verification: sizes differ", file=sys.stderr)
        return 1
    print(f"entry.png: {size} bytes copied to {target} (sha256 {src_hash[:12]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
