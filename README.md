# Thursday 26 November 2026 — world news in one image

A newspaper front page summing up Thursday 26 November 2026 in 27 stories:
Trump's new tariffs on 14 partners and the market plunge; Russia's overnight
strikes on Ukraine's energy sites; two tankers hit by mines in the Strait of
Hormuz; a second Hamas security chief killed in Gaza; the EU summit opening
in Brussels; Thanksgiving Day in the US; and the first Pakistani astronaut
aboard China's Tiangong station.

## How it works

`output/entry.png` is the finished 1024×1024 PNG (171,236 bytes), drawn
locally with Pillow. `main.py` is standard-library-only: it checks the PNG
magic bytes and the 1 MiB size limit, then copies the image byte-for-byte
to `/output/entry.png`. The grading container installs nothing, so the
entrypoint must not import Pillow or any other third-party package.

Run it twice to confirm determinism:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — stdlib-only copy program (the entrypoint)
- `output/entry.png` — the finished image
- `NEWS.md` — the 27 stories with sources
- `NEWS-RESEARCH.md` — the research behind the image (48 stories)
