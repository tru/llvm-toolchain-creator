from utils.downloader import download_with_curl
from utils.globals import llvm_version


def task_llvm_download():
    version = llvm_version()
    return download_with_curl(
        f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz",
        f"llvm-project-{version}.tar.xz",
    )


def task_llvm_unpack():
    version = llvm_version()
