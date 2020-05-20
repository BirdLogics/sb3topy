#pylint:disable=all
import asyncio
from asyncio import sleep

import time

async def loop(l, t=1, c=3):
    for i in range(c):
        time.sleep(1)
        print(l, i)
        await sleep(0)


async def main():
    await asyncio.gather(loop("A"), loop("B",9), loop("C"))

class ScratchCat:
    def __init__(self):
        pass


asyncio.run(main())