#!/usr/bin/env python

import argparse
import logging

import numpy as np

from simpleaccess import logging_setup
from simpleaccess.provider.factory import factory_handler

log = logging.getLogger(__name__)


def main(source_file: str, amount: int) -> None:

    reader = factory_handler.get_handler(source_file)

    vectors, keys = reader.from_file()
    n = 0
    for v, k in zip(vectors, keys):
        print("{} {}".format(k, np.array_repr(v).replace("\n", "")))
        n += 1
        if n > amount:
            break


if __name__ == "__main__":
    logging_setup.setup(default_path="logging.yaml")

    parser = argparse.ArgumentParser(
        description="File peek", formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("dataset", nargs="*", help="Provide a number of input files")

    args = parser.parse_args()
    args_dict = vars(args)

    try:
        log.info(args_dict)
        for src in args_dict["dataset"]:

            log.info("Source: {}".format(src))
            main(src, 10)

    except Exception as e:
        log.error(e)
        raise  # raising will get process exit and stack unwinding
