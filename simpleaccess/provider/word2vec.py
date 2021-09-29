from typing import List, Tuple

import numpy as np
from gensim.models import KeyedVectors

from simpleaccess.provider import base


class word2vec_handler(base.handler):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename

    def to_file(self, vectors: np.ndarray, keys: List) -> None:
        raise NotImplementedError

    def from_file(self) -> Tuple[np.ndarray, List]:
        w2vec = KeyedVectors.load_word2vec_format(self.filename, binary=True)

        return w2vec.vectors, list(w2vec.index_to_key)


def create_word2vec_handler(filename: str) -> word2vec_handler:
    return word2vec_handler(filename)
