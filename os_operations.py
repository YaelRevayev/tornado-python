import os


def create_dir(dir_name):
    try:
        path = os.path.join(".", dir_name)
        os.makedirs(path, exist_ok=True)
        return path
    except NameError:
        print(NameError)


