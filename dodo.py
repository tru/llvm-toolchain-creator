from actions import *
from utils.paths import create_paths, all_paths
from doit.tools import run_once


def task_create_dirs():
    return {
        "actions": [create_paths],
        "targets": all_paths(),
        "uptodate": [run_once],
        "clean": True,
    }
