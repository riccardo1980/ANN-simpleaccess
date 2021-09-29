from abc import ABC, abstractmethod
from typing import List, Tuple

import numpy as np


class handler(ABC):
    @abstractmethod
    def to_file(self, vectors: np.ndarray, keys: List) -> None:
        """
        Write to file

        :param vectors:
            np.ndarray of embeddings

        :param keys:
            list of UTF-8 encoded strings
        """

    @abstractmethod
    def from_file(self) -> Tuple[np.ndarray, List]:
        """
        Read from file

        :return: vectors, keys
            vectors: np.ndarray of embeddings
            keys: list of UTF-8 encoded strings
        """
