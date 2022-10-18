from pathlib import Path
from typing import List
import os
from doit import get_var
from .globals import llvm_version


class AllPaths:
    @property
    def root(self) -> Path:
        return Path(__file__).resolve().parent.parent

    @property
    def release(self) -> Path:
        version = llvm_version()
        return self.root / f"llvm-{version}"

    @property
    def downloads(self) -> Path:
        return self.release / "download"

    @property
    def sources(self) -> Path:
        return self.release / "sources"

    @property
    def all(self) -> List[Path]:
        return [self.release, self.downloads, self.sources]


Paths = AllPaths()


def create_paths() -> None:
    for path in Paths.all:
        os.makedirs(str(path), exist_ok=True)


def all_paths() -> List[Path]:
    return [str(path) for path in Paths.all]
