from utils.paths import Paths
from utils.tools import clean_rmtree


def task_llvm_stage0_cmake():
    src_dir = Paths.sources / "llvm" / "llvm"
    bld_dir = Paths.build / "llvm_stage0"
    cache_file = Paths.host_cache / "stage0.cmake"

    return {
        "actions": [
            (clean_rmtree, (bld_dir,)),
            f"cmake -GNinja -C {cache_file} -S {src_dir} -B {bld_dir}",
        ],
        "file_dep": [src_dir / "CMakeLists.txt", cache_file],
        "targets": [bld_dir / "CMakeCache.txt"],
        "clean": [(clean_rmtree, (bld_dir,))],
    }


def task_llvm_stage0_build():
    bld_dir = Paths.build / "llvm_stage0"
    return {
        "actions": [f"cmake --build {bld_dir} --target distribution"],
        "file_dep": [bld_dir / "CMakeCache.txt"],
        "targets": [bld_dir / "bin" / "clang"],
        "clean": [(clean_rmtree, [bld_dir])],
    }
