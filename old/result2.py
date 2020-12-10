"""
Generated with sb3topy
"""
import asyncio
import math
import random

import engine


class Stage(engine.Target):  # engine.Target
    direction = 0
    costumes = [
        {
            "assetId": "797b03bdb8cf6ccfc30c0692d533d998",
            "name": "backdrop1",
            "bitmapResolution": 2,
            "md5ext": "797b03bdb8cf6ccfc30c0692d533d998.png",
            "dataFormat": "png",
            "rotationCenterX": 480,
            "rotationCenterY": 360
        }
    ]
    sounds = [
        {
            "assetId": "83a9787d4cb6f3b7632b4ddfebf74367",
            "name": "pop",
            "dataFormat": "wav",
            "format": "",
            "rate": 48000,
            "sampleCount": 1123,
            "md5ext": "83a9787d4cb6f3b7632b4ddfebf74367.wav"
        }
    ]

    def __init__(self, util):
        self.hats = {}
        super().__init__(util)


class Sprite1(engine.Target):
    # TODO Costume/Sound dicts
    costumes = [
        {
            "assetId": "106798711d0220a08cca12e750468e2b",
            "name": "costume1",
            "bitmapResolution": 2,
            "md5ext": "106798711d0220a08cca12e750468e2b.png",
            "dataFormat": "png",
            "rotationCenterX": 96,
            "rotationCenterY": 99
        },
        {
            "assetId": "27a0bf89451a32a7eea1930e3e2bfce4",
            "name": "costume2",
            "bitmapResolution": 2,
            "md5ext": "27a0bf89451a32a7eea1930e3e2bfce4.png",
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

    # TODO x/ypos
    xpos = 0
    ypos = 0

    def __init__(self, util):
        # TODO Hats
        self.hats = {
            "green_flag": [self.green_flag]
        }

        # TODO Super init
        super().__init__(util)

        self.sprite.visible = 1  # TODO visible

    async def green_flag(self, util):  # TODO Util param
        self.xpos = 0
        self.ypos = 0
        while True:
            radians = math.radians(self.direction)
            #print(f"Rads: {radians}, Degs: {90-self.direction}")
            self.xpos += 10 * math.cos(radians)
            self.ypos += 10 * math.sin(radians)
            self.set_direction(self.direction + 15)
            self.change_effect('color', 5)
            await self.do_yield(3)  # TODO Yield dirty


if __name__ == '__main__':
    engine.main({"Sprite1": Sprite1, "Stage": Stage})
