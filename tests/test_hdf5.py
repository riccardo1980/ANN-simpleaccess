import os
from unittest import TestCase

import numpy as np

from simpleaccess.provider import hdf5
from simpleaccess.provider.factory import factory_handler

ASSETS_FOLDER = os.path.join(".", "assets")


def test_register() -> None:
    factory_handler.register("h5", hdf5.create_hdf5_handler)

    reference_file = os.path.join(ASSETS_FOLDER, "test_data.h5")
    h = factory_handler.get_handler(reference_file)

    assert isinstance(h, hdf5.hdf5_handler)


def test_read() -> None:
    """
    TEST: read hdf5 file of a known content
    """
    reference_file = os.path.join(ASSETS_FOLDER, "test_data.h5")
    keys = ["key1", "key2"]
    vectors = np.asarray(
        (
            (1.0, 1.0, 1.0),
            (2.0, 2.0, 2.0),
        )
    )

    h = hdf5.hdf5_handler(reference_file)

    vr, kr = h.from_file()

    np.testing.assert_array_equal(vectors, vr, err_msg="Read vectors are not equal")
    TestCase().assertListEqual(keys, kr, msg="Read keys are not equal")


def test_write() -> None:
    """
    TEST: write hdf5 file and read back
    """
    reference_file = os.path.join(ASSETS_FOLDER, "temp.h5")
    keys = ["key1", "key2", "key3"]
    vectors = np.asarray(
        (
            (1.0, 1.0, 1.0, 1.0),
            (2.0, 2.0, 2.0, 2.0),
            (3.0, 3.0, 3.0, 3.0),
        )
    )

    h = hdf5.hdf5_handler(reference_file)
    h.to_file(vectors=vectors, keys=keys)

    vr, kr = h.from_file()

    np.testing.assert_array_equal(vectors, vr, err_msg="Read vectors are not equal")
    TestCase().assertListEqual(keys, kr, msg="Read keys are not equal")
