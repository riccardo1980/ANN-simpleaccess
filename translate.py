#!/usr/bin/env python

import argparse
import logging

from simpleaccess import logging_setup
from simpleaccess.provider.factory import factory_handler

log = logging.getLogger(__name__)


def main(source_file: str, dest_file: str) -> None:

    reader = factory_handler.get_handler(source_file)
    writer = factory_handler.get_handler(dest_file)

    vectors, keys = reader.from_file()
    writer.to_file(vectors, keys)


if __name__ == "__main__":
    logging_setup.setup(default_path="logging.yaml")

    parser = argparse.ArgumentParser(
        description="Format translator", formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "dataset", nargs="*", help="Provide couple of <src> <dest> files"
    )

    args = parser.parse_args()
    args_dict = vars(args)

    # check
    if len(args_dict["dataset"]) % 2 != 0:
        raise ValueError("File names must be couple src/dest")

    try:
        log.info(args_dict)
        for src, dest in zip(args_dict["dataset"][::2], args_dict["dataset"][1::2]):

            log.info("Source: {} Dest: {}".format(src, dest))
            main(src, dest)

    except Exception as e:
        log.error(e)
        raise  # raising will get process exit and stack unwinding
