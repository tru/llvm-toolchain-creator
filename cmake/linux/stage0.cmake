set(CMAKE_BUILD_TYPE "Release" CACHE STRING "")
set(LLVM_ENABLE_PROJECTS "clang;lld" CACHE STRING "")
set(LLVM_TARGETS_TO_BUILD "Native" CACHE STRING "")
set(LLVM_DISTRIBUTION_COMPONENTS "clang;clang-resource-headers;lld;runtimes;builtins;llvm-strip;llvm-objcopy;llvm-as;llvm-nm;llvm-strings;llvm-ar;llvm-profdata;llvm-ranlib;llvm-readelf;llvm-windres;llvm-rc" CACHE STRING "")

set(CLANG_DEFAULT_CXX_STDLIB "libc++" CACHE STRING "")
set(CLANG_DEFAULT_OBJCOPY "llvm-objcopy" CACHE STRING "")
set(CLANG_DEFAULT_RTLIB "compiler-rt" CACHE STRING "")
set(CLANG_DEFAULT_LINKER "lld" CACHE STRING "")

set(LLVM_BUILD_TESTS OFF CACHE BOOL "")
set(LLVM_ENABLE_ASSERTIONS OFF CACHE BOOL "")
set(LLVM_STATIC_LINK_CXX_STDLIB ON CACHE BOOL "")

set(_TARGETS "x86_64-unknown-linux-gnu")
list(GET _TARGETS 0 _DEF_TARGET)
set(LLVM_ENABLE_RUNTIMES "compiler-rt;libcxx;libcxxabi;libunwind" CACHE STRING "")
set(LLVM_RUNTIME_TARGETS "${_TARGETS}" CACHE STRING "")
set(LLVM_BULITIN_TARGETS "${_TARGETS}" CACHE STRING "")
set(LLVM_DEFAULT_TARGET "${_DEF_TARGET}" CACHE STRING "")