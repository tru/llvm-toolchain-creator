from utils.downloader import download_with_curl
from utils.unpack import unpack
from utils.paths import Paths
from utils.tools import clean_rmtree


def task_zlib_download():
    return download_with_curl(
        "https://github.com/madler/zlib/releases/download/v1.2.13/zlib-1.2.13.tar.xz",
        "zlib.tar.xz",
    )


def task_zlib_unpack():
    return unpack(
        "zlib.tar.xz", "zlib", strip_component=1, target_file="CMakeLists.txt"
    )


def task_zlib_cmake():
    cache_file = Paths.host_cache / "zlib.cmake"
    src_dir = Paths.sources / "zlib"
    bld_dir = Paths.build / "zlib"

    return {
        "actions": [
            (clean_rmtree, [bld_dir]),
            f"cmake -C {cache_file} -S {src_dir} -B {bld_dir}",
        ],
        "file_dep": [src_dir / "CMakeLists.txt", cache_file],
        "targets": [bld_dir / "CMakeCache.txt"],
        "clean": [(clean_rmtree, [bld_dir])],
    }


def task_zlib_build():
    bld_dir = Paths.build / "zlib"

    return {
        "actions": [f"cmake --build {bld_dir}"],
        "file_dep": [bld_dir / "CMakeCache.txt"],
        "targets": [bld_dir / "libz.a"],
        "clean": [(clean_rmtree, [bld_dir])],
    }
