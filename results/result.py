"""
Generated with sb3topy
"""
import asyncio
import math
import random
import time

import engine

class Stage(engine.Target):
    costume = -1

    costumes = [
        {
            'name': "backdrop1",
            'path': "3495321c6b96977754d0640a217b0bbb.png",
            'scale': 2,
            'center': (0, 0)
        },
    ]

    sounds = [
        {
            'name': "pop",
            'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
        }
        super().__init__(util)

    pass


class Sprite1(engine.Target):
    costume = 0

    costumes = [
        {
            'name': "costume1",
            'path': "680ccff3a18c704d946dd100c833bb9d.png",
            'scale': 2,
            'center': (95, 99)
        },
        {
            'name': "costume2",
            'path': "0891746f1b56ab1cd1623ce16871899b.png",
            'scale': 2,
            'center': (91, 105)
        },
    ]

    sounds = [
        {
            'name': "Meow",
            'path': "83c36d806dc92327b9e7049a565c6bff.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_message1': [
                self.broadcast_message1,
            ],
        }
        super().__init__(util)

    async def green_flag(self, util):
        util.send_event('broadcast_message1')



    async def broadcast_message1(self, util):
        self.xpos = 4
        self.ypos = 4
        self.set_direction(8)
        self.set_dirty(3)
        while True:
            radians = math.radians(self.direction)
            self.xpos += 4 * math.cos(radians)
            self.ypos += 4 * math.sin(radians)
            self.set_direction(self.direction + 4)
            self.change_effect('color', 4)
            await self._yield(3)


SPRITES = {
    'Stage': Stage,
    'Sprite1': Sprite1,
}

if __name__ == '__main__':
    engine.main(SPRITES)
