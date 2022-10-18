from doit import get_var

DEFAULT_LLVM_VERSION = "15.0.3"


def llvm_version():
    return get_var("llvm-version", DEFAULT_LLVM_VERSION)
