import os
import warnings


def create_dir(dir_name):
    if dir_name == "":
        warnings.warn("The dir name is empty")
        pass

    path = os.path.join(".", dir_name)
    os.makedirs(path, exist_ok=True)
    return path
