from halo import Halo
from munch import munchify
from os.path import join
from pathlib import Path
from yaml import safe_load

def obtain_config(args, calling_script_file_path):
    script_parent_path = Path(calling_script_file_path).parent.absolute()
    config_path = join(script_parent_path, "config.yaml")
    with open(config_path, "r") as file_handle:
        yaml_dict = safe_load(file_handle)
    config = munchify(yaml_dict)
    config._script_parent_path = script_parent_path
    return config