from typing import Any, NamedTuple, Optional, TypedDict
from types import SimpleNamespace

# NestedNamespace
class Dotty(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, Dotty(value))
            else:
                self.__setattr__(key, value)


# https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python

Article = TypedDict("Users", {"content": str, "title": str})
Users = TypedDict("Users", {"name": str, "age": int, "article": Article})


class Result(NamedTuple):
    ok: Any = None
    err: Optional[Exception] = None


class Api:
    @classmethod
    def fetch_users(cls) -> Result(ok=Optional[Users], err=Optional[Exception]):
        users = [
            {
                "name": "test",
                "age": 20,
                "article": {"content": "abc", "title": "alphabet"},
            },
            {
                "name": "test",
                "age": 20,
                "article": {"content": "abc", "title": "alphabet"},
            },
        ]
        return Result(ok=[Dotty(user) for user in users])


if __name__ == "__main__":
    result: Result = Api.fetch_users()
    if result.err is not None:
        raise result.err
    else:
        for user in result.ok:
            print(f"{user.name} is {user.age} years old")
