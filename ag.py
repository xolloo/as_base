import asyncio


async def serve(val):
    await asyncio.sleep(val / 10)
    print("work")
    print("not")
    return val


def res_cb(task: asyncio.Task):
    if not task.cancelled():
        print(task.result())
    else:
        print("Task is cancel")


async def coro(val):
    print("start")
    print("HELLO")
    tasks = asyncio.gather(serve(val), serve(val + 1))
    print("end")
    await tasks
    print(tasks.result())


if __name__ == '__main__':
    asyncio.run(coro(5))
