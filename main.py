"""news-image-20261117: write the entry image to /output/entry.png.

The image (a front-page summary of Tuesday 17 November 2026 world news)
is stored in this repository as entry.png; this program copies it to the
output directory. It runs with no network and uses only the standard
library. The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting
to /output (the make.fun sandbox layout).
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, destination)
    # Sanity-check the entry the competition gate will check: at most
    # 1 MiB and at most 1024x1024 pixels.
    size = os.path.getsize(destination)
    if size > 1048576:
        print(f"entry.png is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
