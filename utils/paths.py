from pathlib import Path
from typing import List
import os
from doit import get_var
import platform
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
    def build(self) -> Path:
        return self.release / "build"

    @property
    def all(self) -> List[Path]:
        return [self.release, self.downloads, self.sources, self.build]

    @property
    def host_cache(self) -> Path:
        return self.root / "cmake" / platform.system().lower()


Paths = AllPaths()


def create_paths() -> None:
    for path in Paths.all:
        os.makedirs(str(path), exist_ok=True)


def all_paths() -> List[str]:
    return [str(path) for path in Paths.all]
