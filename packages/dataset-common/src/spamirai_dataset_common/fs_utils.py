import os
from pathlib import Path


def mkdirp(path: Path):
    os.makedirs(path, exist_ok=True)
