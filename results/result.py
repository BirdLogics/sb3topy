"""
Generated with sb3topy
"""
import asyncio
import math
import random
import time

import engine

class Stage(engine.Target):
    costume = 1
    xpos, ypos = 0, 0
    direction = 90
    visible = True

    costumes = [
        {
            'name': "backdrop1",
            'path': "3495321c6b96977754d0640a217b0bbb.png",
            'center': (0, 0),
            'scale': 2
        },
        {
            'name': "Playing Field",
            'path': "2de108f3098e92f5c5976cf75d38e99d.png",
            'center': (480, 360),
            'scale': 2
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
        self.sprite._layer = 0

    pass


class Sprite1(engine.Target):
    costume = 3
    xpos, ypos = 42.50073635671901, -11.388037984510913
    direction = 105
    visible = True

    costumes = [
        {
            'name': "costume1",
            'path': "680ccff3a18c704d946dd100c833bb9d.png",
            'center': (0, -1),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "0891746f1b56ab1cd1623ce16871899b.png",
            'center': (92, 105),
            'scale': 2
        },
        {
            'name': "Playing Field",
            'path': "2de108f3098e92f5c5976cf75d38e99d.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "b04ae60e87b53d62a9b77449610bcfa9.png",
            'center': (37, 93),
            'scale': 2
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
        }
        super().__init__(util)
        self.sprite._layer = 2

    async def green_flag(self, util):
        pass



class Sprite2(engine.Target):
    costume = 1
    xpos, ypos = 0, 0
    direction = 90
    visible = True

    costumes = [
        {
            'name': "costume1",
            'path': "41d8cb74d9d006bbfbdf3eca1aa3ee0e.png",
            'center': (5, 5),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "eda4d6c27b06f31584314e1082da5a71.png",
            'center': (18, 103),
            'scale': 2
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
        self.sprite._layer = 3

    pass


class Sprite3(engine.Target):
    costume = 2
    xpos, ypos = 0, 0
    direction = 105
    visible = True

    costumes = [
        {
            'name': "costume1",
            'path': "680ccff3a18c704d946dd100c833bb9d.png",
            'center': (0, -1),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "0891746f1b56ab1cd1623ce16871899b.png",
            'center': (92, 105),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "9c0a7567e9e79089da437a14da5e434a.png",
            'center': (57, 1),
            'scale': 2
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
            'broadcast_message1': [
                self.broadcast_message1,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 1

    async def broadcast_message1(self, util):
        pass

SPRITES = {
    'Stage': Stage,
    'Sprite1': Sprite1,
    'Sprite2': Sprite2,
    'Sprite3': Sprite3,
}

if __name__ == '__main__':
    engine.main(SPRITES)
