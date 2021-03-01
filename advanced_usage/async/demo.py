import asyncio
import time
from typing import Any, Final, NamedTuple, Optional

Ok: Final[str] = "Ok"


class Result(NamedTuple):
    ok: Any = None
    err: Optional[Exception] = None


# async をつけると coroutine オブジェクトを生成するようになる
# コルーチンオブジェクトはイベントループ内でのみ実行可能
async def hello_world():
    print(f"Ok")


async def say_after(delay: int, what) -> Result:
    await asyncio.sleep(delay)
    print(f"{what=}")
    return Result(ok=what)


async def do_something_long():
    await hello_world()  # async の中でしか await できない
    task1 = asyncio.create_task(say_after(delay=1, what="hi"))
    await task1  # await してあげないと do_something_long() が先に終了（complete）する (呼び出し側で sleep しても関数自体が完了してしまっているため何も表示されない)
    print(task1.result())  # get result of task


async def main():
    # event_loop の中でなくても run の中で非同期処理が可能
    print(f"just async main")
    task1 = asyncio.create_task(say_after(delay=1, what="hi"))
    await task1
    print(task1.result())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_something_long())  # 引数内で実行
    asyncio.run(
        main()
    )  # this should be a function to run the top-level entry point “main()” function
