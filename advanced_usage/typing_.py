from typing import Callable, List, Dict, Tuple, Sequence, TypeVar
# TODO: https://docs.python.org/ja/3/library/typing.html
# refs
# https://python.ms/type/
# https://www.python.org/dev/peps/pep-0484/
# https://qiita.com/icoxfog417/items/c17eb042f4735b7924a3

Address = Tuple[str, int]
ConnectionOption = Dict[str, str]
Server = Tuple[Address, ConnectionOption]

data = [
    (('Tokyo Region', 80),
     {'HTTPS': 'localhost'}),

    (('Los Angeles Region', 100),
     {'HTTPS': 'localhost'})
]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    print(message)
    print(servers)


A = TypeVar('A', str, bytes)  # Must be str or bytes


def longest(x: A, y: A) -> A:
    """
    Return the longest of two strings.
    """
    return x if len(x) >= len(y) else y


def f(some: str) -> None:
    print('{}'.format(f.__name__))


def ff(fn: Callable[[str], None]) -> None:
    fn('k')


if __name__ == "__main__":
    ff(f)
    lst: List[int]
    lst = [1]
    broadcast_message('howru', data)
