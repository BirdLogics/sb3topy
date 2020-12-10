import asyncio

async def func1():
    print("A1")
    asyncio.ensure_future(func2())
    print("A2")
    asyncio.gather(func3())
    while True:
        await asyncio.sleep(0)
    print("A3")

async def func2():
    print("B")

async def func3():
    print("C1")
    await asyncio.sleep(0.1)
    print("C3")

asyncio.run(func1(), debug=True)

