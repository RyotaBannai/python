import asyncio
import time
import threading
from asyncio import AbstractEventLoop
from functools import partial
from typing import Any, Final, NamedTuple, Optional
from queue import Queue


Ok: Final[str] = "Ok"


class Result(NamedTuple):
    ok: Any = None
    err: Optional[Exception] = None


def some_task(n: int) -> Result:
    return Result(ok=n)


async def task(n: int, q: Queue):
    print(f"async task {n} is called.")
    # time.sleep(1)
    asyncio.sleep(1)
    # put result
    q.put(some_task(n=n))


async def async_main(q: Queue):
    loop = asyncio.get_event_loop()
    tasks = list()
    for n in range(3):
        tasks.append(
            asyncio.create_task(task(n=n, q=q))
        )  # run before do something with list..
        # doesn't work because anyways gather or await blocks thread... and while True will run thereafter.


def worker(item: Result):
    print(f"do someting in thread..")


if __name__ == "__main__":
    q = Queue()
    asyncio.run(async_main(q=q))

    # loop.run_until_complete(async_sub_worker(n=n))
    while True:
        if not q.empty():
            item = q.get()
            threading.Thread(target=partial(worker, item=item)).start()
