from pathlib import Path
from typing import Dict, Any, Union, List
import shutil
from os import makedirs
from utils.paths import Paths
from utils.tools import clean_rmtree


def unpack(
    file_to_uncompress: str,
    destination: str,
    strip_component: int = 0,
    target_file: Union[str, List[str]] = "",
) -> Dict[Any, Any]:
    def make_dir():
        if dest.is_dir():
            shutil.rmtree(dest)
        makedirs(dest)

    fpath = Paths.downloads / file_to_uncompress
    dest = Paths.sources / destination
    cmd = f"tar --strip-component={strip_component} -xaf {str(fpath)} -C {dest}"

    targets = [dest]
    if isinstance(target_file, str):
        targets.append(dest / target_file)
    elif isinstance(target_file, list):
        targets += [dest / t for t in target_file]

    return {
        "actions": [make_dir, cmd],
        "targets": targets,
        "file_dep": [fpath],
        "clean": [(clean_rmtree, [dest])],
    }
