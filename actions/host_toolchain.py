from utils.paths import Paths
import platform
from typing import Dict, Any
from subprocess import run


def linux_clang_toolchain() -> Dict[Any, Any]:
    return {
        "CMAKE_C_COMPILER": "clang",
        "CMAKE_CXX_COMPILER": "clang++",
        "CMAKE_AR": "llvm-ar",
    }


def linux_toolchain() -> Dict[Any, Any]:
    # We want clang over gcc
    res = run(["clang", "-dumpversion"], capture_output=True)
    if res.returncode == 0:
        print(res.stdout)

    return {
        "actions": ["clang --version > {targets}"],
        "file_dep": [],
        "targets": [Paths.build / "host-toolchain.cmake"],
    }


def d_task_gen_host_toolchain():
    # First we need to detect the host toolchain
    if platform.system() == "Linux":
        return linux_toolchain()
