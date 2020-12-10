"""
Generated with sb3topy
"""
import asyncio
import math
import random
import time

import engine


class Stage(engine.Target):
    pass


class Sprite1(engine.Target):

    costume = 0

    costumes = [
        {
            "assetId": "680ccff3a18c704d946dd100c833bb9d",
            "name": "costume1",
            "bitmapResolution": 2,
            "md5ext": "680ccff3a18c704d946dd100c833bb9d.png",
            "dataFormat": "png",
            "rotationCenterX": 95,
            "rotationCenterY": 99
        },
        {
            "assetId": "0891746f1b56ab1cd1623ce16871899b",
            "name": "costume2",
            "bitmapResolution": 2,
            "md5ext": "0891746f1b56ab1cd1623ce16871899b.png",
            "dataFormat": "png",
            "rotationCenterX": 91,
            "rotationCenterY": 105
        }
    ]
    sounds = [
        {
            "assetId": "83c36d806dc92327b9e7049a565c6bff",
            "name": "Meow",
            "dataFormat": "wav",
            "format": "",
            "rate": 48000,
            "sampleCount": 40681,
            "md5ext": "83c36d806dc92327b9e7049a565c6bff.wav"
        }
    ]

    def __init__(self, util):
        self.hats = {
            "green_flag": [self.green_flag],
            "broadcast_message1": [self.broadcast_message1]
        }
        super().__init__(util)

    async def green_flag(self, util):
        util.send_event('broadcast_message1')

    async def broadcast_message1(self, util):
        self.xpos = 4
        self.ypos = 4
        self.set_direction(8)
        self.set_dirty(1) # TODO Dirty = 0?
        while True:
            radians = math.radians(self.direction)
            self.xpos += 4 * math.cos(radians)
            self.ypos += 4 * math.sin(radians)
            self.set_direction(self.direction + 4)
            self.change_effect('color', 4) # TODO lowercase this
            await self.do_yield(3) # TODO Yield after loop

if __name__ == '__main__':
    engine.main({'Sprite1': Sprite1})