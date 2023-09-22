import logging

fmt = {
    'app_name': 'blockchain',
    'time': '%(asctime)s',
    'name': '%(name)s',
    'level': '%(levelname)s',
    'msg': '%(message)s'
}
logging.basicConfig(level=logging.INFO, format=str(fmt), datefmt="%Y-%m-%dT%H:%M:%S%z")


def get_logger(name: str):
    return logging.getLogger(name)
