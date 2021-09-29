import logging.config
import os

import yaml


def setup(
    default_path: str = os.path.dirname(os.path.abspath(__file__)) + "/logging.yaml",
    default_level: int = logging.INFO,
    env_key: str = "LOG_CFG",
) -> None:
    """
    Setup logging configuration

    :param default_path: default value for logging conf. file
    :param default_level: default log level
    :param env_key: evironment variable to override configuration file

    Override choices a runtime by using specified environment variable
    """

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
