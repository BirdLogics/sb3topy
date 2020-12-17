"""
Generated with sb3topy
"""
import asyncio
import math
import random
import time

import engine
from engine import Value

class SpriteStage(engine.Target):
    costume = 1
    xpos, ypos = 0, 0
    direction = 90
    visible = True

    costumes = [
        {
            'name': "background1",
            'path': "1af373d3b7464a8af1a32fd051effbec.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background2",
            'path': "8a95ad28c2e25e18cdbde76a45120cd0.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background3",
            'path': "f5394526f852ccd2567876b395894d59.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background4",
            'path': "485017a18ddf105e236e49576a65d641.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background5",
            'path': "1c0a59735c5cf80ce6528bb5b4b9b2de.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background6",
            'path': "cce512cf9af05a32a0a430a7530e7446.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background7",
            'path': "a81f62d19ecdde6630f76586c9bf51ff.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background8",
            'path': "d9abdbe9f8f77601cd8819d27c8cd990.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background9",
            'path': "2a3fd57cdaa3eab75dc1b2812aa4ec0b.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background10",
            'path': "3ed5ddd1d0f241b317fb0b0bf7786eb1.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background11",
            'path': "f29e86bad9c5bbe3eef9a10366bd740e.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background12",
            'path': "d4910d9b756d9c26077a286f414eda1b.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background13",
            'path': "10797d2fc54ab59ae4f3b8e602c089b1.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background14",
            'path': "c4271d5fe4fbdab4a97c06ebdbd9d16a.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background15",
            'path': "f58f0661c83b2f3a288b59d8492df24d.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background16",
            'path': "27c13f6c916f1f59c49d853e57bf3346.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "RFClip1",
            'path': "e0292660634aee44d7e3eacf33d9af08.wav"
        },
        {
            'name': "Swoosh",
            'path': "d9ca82a22e133716ca9627a1e71cd39a.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_WheresMyTaco': [
                self.broadcast_WheresMyTaco,
            ],
            'broadcast_Drrr': [
                self.broadcast_Drrr,
            ],
            'broadcast_IsHeDead': [
                self.broadcast_IsHeDead,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
                self.broadcast_Play1,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_ThatGuy': [
                self.broadcast_ThatGuy,
            ],
            'broadcast_OhBoy': [
                self.broadcast_OhBoy,
                self.broadcast_OhBoy1,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 0

    async def broadcast_WheresMyTaco(self, util):
        util.stage.costume = util.stage.get_costume('background15')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_Drrr(self, util):
        util.stage.costume = util.stage.get_costume('background16')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_IsHeDead(self, util):
        util.stage.costume = util.stage.get_costume('background15')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_Play(self, util):
        self.variables['uhoh'] = 0
        while not (self.variables['UhOh'] == 1):
            util.stage.costume = util.stage.get_costume('background2')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background3')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background4')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background5')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            await self._yield(0)

        for _ in range(5):
            util.stage.costume = util.stage.get_costume('background2')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background3')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background4')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background5')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            await self._yield(0)

        for _ in range(2):
            util.stage.costume = util.stage.get_costume('background2')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.1)
            util.stage.costume = util.stage.get_costume('background3')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.1)
            util.stage.costume = util.stage.get_costume('background4')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.1)
            util.stage.costume = util.stage.get_costume('background5')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.1)
            await self._yield(0)

        util.stage.costume = util.stage.get_costume('background4')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)

        await self.sleep(1)
        util.stage.costume = util.stage.get_costume('background5')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)

        await self.sleep(1)
        util.stage.costume = util.stage.get_costume('background1')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_Play1(self, util):
        await self.sleep(3)
        self.sounds.set_volume(30)
        await self.sounds.play('RFClip1')


    async def green_flag(self, util):
        util.stage.costume = util.stage.get_costume('background2')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_ThatGuy(self, util):
        while not (self.variables['UhOh'] == 0):
            util.stage.costume = util.stage.get_costume('background2')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background3')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background4')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background5')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)

            await self.sleep(0.05)
            await self._yield(0)

        self.sounds.play('Swoosh')
        util.stage.costume = util.stage.get_costume('background7')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)

        for _ in range(5):
            await self.sleep(0.06)
            next_backdrop = util.stage.costume['number'] + 1
            if next_backdrop == len(util.stage.costumes):
                util.stage.costume = util.stage.costumes[0]
            else:
                util.stage.costume = util.stage.costumes[next_backdrop]
            util.send_event('onbackdrop_' + self.costume['name'])
            await self._yield(3)

        await self.sleep(0.1)
        util.send_event('broadcast_FemaleScream')
        util.stage.costume = util.stage.get_costume('background13')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_OhBoy(self, util):
        util.stage.costume = util.stage.get_costume('background14')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_OhBoy1(self, util):
        for _ in range(30):
            await self.sleep(0.01)
            self.sounds.change_volume(-1)
            await self._yield(0)




class Sprite_title(engine.Target):
    costume = 1
    xpos, ypos = 0, 0
    direction = 90
    visible = True

    costumes = [
        {
            'name': "costume4",
            'path': "3d1622671c37d48f120a5eb33e610b40.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "4b13524cd79f87e7b7bdeec970409e6a.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "SandstormClip",
            'path': "40541aa7dc0d745b7865e752ba25c9f4.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
                self.green_flag1,
                self.green_flag2,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 16

    async def green_flag(self, util):
        self.set_costume('costume2')
        self.variables['menu'] = 1
        self.set_dirty(3)

        while not (self.variables['Menu'] == 0):
            await self.sleep(0.1)
            self.set_costume('costume3')
            self.set_dirty(3)

            await self.sleep(0.1)
            self.set_costume('costume4')
            await self._yield(3)



    async def broadcast_Play(self, util):
        self.variables['menu'] = 0
        self.front_layer(util)
        self.change_layer(util, -2)
        for _ in range(10):
            self.sounds.change_volume(-10)
            self.change_effect('ghost', 10)
            self.set_dirty(3)

            await self.sleep(0.2)
            await self._yield(0)

        self.sounds.stop_all(util)
        self.visible = 0
        self.set_dirty(1)


    async def green_flag1(self, util):
        self.set_effect('brightness', -100)
        self.xpos = 0
        self.ypos = 0
        self.sounds.set_volume(100)
        self.set_effect('ghost', 0)
        self.visible = 1
        self.set_dirty(3)

        await self.sleep(1)
        for _ in range(10):
            self.change_effect('brightness', 10)
            self.set_dirty(3)

            await self.sleep(0.1)
            await self._yield(0)

        while not (self.variables['Menu'] == 0):
            await self.sounds.play('SandstormClip')
            await self._yield(0)



    async def green_flag2(self, util):
        self.set_effect('pixelate', 0)
        self.variables['menu'] = 1
        self.set_dirty(3)

        while not (self.variables['Menu'] == 0):
            await self.sleep(5)
            for _ in range(5):
                self.change_effect('pixelate', 20)
                self.set_dirty(3)

                await self.sleep(0.01)
                await self._yield(0)

            for _ in range(5):
                self.change_effect('pixelate', -20)
                self.set_dirty(3)

                await self.sleep(0.01)
                await self._yield(0)

            await self._yield(0)




class Sprite_play(engine.Target):
    costume = 0
    xpos, ypos = -178, -15
    direction = 90
    visible = True

    costumes = [
        {
            'name': "coollogo_com-1",
            'path': "2ee0ecd44a2f1a2184ad3a3f8db3c297.png",
            'center': (124, 62),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'sprite_clicked': [
                self.sprite_clicked,
            ],
            'green_flag': [
                self.green_flag,
                self.green_flag1,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 25

    async def sprite_clicked(self, util):
        for _ in range(5):
            self.change_effect('ghost', 10)
            self.set_dirty(3)

            await self.sleep(0.2)
            await self._yield(0)

        util.send_event('broadcast_Play')
        self.front_layer(util)
        for _ in range(5):
            self.change_effect('ghost', 10)
            self.set_dirty(3)

            await self.sleep(0.2)
            await self._yield(0)

        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.size = 70
        self.set_dirty(3)

        await self.sleep(3)
        self.visible = 1
        self.front_layer(util)
        self.xpos = -178
        self.ypos = -205
        await self.glide(1, -178, -15)
        self.set_dirty(2)


    async def green_flag1(self, util):
        self.set_effect('pixelate', 0)
        self.set_dirty(3)

        while not (self.variables['Menu'] == 0):
            await self.sleep(5)
            for _ in range(5):
                self.change_effect('pixelate', 20)
                self.set_dirty(3)

                await self.sleep(0.01)
                await self._yield(0)

            for _ in range(5):
                self.change_effect('pixelate', -20)
                self.set_dirty(3)

                await self.sleep(0.01)
                await self._yield(0)

            await self._yield(0)




class SpriteSprite1(engine.Target):
    costume = 30
    xpos, ypos = -84, -57
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "cc5d1382cbe467a146ef4b47b18085f0.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "e01f59cce380c719cfc6f1c7cfcf82ca.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "98a936924fc896b8aadac1e607a99f31.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "1051b2e653cbefd3ed31c697cf272eec.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "d6fc19c45e458be95f7e6a99692af873.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "c55d3d74cc0f5b9800b5cd0f23cc7c17.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "661fb4136edd0b4e7557ed07a14d5ea5.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "c55d3d74cc0f5b9800b5cd0f23cc7c17.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "c626545ca7f0a7ca80a6ce02ced4f18d.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "fb3e6a4a7e2791a88681a4529bac9ba5.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "620841c4df4a43f07e16e0f49ac272d8.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "2bde90d58050c16c123a29f28cb782ab.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "98a936924fc896b8aadac1e607a99f31.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "1051b2e653cbefd3ed31c697cf272eec.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "1051b2e653cbefd3ed31c697cf272eec.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "c626545ca7f0a7ca80a6ce02ced4f18d.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "c626545ca7f0a7ca80a6ce02ced4f18d.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "1bf236791441904cd17bc52a1bfbd0e1.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "661fb4136edd0b4e7557ed07a14d5ea5.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "fb3e6a4a7e2791a88681a4529bac9ba5.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "c626545ca7f0a7ca80a6ce02ced4f18d.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "661fb4136edd0b4e7557ed07a14d5ea5.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "20dbdbb02b02951d7f7b36670bafa25b.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "20dbdbb02b02951d7f7b36670bafa25b.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "1051b2e653cbefd3ed31c697cf272eec.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "c626545ca7f0a7ca80a6ce02ced4f18d.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "8bab36736003a995a16d8f8e045e884d.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "981e33571a2060572dc02ce2da80232f.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume29",
            'path': "c516a6cf1e8de5844f8d59d5ab1702e4.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume30",
            'path': "f6e9ffb8ab42f3a29bdbfcdf03fc43c9.png",
            'center': (186, 250),
            'scale': 2
        },
        {
            'name': "costume31",
            'path': "f9c5d955abda283b86dd3007210eb570.png",
            'center': (186, 250),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "DidntSeeThatOne",
            'path': "fdeaef5122f8e36c645a55629d7687f6.wav"
        },
        {
            'name': "HaHaHa",
            'path': "2656b69baf708ba93c3a970d2da5fdf3.wav"
        },
        {
            'name': "Piff",
            'path': "1b59efcfa3b640a8c8fd7233b9b30833.wav"
        },
        {
            'name': "DidntSeeThatOne1",
            'path': "d70fc4f6cfe913ffe470d6f3b0bbb2cd.wav"
        },
        {
            'name': "HaHaHa1",
            'path': "8a8a144bf71b14ddd5b45f496f7fa707.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Kablammie': [
                self.broadcast_Kablammie,
            ],
            'broadcast_Hiya': [
                self.broadcast_Hiya,
            ],
            'broadcast_HaHaHa': [
                self.broadcast_HaHaHa,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'broadcast_Piff': [
                self.broadcast_Piff,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 4

    async def broadcast_Kablammie(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Hiya(self, util):
        self.size = 75
        self.xpos = -84
        self.ypos = -57
        self.visible = 1
        self.set_dirty(3)


    async def broadcast_HaHaHa(self, util):
        self.set_costume('costume31')
        await self.glide(2, -126, 5)
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Play(self, util):
        self.size = 100
        self.set_costume('costume2')
        self.visible = 1
        self.xpos = 151
        self.ypos = 5
        self.set_dirty(3)

        await self.sleep(5)
        self.sounds.play('DidntSeeThatOne1')
        self.set_costume('costume3')
        self.set_dirty(3)

        for _ in range(23):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(0.5)
        self.sounds.play('HaHaHa1')
        self.set_costume('costume28')
        self.set_dirty(3)

        await self.sleep(0.1)
        self.set_costume('costume29')
        self.set_dirty(3)

        await self.sleep(0.1)
        self.set_costume('costume28')
        self.set_dirty(3)

        await self.sleep(0.1)
        self.set_costume('costume29')
        self.set_dirty(3)

        await self.sleep(0.1)
        self.set_costume('costume28')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume29')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume28')
        self.set_dirty(3)

        await self.sleep(1)
        util.send_event('broadcast_HaHaHa')


    async def broadcast_Piff(self, util):
        self.sounds.play('Piff')
        await self.glide(0.1, -233, 5)
        self.visible = 0
        self.set_dirty(2)



class SpriteSprite2(engine.Target):
    costume = 0
    xpos, ypos = -87, -39
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "b389d214bf6c1aa5560f7217e325270c.png",
            'center': (18, 34),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Kablammie': [
                self.broadcast_Kablammie,
            ],
            'broadcast_Hiya': [
                self.broadcast_Hiya,
            ],
            'broadcast_HaHaHa': [
                self.broadcast_HaHaHa,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'broadcast_Piff': [
                self.broadcast_Piff,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 15

    async def broadcast_Kablammie(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Hiya(self, util):
        self.size = 75
        self.xpos = -87
        self.ypos = -39
        self.visible = 1
        self.set_dirty(3)


    async def broadcast_HaHaHa(self, util):
        await self.glide(2, -131, 31)
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Play(self, util):
        self.size = 100
        self.visible = 1
        self.front_layer(util)
        self.change_layer(util, -3)
        self.xpos = 146
        self.ypos = 31
        self.set_direction(90)
        self.set_dirty(3)

        while True:
            for _ in range(9):
                await self.sleep(0.01)
                self.set_direction(self.direction + 10)
                await self._yield(3)

            for _ in range(9):
                await self.sleep(0.01)
                self.set_direction(self.direction + -10)
                await self._yield(3)

            await self._yield(0)



    async def broadcast_Piff(self, util):
        await self.glide(0.1, -243, 31)
        self.visible = 0
        self.set_dirty(2)



class SpriteSprite4(engine.Target):
    costume = 0
    xpos, ypos = -131, -41
    direction = 60
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "a3ad85b64165eb33c45a6ee9b96ed73c.png",
            'center': (150, 62),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Kablammie': [
                self.broadcast_Kablammie,
            ],
            'broadcast_Hiya': [
                self.broadcast_Hiya,
            ],
            'broadcast_HaHaHa': [
                self.broadcast_HaHaHa,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'broadcast_Piff': [
                self.broadcast_Piff,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 3

    async def broadcast_Kablammie(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Hiya(self, util):
        self.size = 75
        self.xpos = -131
        self.ypos = -41
        self.visible = 1
        self.set_dirty(3)


    async def broadcast_HaHaHa(self, util):
        await self.glide(2, -192, 27)
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Play(self, util):
        self.size = 100
        self.visible = 1
        self.change_layer(util, -99)
        self.xpos = 90
        self.ypos = 27
        self.set_direction(90)
        self.set_dirty(3)

        while True:
            for _ in range(9):
                await self.sleep(0.01)
                self.set_direction(self.direction + -10)
                await self._yield(3)

            for _ in range(9):
                await self.sleep(0.01)
                self.set_direction(self.direction + 10)
                await self._yield(3)

            await self._yield(0)



    async def broadcast_Piff(self, util):
        await self.glide(0.1, -312, 27)
        self.visible = 0
        self.set_dirty(2)



class SpriteSprite3(engine.Target):
    costume = 1
    xpos, ypos = -108, -115
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "5d5dab7178b277d34f773d9af5071dff.png",
            'center': (160, 98),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "be4e84c556a493b35a4affaea99e12ba.png",
            'center': (160, 98),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Kablammie': [
                self.broadcast_Kablammie,
            ],
            'broadcast_Hiya': [
                self.broadcast_Hiya,
            ],
            'broadcast_HaHaHa': [
                self.broadcast_HaHaHa,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'broadcast_Piff': [
                self.broadcast_Piff,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 14

    async def broadcast_Kablammie(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Hiya(self, util):
        self.size = 75
        self.xpos = -108
        self.ypos = -115
        self.visible = 1
        self.set_dirty(3)


    async def broadcast_HaHaHa(self, util):
        await self.glide(2, -163, -77)
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Play(self, util):
        self.size = 100
        self.visible = 1
        self.set_costume('costume1')
        self.front_layer(util)
        self.change_layer(util, -4)
        self.xpos = 115
        self.ypos = -77
        self.set_dirty(3)

        while True:
            await self.sleep(0.01)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)



    async def broadcast_Piff(self, util):
        await self.glide(0.1, -290, -78)
        self.visible = 0
        self.set_dirty(2)



class SpriteSprite5(engine.Target):
    costume = 12
    xpos, ypos = -48, -39
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume2",
            'path': "c78a0195eb1ef3578d4468c29dba927f.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "1ccec7b5278bbd76086adfd3c3ef88c4.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "494c5b5a55bccea07abad8d84e16a49c.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "fc0fd836e39a565eae541c2f63bba69a.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "494c5b5a55bccea07abad8d84e16a49c.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "b5f9c6cc1658093ddde223b1d06f08ad.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "f3b1465c715f7baabfd1956b12e5f78d.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "6d3e11da96465c5ce057d3fbcdf1c94d.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "1ccec7b5278bbd76086adfd3c3ef88c4.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "e5264186e7e891798d6ff947606cd8bc.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "aafeb64732f775e426c86eec7628053d.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "c31023e281080d2c41ae76aedf2bcbd4.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "16b3e96643204811875ba6f75140087c.png",
            'center': (252, 290),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "GiveItBack",
            'path': "b50990168f091aa5324593a8b7fa7ce5.wav"
        },
        {
            'name': "Hiya",
            'path': "211d58b810aeeb0f7ea36e0632e35f4b.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Hiya': [
                self.broadcast_Hiya,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_HaHaHa': [
                self.broadcast_HaHaHa,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 5

    async def broadcast_Hiya(self, util):
        self.size = 75
        self.xpos = 147
        self.ypos = 76
        self.set_costume('costume12')
        self.visible = 1
        self.sounds.play('Hiya')
        self.set_costume('costume12')
        self.set_dirty(3)

        await self.sleep(0.1)
        self.set_costume('costume13')
        self.set_dirty(3)

        await self.sleep(1)
        await self.glide(0.1, 44, 6)
        self.set_costume('costume14')
        await self.glide(0.1, -48, -39)
        util.send_event('broadcast_Kablammie')
        self.visible = 0
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_HaHaHa(self, util):
        self.size = 100
        self.set_costume('costume3')
        self.xpos = 351
        self.ypos = 102
        self.visible = 1
        await self.glide(2, 94, 49)
        self.sounds.play('GiveItBack')
        self.set_dirty(3)

        for _ in range(6):
            await self.sleep(0.08)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(1.7)
        self.set_costume('costume10')
        self.set_dirty(3)

        await self.sleep(1)
        util.send_event('broadcast_Piff')
        await self.sleep(0.5)
        await self.glide(0.3, -352, 43)
        self.visible = 0
        self.set_dirty(2)

        await self.sleep(1)
        util.send_event('broadcast_WaitForMe')



class SpriteSprite6(engine.Target):
    costume = 16
    xpos, ypos = -44, -38
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume2",
            'path': "f6153efd16da2f4e3212a77ae5c024c9.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "89a03b2339a009a67896fff989ec69b6.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "3dcda32dc74e295783fd36ef5c9a0a92.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "7ddea87554e338d70e0f417f48803860.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "4782005bdf507de65124de895271d3e9.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "89a03b2339a009a67896fff989ec69b6.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "b758130351b57df6aee730cb6da7ba23.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "42c4fff5fd40fc01caf71741e22c82e5.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "d2e40d038b06db5672bfc04b6f4c860d.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "3bdd3c79619842e52c39956911d7a4d5.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "8dce9c7916eb2305045705c11bcacd08.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "33f08042c151bf1b0c499f87a1864dee.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "7a596eed71271c2f712636b62b6d9f4c.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "9629cf894e20a05c716b37d88af13bc9.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "b42307b901b2ecf76cae138b51c66e48.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "c09a37c64b10b053cc62ef4f383cb88a.png",
            'center': (214, 282),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "7a1606426226e76ffcfcf1014a6d1130.png",
            'center': (214, 282),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "WaitForMe",
            'path': "c7e24253ffd0987fb94795abd7bab29f.wav"
        },
        {
            'name': "ShortScream",
            'path': "ab66262ea60f9764ca61785e4ce1179f.wav"
        },
        {
            'name': "Whee",
            'path': "a210e1b5f30c11d7fd22e3665d5b93ad.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Whee': [
                self.broadcast_Whee,
            ],
            'broadcast_WaitForMe': [
                self.broadcast_WaitForMe,
                self.broadcast_WaitForMe1,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Waaah': [
                self.broadcast_Waaah,
            ],
            'broadcast_ThatGuy': [
                self.broadcast_ThatGuy,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 7

    async def broadcast_Whee(self, util):
        self.sounds.play('Whee')
        self.set_costume('costume16')
        self.set_dirty(3)

        await self.sleep(0.01)
        self.set_costume('costume17')
        self.set_dirty(3)


    async def broadcast_WaitForMe(self, util):
        self.set_costume('costume3')
        self.set_dirty(3)

        await self.sleep(1)
        self.sounds.play('WaitForMe')
        self.set_costume('costume4')
        self.set_dirty(3)

        for _ in range(8):
            await self.sleep(0.1)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(1)
        util.send_event('broadcast_Hiya')
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WaitForMe1(self, util):
        self.size = 100
        self.xpos = 280
        self.ypos = -62
        self.visible = 1
        await self.glide(4, 41, -61)
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Waaah(self, util):
        self.size = 75
        self.xpos = 259
        self.ypos = -68
        self.set_costume('costume14')
        self.sounds.play('ShortScream')
        self.visible = 1
        await self.glide(0.2, 12, -63)
        self.visible = 0
        self.set_dirty(3)

        await self.sleep(2)
        util.send_event('broadcast_Whee')
        self.set_costume('costume15')
        self.visible = 1
        await self.glide(0.3, 259, -68)
        self.visible = 0
        self.set_dirty(3)


    async def broadcast_ThatGuy(self, util):
        self.size = 100
        self.xpos = -44
        self.ypos = -38
        self.set_costume('costume20')
        self.visible = 1
        self.set_dirty(3)

        await self.sleep(3)
        self.variables['uhoh'] = 0
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite7(engine.Target):
    costume = 0
    xpos, ypos = -16, -115
    direction = -90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "81277b17aba06ae53d04625218eed612.png",
            'center': (160, 98),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "3f3ab3849e8b75fd3f668287d116372e.png",
            'center': (160, 98),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Whee': [
                self.broadcast_Whee,
            ],
            'broadcast_Hiya': [
                self.broadcast_Hiya,
            ],
            'broadcast_WaitForMe': [
                self.broadcast_WaitForMe,
                self.broadcast_WaitForMe1,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Waaah': [
                self.broadcast_Waaah,
            ],
            'broadcast_ThatGuy': [
                self.broadcast_ThatGuy,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 17

    async def broadcast_Whee(self, util):
        self.set_direction(-90)
        self.visible = 1
        await self.glide(0.3, 263, -130)
        self.visible = 0
        self.set_dirty(3)


    async def broadcast_Hiya(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WaitForMe(self, util):
        self.set_costume('costume1')
        self.set_dirty(3)

        while True:
            await self.sleep(0.01)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)



    async def broadcast_WaitForMe1(self, util):
        self.xpos = 298
        self.ypos = -145
        self.set_direction(90)
        self.size = 100
        self.visible = 1
        self.front_layer(util)
        await self.glide(4, 34, -146)
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Waaah(self, util):
        self.size = 75
        self.xpos = 263
        self.ypos = -130
        self.visible = 1
        await self.glide(0.2, 16, -130)
        self.visible = 0
        self.set_dirty(3)


    async def broadcast_ThatGuy(self, util):
        self.size = 100
        self.xpos = -16
        self.ypos = -115
        self.front_layer(util)
        self.visible = 1
        self.set_dirty(3)

        await self.sleep(3)
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite10(engine.Target):
    costume = 3
    xpos, ypos = -80, -45
    direction = -7
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "b700dc51bc8d3f96d2fc03f763a728e8.png",
            'center': (300, 254),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "636cafcc2e96ea8ff6466d993197f57b.png",
            'center': (300, 254),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "d31a0c956be1001fb1ecda2086fdf543.png",
            'center': (268, 280),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "5e4dbfec5a65ba94793e71c111bdc49e.png",
            'center': (268, 280),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "Smack-SoundBible",
            'path': "1aa54f12e5fad917218c27b2350c7134.wav"
        },
        {
            'name': "Super Punch MMA-",
            'path': "1b4f2d7df7a8784fcf3cb061df855215.wav"
        },
        {
            'name': "Thwack Hit By Pu",
            'path': "0dbd74c6e2313305704e755ef3e0fa6a.wav"
        },
        {
            'name': "Bite-SoundBible",
            'path': "da7adb29e5068dfaf92a324d0a8e5876.wav"
        },
        {
            'name': "Left Hook-SoundB",
            'path': "2f0a1580177f0e27dfec2622d23d2af7.wav"
        },
        {
            'name': "Right Cross-Soun",
            'path': "c519d13b4ef6bc893cb39b58c7843e7f.wav"
        },
        {
            'name': "Upper Cut-SoundB",
            'path': "cfe8b27afdd9d622423d55b7f46c5a46.wav"
        },
        {
            'name': "Jab-SoundBible",
            'path': "5e96c7ade80aa01b170d647df0d75614.wav"
        },
        {
            'name': "Kick-SoundBible",
            'path': "394ce2c35bbac34183121e6be6e78bcd.wav"
        },
        {
            'name': "Spin Kick-SoundB",
            'path': "19ee6e924c3b707aa3346c1345e3d670.wav"
        },
        {
            'name': "Roundhouse Kick-",
            'path': "e06661e8e62c146c286e00ddf784587d.wav"
        },
        {
            'name': "Strong_Punch-Mik",
            'path': "4d8b4639a6164cee3ffc821a9e56e7f3.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Kablammie': [
                self.broadcast_Kablammie,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 6

    async def broadcast_Kablammie(self, util):
        self.variables['uhoh'] = 1
        self.xpos = -80
        self.ypos = -45
        self.visible = 1
        self.set_dirty(2)

        for _ in range(25):
            self.sounds.play(random.randint(1, 12))
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            self.set_direction(self.direction + random.randint(-360, 360))
            self.set_dirty(3)

            await self.sleep(0.1)
            await self._yield(0)

        util.send_event('broadcast_Waaah')
        for _ in range(25):
            self.sounds.play(random.randint(1, 12))
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            self.set_direction(self.direction + random.randint(-360, 360))
            self.set_dirty(3)

            await self.sleep(0.1)
            await self._yield(0)

        util.send_event('broadcast_ThatGuy')
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite11(engine.Target):
    costume = 2
    xpos, ypos = -45, 77
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "3da21817b579bd8afd458ab761d1f524.png",
            'center': (136, 246),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "370f785b81c6d87328c31a3b44a2ae0c.png",
            'center': (136, 246),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "a7ff76a8c90598e3137355f5f67d934c.png",
            'center': (452, 272),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "FemaleScream",
            'path': "b6112cd0ba548e3f327ab8f817e4046e.wav"
        },
        {
            'name': "MegaPiff",
            'path': "1df99f700c6a9d5996059c7969d4aa2f.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_FemaleScream': [
                self.broadcast_FemaleScream,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 8

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_FemaleScream(self, util):
        self.xpos = 38
        self.ypos = 3
        self.set_costume('costume2')
        self.set_effect('ghost', 0)
        self.visible = 1
        self.sounds.play('FemaleScream')
        self.set_dirty(3)

        for _ in range(20):
            await self.sleep(0.03)
            self.ypos += 10
            self.xpos += -1
            self.set_dirty(2)

            await self.sleep(0.03)
            self.ypos += -7
            await self._yield(2)

        util.send_event('broadcast_MegaPiff')
        self.sounds.play('MegaPiff')
        self.set_costume('costume3')
        self.xpos = -45
        self.ypos = 77
        self.set_dirty(3)

        for _ in range(10):
            await self.sleep(0.06)
            self.change_effect('ghost', 10)
            await self._yield(3)

        self.visible = 0
        self.set_dirty(1)



class SpriteSprite12(engine.Target):
    costume = 1
    xpos, ypos = -107, -225
    direction = 120
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "3ca9ebd70a39c95ea669bbeab9ec1c55.png",
            'center': (96, 214),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "25999b45dac21f4190816405be74bc56.png",
            'center': (96, 214),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "Cikehs",
            'path': "c132179ce0e6bcc3eec567e4b061d186.wav"
        },
        {
            'name': "Thwack Hit By Pu",
            'path': "0dbd74c6e2313305704e755ef3e0fa6a.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_FemaleScream': [
                self.broadcast_FemaleScream,
            ],
            'broadcast_MegaPiff': [
                self.broadcast_MegaPiff,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 18

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_FemaleScream(self, util):
        self.xpos = 147
        self.ypos = 71
        self.set_costume('costume1')
        self.set_direction(90)
        self.visible = 1
        self.set_dirty(3)


    async def broadcast_MegaPiff(self, util):
        self.front_layer(util)
        await self.sleep(1.5)
        self.set_costume('costume2')
        self.set_dirty(3)

        await self.sounds.play('Cikehs')
        for _ in range(6):
            self.set_direction(self.direction - DEGREES)
            self.ypos += -14
            self.xpos += -9
            self.set_dirty(3)

            await self.sleep(0.01)
            await self._yield(0)

        util.send_event('broadcast_Lo')
        await self.sleep(0.5)
        self.sounds.play('Thwack Hit By Pu')
        for _ in range(20):
            self.xpos += -10
            self.ypos += -15
            self.set_direction(self.direction + -30)
            self.set_dirty(3)

            await self.sleep(0.01)
            await self._yield(0)

        self.visible = 0
        self.set_dirty(1)



class SpriteSprite13(engine.Target):
    costume = 0
    xpos, ypos = 240, 170
    direction = 60
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "e53fdbe3d53b1694111ca71a21419fd2.png",
            'center': (66, 36),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Yesss': [
                self.broadcast_Yesss,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_MegaPiff': [
                self.broadcast_MegaPiff,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 9

    async def broadcast_Yesss(self, util):
        await self.glide(0.9, 240, 170)
        self.visible = 0
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_MegaPiff(self, util):
        self.variables['velocity'] = 5
        self.set_direction(90)
        self.xpos = 24
        self.ypos = 91
        self.set_costume('costume1')
        self.visible = 1
        self.set_dirty(3)

        for _ in range(7):
            self.ypos += number(self.variables['Velocity'])
            self.set_direction(self.direction + 15)
            self.set_dirty(3)

            await self.sleep(0.01)
            await self._yield(0)

        for _ in range(15):
            self.variables['velocity'] += -2
            self.ypos += number(self.variables['Velocity'])
            self.set_direction(self.direction + 15)
            self.set_dirty(3)

            await self.sleep(0.01)
            await self._yield(0)




class SpriteSprite14(engine.Target):
    costume = 3
    xpos, ypos = 252, 187
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "c6665c06cb61e2e4d7a771f40f4c6a1a.png",
            'center': (220, 246),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "f00c343e2988b145fb50ee5ab1b0c84f.png",
            'center': (220, 246),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "21767caa97fbd02b242d783ba8bab7ba.png",
            'center': (220, 246),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "e848464ea146f1504b10a5d169d3db77.png",
            'center': (220, 246),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "Lo",
            'path': "656366fa1089de7dfd53d2015f49bb3b.wav"
        },
        {
            'name': "HehHehHeh",
            'path': "49376427395c10e22ab9c38df7a1d796.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Lo': [
                self.broadcast_Lo,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 19

    async def broadcast_Lo(self, util):
        self.xpos = 244
        self.ypos = 264
        self.set_costume('costume2')
        self.visible = 1
        self.front_layer(util)
        self.sounds.play('Lo')
        await self.glide(1, -173, -289)
        self.visible = 0
        self.set_dirty(3)

        await self.sleep(1)
        self.set_costume('costume4')
        self.visible = 1
        self.sounds.play('HehHehHeh')
        await self.glide(0.6, -95, -107)
        util.send_event('broadcast_Yesss')
        await self.glide(1.4, 252, 187)
        self.visible = 0
        self.set_dirty(3)

        await self.sleep(1)
        util.send_event('broadcast_OhBoy')


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite15(engine.Target):
    costume = 46
    xpos, ypos = -61, -299
    direction = 80
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "2f10e985e44a92c6e3f76e5250436f67.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "04cdb206e78bf1647040e8b4583a1e20.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "1412edf931cac05be7b98385226f79d4.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "440e4dbae9fc899699feb8f75721d2db.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "ef95dc6f1e73d2077774c9aaaa055e42.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "302b1170d5a7f494b6dccf05d624328f.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "77dde23f4efe2d926e5724c8b6c8bd24.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "302b1170d5a7f494b6dccf05d624328f.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "ef95dc6f1e73d2077774c9aaaa055e42.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "440e4dbae9fc899699feb8f75721d2db.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "a5c3760bc95ab6a6e78e5aca507c3511.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "59e8280ddb213cafe440744224f712b9.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "04cdb206e78bf1647040e8b4583a1e20.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "ab0b8bdc6c9cc62e1267ef285dc022a4.png",
            'center': (408, 344),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "6bbaf29a08fe60d38d7494aa260203c6.png",
            'center': (408, 344),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "ddd5afe01edc517c9e586b300a99d617.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "b6b205603b8667e7673dd2022d750a9e.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "4a57484d7c01859015fbe7424e57d3dc.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "370f57262ae0c6e96b44b3197e9ee840.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "c077abf04506980c2adf28354a16a291.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "5efd46fe55f0ddc8ae296bcc141a15d7.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "a5e9e1bc4ee2c4b13230de9352109284.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "df5e0c67484fd910d1d6568954bc764a.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "5a06d1e209eedea6277b65c9894ad4d6.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "df5e0c67484fd910d1d6568954bc764a.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "bebe5881b39383e94ec3c7cdb334b046.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "5efd46fe55f0ddc8ae296bcc141a15d7.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "bebe5881b39383e94ec3c7cdb334b046.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume29",
            'path': "72b5c3f8ce4910ae414da29a67954215.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume30",
            'path': "5a06d1e209eedea6277b65c9894ad4d6.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume31",
            'path': "5efd46fe55f0ddc8ae296bcc141a15d7.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume32",
            'path': "72b5c3f8ce4910ae414da29a67954215.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume33",
            'path': "df5e0c67484fd910d1d6568954bc764a.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume34",
            'path': "5efd46fe55f0ddc8ae296bcc141a15d7.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume35",
            'path': "72b5c3f8ce4910ae414da29a67954215.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume36",
            'path': "b254550271783ed9f8605938a373d206.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume37",
            'path': "fdc3deedf4cf3f25ada986085bfe105f.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume38",
            'path': "29fad1fcdeb3aa0f6cd0ddbbc27d1d3f.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume39",
            'path': "acf96de19086a3d02f3bd09c4a757747.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume40",
            'path': "622d4c7971da097a968363c7865a9dad.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume41",
            'path': "d90b7d023cd367efb78540be18c392b1.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume42",
            'path': "4481b099ac1a8beb4b4f90510b80766a.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume43",
            'path': "6ffb3b08145ff02668337413274ded03.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume46",
            'path': "6ffb3b08145ff02668337413274ded03.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume44",
            'path': "d8bf4a673a2d40ffc55ede88407fb1e6.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume45",
            'path': "d90b7d023cd367efb78540be18c392b1.png",
            'center': (408, 304),
            'scale': 2
        },
        {
            'name': "costume47",
            'path': "76853a6c22b19e44d6c845555e1b7871.png",
            'center': (408, 304),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "OhBoy",
            'path': "7ada0852c96957ffebf41f92c09e8282.wav"
        },
        {
            'name': "SuddenDefeatClip",
            'path': "22ea2700c0059d4b518f6e7aa9fd99ba.wav"
        },
        {
            'name': "Chomp",
            'path': "ca6526c0b3ae71c2b24c214742afcddd.wav"
        },
        {
            'name': "Crunch",
            'path': "ebb8fc04a1dc7c98d20266f5b641a157.wav"
        },
        {
            'name': "Mmmm",
            'path': "751a83c65e31dab7ab10eaa85ee4a22b.wav"
        },
        {
            'name': "TheDeliciousFlavorOf",
            'path': "b111d132a1cebaa0cb5ccf9df703d99e.wav"
        },
        {
            'name': "Ohhh",
            'path': "dafe8a7ec217dd0667651d1927fcab5f.wav"
        },
        {
            'name': "Cardboard",
            'path': "dfbc8b77b474a37501f065d55a5d092a.wav"
        },
        {
            'name': "Thump",
            'path': "829b6d3efba6b99d48ebb84714955fdb.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_OhBoy': [
                self.broadcast_OhBoy,
            ],
            'broadcast_Faint': [
                self.broadcast_Faint,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 20

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_OhBoy(self, util):
        self.set_direction(90)
        self.set_costume('costume2')
        self.xpos = -50
        self.ypos = -27
        self.size = 92
        self.front_layer(util)
        self.change_layer(util, -1)
        self.visible = 1
        self.set_dirty(3)

        await self.sleep(1)
        self.sounds.play('OhBoy')
        self.set_costume('costume3')
        self.set_dirty(3)

        for _ in range(10):
            await self.sleep(0.08)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(1)
        util.send_event('broadcast_HesGonnaEatIt')
        self.sounds.stop_all(util)
        self.sounds.play('SuddenDefeatClip')
        self.xpos = -50
        self.ypos = -42
        self.set_costume('costume14')
        await self.glide(10, -47, -15)
        self.sounds.stop_all(util)
        util.send_event('broadcast_Chomp')
        self.sounds.play('Chomp')
        self.set_costume('costume15')
        self.set_dirty(3)

        await self.sleep(0.08)
        self.set_costume('costume16')
        self.set_dirty(3)

        await self.sleep(0.08)
        self.set_costume('costume17')
        self.set_dirty(3)

        await self.sleep(1)
        self.sounds.play('Crunch')
        for _ in range(4):
            self.set_costume('costume18')
            self.set_dirty(3)

            await self.sleep(0.1)
            self.set_costume('costume17')
            self.set_dirty(3)

            await self.sleep(0.15)
            await self._yield(0)

        await self.sleep(1)
        self.xpos = -50
        self.ypos = -24
        self.set_dirty(2)

        await self.sounds.play('Mmmm')
        await self.sleep(1)
        self.sounds.play('TheDeliciousFlavorOf')
        self.set_costume('costume20')
        self.set_dirty(3)

        for _ in range(15):
            await self.sleep(0.07)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(1)
        self.sounds.play('Ohhh')
        self.set_costume('costume37')
        self.set_direction(90)
        self.set_dirty(3)

        for _ in range(10):
            await self.sleep(0.01)
            self.set_direction(self.direction - DEGREES)
            self.xpos += -1
            await self._yield(3)

        self.sounds.play('Cardboard')
        self.set_costume('costume38')
        self.set_dirty(3)

        for _ in range(8):
            await self.sleep(0.1)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(1)
        util.send_event('broadcast_ItsCardboard')


    async def broadcast_Faint(self, util):
        self.set_costume('costume47')
        self.set_dirty(3)

        await self.sleep(1)
        await self.glide(0.1, -61, -299)
        self.sounds.play('Thump')
        self.visible = 0
        self.set_dirty(2)

        await self.sleep(1)
        util.send_event('broadcast_Ahhhhh')



class SpriteSprite16(engine.Target):
    costume = 0
    xpos, ypos = 34, -254
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "bbf76ca2a52d746d979b1ffb3fe63ee7.png",
            'center': (366, 198),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_HesGonnaEatIt': [
                self.broadcast_HesGonnaEatIt,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_OhBoy': [
                self.broadcast_OhBoy,
            ],
            'broadcast_Faint': [
                self.broadcast_Faint,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 2

    async def broadcast_HesGonnaEatIt(self, util):
        await self.glide(10, 33, -77)
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_OhBoy(self, util):
        self.xpos = 78
        self.ypos = -95
        self.size = 92
        self.set_costume('costume1')
        self.change_layer(util, -99)
        self.visible = 1
        self.set_dirty(3)


    async def broadcast_Faint(self, util):
        await self.sleep(1)
        await self.glide(0.08, 34, -262)
        self.visible = 0
        self.set_dirty(2)



class SpriteSprite17(engine.Target):
    costume = 3
    xpos, ypos = 52, -234
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "e797f9606a2ab6933e628da832374959.png",
            'center': (298, 202),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "8d0ae533a461082a8ce2822f1dbff7d3.png",
            'center': (298, 206),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "6415753103f93c87e51b854bde5e9ef6.png",
            'center': (134, 206),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "3627566dcf66954f2b324ee8abb6f684.png",
            'center': (134, 206),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "ItsCardboard",
            'path': "20d89f7bbab1312691403f2605f875cd.wav"
        },
        {
            'name': "Ding",
            'path': "3937aaea6f511827f374e85e6d2912f6.wav"
        },
        {
            'name': "DingDingDing",
            'path': "222e0c767669318766492053bd34dee7.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_ItsCardboard': [
                self.broadcast_ItsCardboard,
            ],
            'broadcast_HesGonnaEatIt': [
                self.broadcast_HesGonnaEatIt,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_OhBoy': [
                self.broadcast_OhBoy,
            ],
            'broadcast_Chomp': [
                self.broadcast_Chomp,
            ],
            'broadcast_Faint': [
                self.broadcast_Faint,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 21

    async def broadcast_ItsCardboard(self, util):
        self.sounds.play('Ding')
        self.set_costume('costume4')
        self.set_dirty(3)

        await self.sleep(1)
        await self.sounds.play('ItsCardboard')
        await self.sleep(1)
        util.send_event('broadcast_Faint')


    async def broadcast_HesGonnaEatIt(self, util):
        await self.glide(10, 62, -13)
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_OhBoy(self, util):
        self.xpos = 114
        self.ypos = 5
        self.size = 77
        self.set_costume('costume2')
        self.front_layer(util)
        self.visible = 1
        self.set_dirty(3)


    async def broadcast_Chomp(self, util):
        self.set_costume('costume3')
        self.set_dirty(3)


    async def broadcast_Faint(self, util):
        await self.sleep(1)
        await self.glide(0.07, 52, -234)
        self.visible = 0
        self.set_dirty(2)



class SpriteSprite18(engine.Target):
    costume = 1
    xpos, ypos = -249, -46
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "8d6f73936946413e6ec09b0868832cd1.png",
            'center': (52, 68),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "ffda3776616f48741c9c101be3cf3214.png",
            'center': (52, 68),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "91021eeb37a50f3cf3962298ff1ecd8d.png",
            'center': (52, 68),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "Ahhhhh",
            'path': "c229c65484dee3055e15dfe41c29fc84.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Ahhhhh': [
                self.broadcast_Ahhhhh,
                self.broadcast_Ahhhhh1,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 10

    async def broadcast_Ahhhhh(self, util):
        for _ in range(40):
            await self.sleep(0.05)
            self.set_costume('costume3')
            self.set_dirty(3)

            await self.sleep(0.05)
            self.set_costume('costume2')
            await self._yield(3)



    async def broadcast_Ahhhhh1(self, util):
        self.xpos = 260
        self.ypos = -46
        self.visible = 1
        self.sounds.play('Ahhhhh')
        await self.glide(4, -260, -46)
        self.visible = 0
        self.set_dirty(2)

        await self.sleep(1)
        util.send_event('broadcast_IsHeDead')


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite19(engine.Target):
    costume = 15
    xpos, ypos = -230, -0.36693877551016385
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "c348f55de3cb3c88b189009eb2a868e1.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "6b3f376e12392696ec366a6af65c197c.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "3e02c4732e3669f0e43b8fabb0a2b0dd.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "10e14147b00ff49ecc2301a62a091c48.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "fc8f85054236d070e73334c2171f4413.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "dfffb9319d5ec8dfd1eb98e26f678987.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "172360902c89e2495800c0eb48250667.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "7ab89df92709cc2d5ed0fef1f50fba53.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "4b33702f1e1823c8845917d9841c9f4b.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "6c9be909781151b03a94b2f182f59a40.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "4b33702f1e1823c8845917d9841c9f4b.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "7ab89df92709cc2d5ed0fef1f50fba53.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "fc8f85054236d070e73334c2171f4413.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "fc8f85054236d070e73334c2171f4413.png",
            'center': (202, 280),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "d25a0a6c9c75fafc5cbf0acd3f4558e3.png",
            'center': (202, 332),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "0fa12252076c82aee646397baa9e5dd3.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "0fa12252076c82aee646397baa9e5dd3.png",
            'center': (202, 274),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "e72101071231b54732cdfdde8721876d.png",
            'center': (368, 328),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "6b3f376e12392696ec366a6af65c197c.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "3a4530ddc0392b9a8b5b6b1087276f45.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "4b33702f1e1823c8845917d9841c9f4b.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "c57446a1913e062a157d97ad3549f035.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "6c9be909781151b03a94b2f182f59a40.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "dfffb9319d5ec8dfd1eb98e26f678987.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "fc8f85054236d070e73334c2171f4413.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "4b33702f1e1823c8845917d9841c9f4b.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "10e14147b00ff49ecc2301a62a091c48.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume29",
            'path': "fc8f85054236d070e73334c2171f4413.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume30",
            'path': "dfffb9319d5ec8dfd1eb98e26f678987.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume31",
            'path': "10e14147b00ff49ecc2301a62a091c48.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume32",
            'path': "3a4530ddc0392b9a8b5b6b1087276f45.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume33",
            'path': "e822269adf812f55b57f061a62c25d6b.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume34",
            'path': "4b33702f1e1823c8845917d9841c9f4b.png",
            'center': (202, 306),
            'scale': 2
        },
        {
            'name': "costume35",
            'path': "dfffb9319d5ec8dfd1eb98e26f678987.png",
            'center': (202, 306),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "IsHeDead",
            'path': "99b00f4f05148566a0778f2606f6aa21.wav"
        },
        {
            'name': "whoosh",
            'path': "6394551b397c5a9669d02786b4d8e91d.wav"
        },
        {
            'name': "YoureJustGoingToLeaveHim",
            'path': "43449f2826a3eb96446ef9825ac59717.wav"
        },
        {
            'name': "IGuessHesOk",
            'path': "7e1dcfde31da239316fe09f01d7ba3f1.wav"
        },
        {
            'name': "IsHeDead1",
            'path': "747a1334777118e0f51354a439d4e11e.wav"
        },
        {
            'name': "YoureJustGoingTo1",
            'path': "91eae9fbf04452b573e07e93a8bf5533.wav"
        },
        {
            'name': "IGuessHesOk1",
            'path': "d4cb3289c3162a5023cda71564cd265f.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_MoreEffects': [
                self.broadcast_MoreEffects,
            ],
            'broadcast_Drrr': [
                self.broadcast_Drrr,
            ],
            'broadcast_IsHeDead': [
                self.broadcast_IsHeDead,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_WheresMyTaco': [
                self.broadcast_WheresMyTaco,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 24

    async def broadcast_MoreEffects(self, util):
        for _ in range(5):
            await self.sleep(0.03)
            self.change_effect('pixelate', -10)
            self.size += -2
            self.xpos += 2
            await self._yield(3)

        await self.sleep(1)
        self.sounds.play('whoosh')
        self.set_costume('costume16')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume15')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume17')
        self.set_dirty(3)

        await self.sleep(1)
        await self.sounds.play('YoureJustGoingTo1')
        await self.sleep(1)
        self.sounds.play('whoosh')
        self.set_costume('costume18')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume20')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume19')
        self.set_dirty(3)

        await self.sleep(1)
        self.set_costume('costume19')
        self.sounds.play('IGuessHesOk1')
        self.set_dirty(3)

        for _ in range(15):
            await self.sleep(0.07)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(1)
        self.sounds.play('whoosh')
        self.set_costume('costume16')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume15')
        self.set_dirty(3)

        await self.sleep(0.03)
        self.set_costume('costume17')
        self.set_dirty(3)

        await self.sleep(1)
        for _ in range(3):
            for _ in range(4):
                await self.sleep(0.01)
                self.xpos += -10
                self.ypos += (number(round(self.size)) / -50)
                self.size += (number(round(self.size)) * -0.01)
                await self._yield(3)

            for _ in range(4):
                await self.sleep(0.01)
                self.xpos += -10
                self.ypos += (number(round(self.size)) / 49)
                self.size += (number(round(self.size)) * -0.01)
                await self._yield(3)

            await self._yield(0)

        self.visible = 0
        self.set_dirty(1)

        await self.sleep(1)
        util.send_event('broadcast_Questions')


    async def broadcast_Drrr(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_IsHeDead(self, util):
        self.set_effect('pixelate', 0)
        self.xpos = -301
        self.ypos = -102
        self.size = 79
        self.set_costume('costume2')
        self.visible = 1
        self.set_dirty(3)

        for _ in range(5):
            for _ in range(4):
                await self.sleep(0.01)
                self.xpos += 5
                self.ypos += (number(round(self.size)) / 25)
                self.size += (number(round(self.size)) * 0.01)
                await self._yield(3)

            for _ in range(4):
                await self.sleep(0.01)
                self.xpos += 5
                self.ypos += (number(round(self.size)) / -98)
                self.size += (number(round(self.size)) * 0.01)
                await self._yield(3)

            await self._yield(0)

        await self.sleep(1)
        self.set_costume('costume2')
        self.sounds.play('IsHeDead1')
        self.set_dirty(3)

        for _ in range(10):
            await self.sleep(0.07)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(0.2)
        next_costume = self.costume['number'] + 1
        if next_costume == len(self.costumes):
            self.set_costume(0)
        else:
            self.set_costume(next_costume)
        self.set_dirty(3)

        await self.sleep(1)
        util.send_event('broadcast_AwesomeEffects')
        for _ in range(5):
            await self.sleep(0.03)
            self.change_effect('pixelate', 10)
            self.size += 2
            self.xpos += -2
            await self._yield(3)



    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WheresMyTaco(self, util):
        self.visible = 1
        self.set_dirty(1)



class SpriteSprite20(engine.Target):
    costume = 28
    xpos, ypos = -317, -58.9893877551018
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "e000b94a092717cbc54313658741363b.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "9da36a030c5819f1a6c993da3e58d8c5.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "11a16c185008c1cce553ce2ffce4acef.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "5b84a8f195f4d5f9811a67b3e048c2d0.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "e6d5d13f8d3f5fb020953971449eb3cb.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "6d20ad96697e8cf1142f065cc5184ab0.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "755ec95f522a799375e9dee165af1b97.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "870ed6a5039cf2c15cf794f66e74c07c.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "7012965c8aecba7b3087bbd32450efb0.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "9da36a030c5819f1a6c993da3e58d8c5.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "babf367bdc5c802d79d74f30015c9214.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "47ad3b821abcd6f5e3a1fd447e386af9.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "97a96797d654c42d36ab05533908135b.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "9514b6986540821eedf54aec44113707.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "be7f90786217606d9eca0c46a0b0aa6c.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "47ad3b821abcd6f5e3a1fd447e386af9.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "dfb20e7550b2af4cb7dfb5cc514d46a2.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "e29321939fb6423bc97dd663aced7d53.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "be7f90786217606d9eca0c46a0b0aa6c.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "75698502c904cce94f073a0467ccfc2f.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "97a96797d654c42d36ab05533908135b.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "9514b6986540821eedf54aec44113707.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "591e968f626ca0acdb08c9e6ed2927b0.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "dfb20e7550b2af4cb7dfb5cc514d46a2.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "be7f90786217606d9eca0c46a0b0aa6c.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "47ad3b821abcd6f5e3a1fd447e386af9.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "9fe48b2d4f4c25cf3cd6323219334b2e.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "be7f90786217606d9eca0c46a0b0aa6c.png",
            'center': (184, 334),
            'scale': 2
        },
        {
            'name': "costume29",
            'path': "0a54aafcd3e9c79035be3d88982b8919.png",
            'center': (288, 276),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "IDunno",
            'path': "5931783daf8e2cd8aeea2bb3f56d454a.wav"
        },
        {
            'name': "Wait",
            'path': "00a987ccd031bb088785881082e80dbe.wav"
        },
        {
            'name': "WheresMyTaco",
            'path': "571397abc1ee5963a9869fe942052a16.wav"
        },
        {
            'name': "Dash",
            'path': "c9a9e79183c87b3c86cd665a1cc84632.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_WheresMyTaco': [
                self.broadcast_WheresMyTaco,
            ],
            'broadcast_AwesomeEffects': [
                self.broadcast_AwesomeEffects,
            ],
            'broadcast_Drrr': [
                self.broadcast_Drrr,
            ],
            'broadcast_IsHeDead': [
                self.broadcast_IsHeDead,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 1

    async def broadcast_WheresMyTaco(self, util):
        self.set_costume('costume10')
        self.visible = 1
        self.set_dirty(3)

        await self.sleep(1)
        self.sounds.play('Wait')
        self.set_costume('costume12')
        self.set_dirty(3)

        for _ in range(3):
            await self.sleep(0.06)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(0.5)
        self.sounds.play('WheresMyTaco')
        for _ in range(13):
            await self.sleep(0.06)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(2)
        self.set_costume('costume29')
        self.sounds.play('Dash')
        await self.glide(0.2, -317, -59)
        self.visible = 0
        util.send_event('broadcast_MoreEffects')
        self.set_dirty(3)


    async def broadcast_AwesomeEffects(self, util):
        for _ in range(5):
            await self.sleep(0.03)
            self.change_effect('pixelate', -10)
            self.size += 1
            self.xpos += 1
            await self._yield(3)

        self.set_costume('costume2')
        self.sounds.play('IDunno')
        self.set_dirty(3)

        for _ in range(8):
            await self.sleep(0.08)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        await self.sleep(0.8)
        util.send_event('broadcast_Drrr')


    async def broadcast_Drrr(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_IsHeDead(self, util):
        self.change_layer(util, -99)
        self.set_effect('pixelate', 50)
        self.xpos = 301
        self.ypos = -102
        self.size = 68
        self.set_costume('costume2')
        self.set_dirty(3)

        await self.sleep(1)
        self.visible = 1
        self.set_dirty(1)

        for _ in range(5):
            for _ in range(4):
                await self.sleep(0.01)
                self.xpos += -5
                self.ypos += (number(round(self.size)) / 25)
                self.size += (number(round(self.size)) * 0.005)
                await self._yield(3)

            for _ in range(4):
                await self.sleep(0.01)
                self.xpos += -5
                self.ypos += (number(round(self.size)) / -98)
                self.size += (number(round(self.size)) * 0.005)
                await self._yield(3)

            await self._yield(0)



    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite21(engine.Target):
    costume = 0
    xpos, ypos = 67, 29
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "0869900f04bde58ec084a3ce967574da.png",
            'center': (444, 258),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "IDontRecall",
            'path': "8e71396b73a15a5d1d2fafdff666f8ee.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Drrr': [
                self.broadcast_Drrr,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 11

    async def broadcast_Drrr(self, util):
        self.xpos = 67
        self.ypos = 29
        self.visible = 1
        self.set_dirty(2)

        await self.sleep(1)
        await self.sounds.play('IDontRecall')
        await self.sleep(1)
        util.send_event('broadcast_WheresMyTaco')
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite23(engine.Target):
    costume = 0
    xpos, ypos = 0, 0
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "6b2b987e49f541f3b13c6555fe1f5785.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "fee1b64d16e2348e2a9ffc738e36dcf8.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "5d206d3996259ac4b27299f0e25b0b02.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "c74760255a9f2f9a167880546d0b2b85.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "01225cfe28d955a65429f831616947b4.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "c62e74c2bde39f91d62e765cd197b92a.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "f1b7a1a267c36b207b06b72e12f71e90.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "Smash",
            'path': "640ff9c2d0ae74d69355ec709ddc5da0.wav"
        },
        {
            'name': "SmokingGun",
            'path': "1ed0d095cfc049b10695bf40dd2b3c52.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Questions': [
                self.broadcast_Questions,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 12

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Questions(self, util):
        self.xpos = 0
        self.ypos = 347
        self.variables['velocity'] = 0
        self.set_costume('costume1')
        self.set_effect('brightness', -100)
        self.visible = 1
        self.set_dirty(3)

        for _ in range(17):
            self.variables['velocity'] += -2
            self.ypos += number(self.variables['Velocity'])
            self.set_dirty(2)

            await self.sleep(0.01)
            await self._yield(0)

        self.sounds.play('Smash')
        self.xpos = 0
        self.ypos = 0
        self.set_dirty(2)

        await self.sleep(2)
        self.sounds.play('SmokingGun')
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', 10)
            await self._yield(3)

        for _ in range(5):
            await self.sleep(3)
            for _ in range(10):
                await self.sleep(0.01)
                self.change_effect('brightness', -10)
                await self._yield(3)

            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            self.set_dirty(3)

            for _ in range(10):
                await self.sleep(0.01)
                self.change_effect('brightness', 10)
                await self._yield(3)

            await self._yield(0)

        await self.sleep(4)
        for _ in range(20):
            await self.sleep(0.01)
            self.change_effect('brightness', -5)
            await self._yield(3)

        util.send_event('broadcast_Credits')
        next_costume = self.costume['number'] + 1
        if next_costume == len(self.costumes):
            self.set_costume(0)
        else:
            self.set_costume(next_costume)
        self.set_dirty(3)

        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', 10)
            await self._yield(3)




class SpriteSprite24(engine.Target):
    costume = 0
    xpos, ypos = 0, 200
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "59549d5cb71ead543b374528f8708310.png",
            'center': (330, 74),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "9c349d68fa7051971db9ec1622b72b93.png",
            'center': (484, 342),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "f0bcc502c31c532dd4671971a1a4850b.png",
            'center': (484, 342),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "e2fbd0fa48ee6c619aeac32066836bd2.png",
            'center': (530, 342),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "76c98a76d8c3c7b94fc6b0e6be7329f8.png",
            'center': (476, 364),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "1b5bf8f93574db8015c34546548b6a55.png",
            'center': (530, 342),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "682ab633b2e78eb01afab91fd998e8de.png",
            'center': (260, 58),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Credits': [
                self.broadcast_Credits,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 22

    async def broadcast_Credits(self, util):
        self.set_costume('costume1')
        self.xpos = 0
        self.ypos = -180
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)

        for _ in range(7):
            self.xpos = 0
            self.ypos = -200
            await self.glide(3, 0, 200)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)

        self.visible = 0
        util.send_event('broadcast_DaveRoll')
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class SpriteSprite25(engine.Target):
    costume = 13
    xpos, ypos = -4, -10
    direction = 90
    visible = False

    costumes = [
        {
            'name': "Rickroll'd1",
            'path': "80019763e45d78abf930b071ed7ab6e6.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd3",
            'path': "1b243ed9516c0256b82e742b4bb37f66.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd5",
            'path': "e0f76fb69e18ee3ffaec2e16a4eb5de6.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd7",
            'path': "2cb3fe532d876cfe94ce8ebe54e89726.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd9",
            'path': "9b24327f56abb13f10f39f0354088d61.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd11",
            'path': "0938c5d8ddbe2bc82a131d932a2b4394.png",
            'center': (314, 268),
            'scale': 2
        },
        {
            'name': "Rickroll'd13",
            'path': "ac9ea91aeac66ccc11ee4f6db884186d.png",
            'center': (322, 262),
            'scale': 2
        },
        {
            'name': "Rickroll'd15",
            'path': "57df658e599b567d0f5bdcf482941c18.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd17",
            'path': "9406957ee74bf6767c3435ad5401c7c0.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd19",
            'path': "2b656d5286b948f1cdaafa5b5d3fcd16.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd21",
            'path': "b87877741ae3a64d15de2f2ad1a0dd59.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd23",
            'path': "b01a4ae484eb63fb5b1e7b11200741b2.png",
            'center': (306, 254),
            'scale': 2
        },
        {
            'name': "Rickroll'd25",
            'path': "d479c1f353ccf7d10c934d7e0c83c563.png",
            'center': (268, 246),
            'scale': 2
        },
        {
            'name': "Rickroll'd27",
            'path': "4a3d67f9d7589bda5f2d5bfd7a97c734.png",
            'center': (306, 254),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "RickRollClip",
            'path': "bb14ffe161a9a888d80acca088aee328.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_DaveRoll': [
                self.broadcast_DaveRoll,
                self.broadcast_DaveRoll1,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 13

    async def broadcast_DaveRoll(self, util):
        self.sounds.stop_all(util)
        while True:
            await self.sounds.play('RickRollClip')
            await self._yield(0)



    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_DaveRoll1(self, util):
        self.set_costume('Rickroll\'d1')
        self.visible = 1
        self.set_dirty(3)

        while True:
            await self.sleep(0.15)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)




class SpriteSprite22(engine.Target):
    costume = 0
    xpos, ypos = 0, 0
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "527289c91356adf6d928ec9f3c83541e.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite._layer = 23

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)

SPRITES = {
    'SpriteSprite5': SpriteSprite5,
    'SpriteSprite18': SpriteSprite18,
    'SpriteSprite21': SpriteSprite21,
    'SpriteSprite19': SpriteSprite19,
    'SpriteSprite24': SpriteSprite24,
    'SpriteSprite4': SpriteSprite4,
    'SpriteSprite14': SpriteSprite14,
    'SpriteSprite23': SpriteSprite23,
    'SpriteSprite16': SpriteSprite16,
    'SpriteSprite22': SpriteSprite22,
    'SpriteSprite13': SpriteSprite13,
    'Sprite_play': Sprite_play,
    'SpriteSprite2': SpriteSprite2,
    'SpriteSprite11': SpriteSprite11,
    'SpriteSprite6': SpriteSprite6,
    'SpriteSprite12': SpriteSprite12,
    'SpriteSprite1': SpriteSprite1,
    'SpriteSprite3': SpriteSprite3,
    'Sprite_title': Sprite_title,
    'SpriteSprite15': SpriteSprite15,
    'SpriteSprite10': SpriteSprite10,
    'SpriteSprite17': SpriteSprite17,
    'SpriteStage': SpriteStage,
    'SpriteSprite20': SpriteSprite20,
    'SpriteSprite7': SpriteSprite7,
    'SpriteSprite25': SpriteSprite25,
}

if __name__ == '__main__':
    engine.main(SPRITES)
