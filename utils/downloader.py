from pathlib import Path
from utils.paths import Paths
from doit.tools import run_once


def download_with_curl(url: str, output: str):
    odir = Paths.downloads / output

    args = ["curl.exe", "-q", "-L", "-o", str(odir), url]

    return {
        "actions": [" ".join(args)],
        "targets": [odir],
        "uptodate": [run_once],
        "setup": ["create_dirs"],
        "clean": True,
    }
