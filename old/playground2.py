import asyncio
import pprint


# pylint: disable=missing-docstring
class Test:
    def __init__(self):
        self.events = {
            "broadcast1": [self.func1, self.func2],
            "broadcast2": [self.func1, self.func2],
            "broadcast3": [self.func1, self.func2]
        }

        self.text = "Bob is cool"

    async def func1(self):
        print("Func1 A" + self.text)
        await asyncio.sleep(2)
        self.text = "Bob is cooler"
        print("Func1 B" + self.text)

    async def func2(self):
        print("Func2 A" + self.text)
        self.text = "Bob is awesome"
        await asyncio.sleep(3)
        print("Func2 B" + self.text)


def pack(coros):
    return [c() for c in coros]


async def main():
    print("Main A")
    t = Test()
    print(pprint.pformat(t.events))
    for i in range(3):
        l = pack(t.events["broadcast1"])
        task = asyncio.gather(*l)
        print("Main B")
        await asyncio.sleep(5)
        print("Main C")

asyncio.run(main())


"""
A model like below should work:

class
 - events

 events = {
     "name1": [func1, func2, ...],
     "name2": [func3, func4, ...]
 }

Use this model?
events = {
    "broadcasts": {
        "broadcast1": [func1, func2, ...],
    },
    "green_flag": [func1, func2, ...],
    "key_event": {
        "a": [func1, func2, ...],
    },
    "backdrop": {
        "backdrop1": [func1, func2, ...],
    }
}

Each sprite will have an events dict


"""


"""
New Model:
events = {
    "broadcast1": [func1, func2, ...]
}

"""
