import os
from typing import Callable, Dict

from simpleaccess.provider.base import handler
from simpleaccess.provider.hdf5 import create_hdf5_handler
from simpleaccess.provider.word2vec import create_word2vec_handler


class factory_handler:
    handler_builder: Dict[str, Callable[[str], handler]] = dict()

    def __init__(self) -> None:
        pass

    @staticmethod
    def register(ext: str, builder: Callable[[str], handler]) -> None:
        if ext in factory_handler.handler_builder:
            print("builder already exists, overwriting")
        factory_handler.handler_builder[ext] = builder

    @staticmethod
    def get_handler(filename: str) -> handler:
        extension = ".".join(os.path.basename(filename).split(".")[1:])
        return factory_handler.handler_builder[extension](filename)


factory_handler.register("bin.gz", create_word2vec_handler)
factory_handler.register("h5", create_hdf5_handler)
