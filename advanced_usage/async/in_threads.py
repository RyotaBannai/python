import asyncio
import time
import threading
from asyncio import AbstractEventLoop
from functools import partial
from typing import Any, Final, NamedTuple, Optional

Ok: Final[str] = "Ok"


class Result(NamedTuple):
    ok: Any = None
    err: Optional[Exception] = None


def some_task(n: int) -> Result:
    return Result(ok=n)


async def async_sub_worker(n: int):
    task1 = asyncio.create_task(some_task(n=n))
    await task1
    print(task1.result())


def worker(n: int, loop: AbstractEventLoop):
    # in thread and create async tasks
    # loop = asyncio.get_event_loop() -> RuntimeError: There is no current event loop in thread 'Thread-1'.
    loop.run_until_complete(async_sub_worker(n=n))


if __name__ == "__main__":
    # -> RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    loop = asyncio.get_event_loop()
    for n in range(2):
        threading.Thread(target=partial(worker, n=n, loop=loop)).start()
