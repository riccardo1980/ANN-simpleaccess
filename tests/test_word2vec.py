import os

from simpleaccess.provider import word2vec
from simpleaccess.provider.factory import factory_handler

ASSETS_FOLDER = os.path.join(".", "assets")


def test_register() -> None:
    factory_handler.register("bin.gz", word2vec.create_word2vec_handler)

    reference_file = os.path.join(ASSETS_FOLDER, "test_data.bin.gz")
    h = factory_handler.get_handler(reference_file)

    assert isinstance(h, word2vec.word2vec_handler)


def test_read() -> None:
    "not implemented: no reference file"
    pass


def test_write() -> None:
    "not implemented: write is not implemented"
    pass
