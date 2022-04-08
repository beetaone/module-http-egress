"""logging configurations"""
from logging import DEBUG, basicConfig


def configure_logging():
    basicConfig(
        level=DEBUG,
        format="{'levelname': '%(levelname)s', 'asctime': '%(asctime)s', 'name': '%(name)s', 'message': '%(message)s'}",
    )
