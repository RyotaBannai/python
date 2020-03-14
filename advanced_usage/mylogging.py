import logging
import pathlib
import os

if __name__ == "__main__":
    dirname = pathlib.Path(os.path.dirname(__file__))
    # filemode='w'　で上書き
    datefmt = '%Y/%m/%d %H:%m'
    logging.basicConfig(format='%(asctime)s:%(message)s', filename=dirname /
                        'example.log', level=logging.DEBUG, datefmt=datefmt)
    # default logging level is warning.
    # logging.warning('woo ning')
    logging.info('i told you sooooon')  # not gonna show up by default
