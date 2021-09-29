from typing import List, Tuple

import h5py
import numpy as np

from simpleaccess.provider import base


class hdf5_handler(base.handler):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename

    def to_file(self, vectors: np.ndarray, keys: List) -> None:
        with h5py.File(self.filename, "w") as f:
            dt = h5py.special_dtype(vlen=str)
            f.create_dataset(
                "keys",
                data=np.array(keys, dtype=dt),
                dtype=dt,
            )
            f.create_dataset("vectors", data=vectors)

    def from_file(self) -> Tuple[np.ndarray, List]:
        with h5py.File(self.filename, "r") as f:
            keys = f["keys"][:]
            decoder = np.vectorize(lambda keys: keys.decode("UTF-8"))
            keys_str = decoder(keys).tolist()
            vectors = f["vectors"][:]

        return vectors, keys_str


def create_hdf5_handler(filename: str) -> hdf5_handler:
    return hdf5_handler(filename)
