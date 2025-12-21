import os

# /e:/code/mathlab/plugin/filesystem.py

def create_empty_dir(path):
    """
    创建一个空的文件夹：
    - 如果目标路径不存在，则创建该目录及必要的父目录。
    - 如果目标路径存在且是文件，抛出 FileExistsError。
    - 如果目标路径存在且是目录，删除该目录下的所有内容（但保留该目录本身）。
    """
    path = os.path.abspath(path)

    if os.path.exists(path):
        if os.path.isfile(path) or os.path.islink(path) and not os.path.isdir(path):
            raise FileExistsError(f"存在同名文件或符号链接: {path}")
        # 删除目录下的所有内容
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    else:
        os.makedirs(path, exist_ok=True)
