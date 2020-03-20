"""
 any useful reusable library can be this subdirectry.
"""
import sys
import os
import pathlib
from pprint import pprint
import pathlib


def return_project_path():
    package_root_path = pathlib.Path(os.path.dirname(__file__)).parents[1]
    # add package root path to $PYTHONPATH
    sys.path.insert(0, str(package_root_path))
    return package_root_path


def return_sys_path():
    return sys.path


class BB(object):
    def __init__(self):
        print('class BB')


if __name__ == "__main__":
    osdir = os.path.dirname(os.__file__)
    print(os.__file__)
    print('*'*40)
    # print(sys.path)
    print('*'*40)
    print(__package__)  # shows dot module path to this module.

    mypath = return_project_path()

    # もしパッケージのルートパスを $PYTHONPATHに追加すれば、
    # module実行で相対的にパスを指定しなくてもmoduleをimport できる.
    from A.B.b import B
    B()
    pprint(return_sys_path())
