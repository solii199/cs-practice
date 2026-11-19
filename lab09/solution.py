import numpy as np

def make_hours() -> list[int]:
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype=float)
    return {
        "third": float(arr.item(2)),
        "last": float(arr.item(-1)),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }

def change_vector(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    arr[2:5] = 99
    arr[::2] = -1
    return arr.tolist()

