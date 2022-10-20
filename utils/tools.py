import shutil
from pathlib import Path


def clean_rmtree(dir: Path) -> None:
    shutil.rmtree(dir, ignore_errors=True)
