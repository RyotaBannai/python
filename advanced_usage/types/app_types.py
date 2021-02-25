from typing import Any, Callable, Final, NamedTuple, Optional, TypedDict
from types import SimpleNamespace

Ok: Final[str] = "Ok"

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

    def ok_then(self, func: Optional[Callable] = None) -> "Result":
        if func is None:
            return Result(err=Exception("ok_then requires func"))
        if self.ok is not None:
            try:
                result = func(self.ok)
                if isinstance(result, Result):
                    if result.err is not None:
                        return Result(err=result.err)
                    else:
                        return Result(ok=result.ok)
                else:
                    return Result(ok=result if result is not None else Ok)
            except TypeError as e:
                return Result(err=e)
        else:
            return Result(err=Exception("ok is None"))

    def err_then(self, func: Optional[Callable] = None) -> "Result":
        if func is None:
            return Result(err=Exception("err_then requires func"))
        if self.err is not None:
            try:
                result: Result = func(self.err)
                if isinstance(result, Result):
                    if result.err is not None:
                        return Result(err=result.err)
                    else:
                        return Result(ok=result.ok)
                else:
                    return Result(ok=result if result is not None else Ok)
            except TypeError as e:
                return Result(err=e)
        else:
            return Result(err=Exception("ok is None"))


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

    def func1():
        for user in result.ok:
            print(f"{user.name} is {user.age} years old")

    def func2(users: Users):
        for user in users:
            print(f"{user.name} is {user.age} years old")

    # example 1
    result.ok_then(func=func1).err_then(func=lambda err: print(f"{err}"))

    # example 2
    result.ok_then(func=func2).ok_then(func=lambda ok: print("ok"))

    # example 3
    result.ok_then(func=func2).ok_then(func=lambda ok: print("ok")).ok_then(
        func=lambda ok: print("ok")
    )

    # example 4 // no good
    result.ok_then(lambda ok: Result(ok=Ok)).ok_then(
        lambda ok: Result(err=Exception("Err"))
    ).err_then(func=lambda err: print(err))
