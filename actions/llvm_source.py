from utils.downloader import download_with_curl
from utils.globals import llvm_version
from utils.unpack import unpack
from utils.paths import Paths


def task_llvm_src_download():
    version = llvm_version()
    return download_with_curl(
        f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz",
        f"llvm-project-{version}.tar.xz",
    )


def task_llvm_src_unpack():
    version = llvm_version()

    return unpack(
        f"llvm-project-{version}.tar.xz",
        "llvm",
        strip_component=1,
        target_file=["README.md", "llvm/CMakeLists.txt"],
    )
