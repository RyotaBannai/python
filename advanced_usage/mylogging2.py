import logging
import logging.config
import pathlib
import os
_DIRNAME = pathlib.Path(os.path.dirname(__file__))

# https://docs.python.org/ja/3/library/logging.config.html#module-logging.config
# https://docs.python.org/ja/3/howto/
# https://docs.python.org/ja/3/library/logging.html


def randomfn():
    # __main__内で呼び出すと、funcname=<module>と表示される.
    logger.info('hi how are you')


if __name__ == "__main__":

    logging.config.fileConfig(_DIRNAME / 'logging.conf')

    logger = logging.getLogger('simpleExample')
    # dict 形式の環境設定ファイルの場合はdictConfigを使う。djangoはdictConfigを使用している.
    # ? print(logging.config.dictConfig({'simpleExample': 'level'}).configure())

    # create handler thereafter...
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    randomfn()
