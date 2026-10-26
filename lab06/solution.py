import os

def count_by_extension(paths: list[str]) -> dict[str, int]:
    extensions = {}
    for path in paths:
        filename = os.path.basename(path)
        if "." in filename:
            ext = filename.split(".")[-1].lower()
        else:
            ext = ""
        extensions[ext] = extensions.get(ext, 0) + 1
    return extensions

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))