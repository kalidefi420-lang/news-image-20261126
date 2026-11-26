"""Hand in the newspaper front page for 26 November 2026.

Reads the finished picture (output/entry.png, next to this file) and
places an identical copy in the grader's output directory, after
checking the picture is a genuine PNG and small enough to hand in.
"""

import hashlib
import os
import shutil
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def fail(message):
    print(f"entry: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "output", "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        fail(f"missing source image: {source}")

    size = os.path.getsize(source)
    if size == 0:
        fail("source image is empty")
    if size > MAX_BYTES:
        fail(f"source image is {size} bytes, over the 1 MiB limit")

    with open(source, "rb") as handle:
        head = handle.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        fail("source image is not a PNG file")

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, target)

    def digest(path):
        hasher = hashlib.sha256()
        with open(path, "rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    if digest(source) != digest(target):
        fail("copied image differs from the source")

    print(f"entry.png: {size} bytes copied to {target}")


if __name__ == "__main__":
    main()
