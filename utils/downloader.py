from pathlib import Path
from utils.paths import Paths
from doit.tools import run_once
import platform


def download_with_curl(url: str, output: str):
    odir = Paths.downloads / output

    curl = "curl"
    if platform.system == "Windows":
        curl += ".exe"
    args = f"{curl} -s -f -L -o {odir} {url}"

    return {
        "actions": [args],
        "targets": [odir],
        "uptodate": [run_once],
        "setup": ["create_dirs"],
        "clean": True,
    }
