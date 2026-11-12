# coolest-art-01 entry: a colossal bioluminescent whale breaching over a neon city at dusk.
# The program copies the art beside it, byte for byte, to /output/entry.png.
# Pure copy: no network, no randomness, no clock, so both runs write identical bytes.

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SRC = os.path.join(HERE, "art.jpg")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

# Fail loudly rather than ship a truncated copy: the gate rejects a partial image.
if os.path.getsize(SRC) != os.path.getsize(DST):
    raise SystemExit("entry.png size does not match art.jpg")
