from typing import Any, Callable, Final, NamedTuple, Optional, TypedDict
from inspect import signature
from functools import partial

Ok: Final[str] = "Ok"


class Result(NamedTuple):
    ok: Any = None
    err: Optional[Exception] = None


class ResultChain:
    result: Optional[Result] = None

    def __init__(self, result: Result):
        self.result = result

    @classmethod
    def run(
        cls, func: Callable, initial_result: Optional[Result] = None
    ) -> "ResultChain":
        if initial_result is not None and not isinstance(initial_result, Result):
            return cls(
                result=Result(
                    err=Exception("initial_result must be instance of Result")
                )
            )
        return cls(
            result=Result(ok=Ok) if initial_result is None else initial_result
        ).and_then(func=func)

    # helpers
    def and_then(self, func: Callable) -> "ResultChain":
        func_name = getattr(func, "__name__", repr(func))
        # below returns Signature.empty if no return_annotation
        func_return_type: object = signature(func).return_annotation
        # class の判定は is を使う.
        if func_return_type is not Result:
            return ResultChain(
                result=Result(
                    err=Exception(f"func: {func_name} may not return Result type.")
                )
            )
        if self.result is None:
            return ResultChain(result=Result(err=Exception("Call run first.")))

        if self.result.err is not None:
            return ResultChain(result=self.result)
        else:
            try:
                # parameters returns OrderedDict
                if "result" in signature(func).parameters:
                    func_result: Any = func(result=self.result)
                else:
                    func_result: Any = func()

                if isinstance(func_result, Result):
                    return ResultChain(result=func_result)
                else:
                    return ResultChain(
                        result=Result(
                            err=Exception(
                                f"func: {func_name} returned non Result type."
                            )
                        )
                    )
            except Exception as e:
                return ResultChain(result=Result(err=e))

    def unwrap(self) -> Result:
        return self.result


if __name__ == "__main__":

    def my_initial_func() -> Result:
        return Result(ok=Ok)

    def my_second_func() -> Result:
        return Result(err=Exception("test"))

    def my_third_func() -> Result:
        return Result(ok="last")

    my_lambda_func: Callable[[], Result] = lambda: Result(ok=Ok)  # this doesn't help
    # .and_then(func=my_lambda_func) // signature が ()
    # but you can dynamically annotate it
    my_lambda_func.__annotations__["return"] = Result

    # partial works as long as the given func has return annotation.
    my_partial = partial(my_lambda_func)

    def counter(result: Result = None) -> Result:
        if result is not None:
            return Result(
                ok=result.ok + 1
                if result.err is None and isinstance(result.ok, int)
                else 1
            )
        else:
            return Result(ok=1)

    # run funcs orderly and if one of them failed the result all fail.
    # result_chain: ResultChain = (
    #     ResultChain.run(func=my_initial_func)
    #     .and_then(func=my_second_func)
    #     .and_then(func=my_lambda_func)
    #     .and_then(func=my_partial)
    #     .and_then(func=partial(my_initial_func))
    #     .and_then(func=my_third_func)
    # )

    result_chain: ResultChain = (
        ResultChain.run(func=counter, initial_result=Result(ok=10))
        .and_then(func=counter)
        .and_then(func=counter)
    )

    # print(result_chain)
    # print(result_chain.unwrap())
    # ->
    # <__main__.ResultChain object at 0x10b198460>
    # Result(ok=None, err=Exception('test'))

    if result_chain.unwrap().err is not None:
        print(result_chain.unwrap())
    else:
        print("OK")
        print(result_chain.unwrap())
        # Result(ok=3, err=None)

    # ...
