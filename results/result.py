"""
Generated with sb3topy
"""
import asyncio
import math
import random
import time

import engine

class Stage(engine.Target):
    costume = 0
    xpos, ypos = 0, 0
    direction = 90
    visible = True

    costumes = [
        {
            'name': "background1",
            'path': "a9bdb6e689dcd1dbddb29e477369f4fe.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background2",
            'path': "3103857d11c5c7b4ccdd29f0e15caf2c.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background3",
            'path': "b46d1394b6390795a596d7158e182a3a.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background6",
            'path': "dfd9852750f9348b0b856ec1166acdd7.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background4",
            'path': "a14d0ac914b8571b8e0d6e7ca0637ba6.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background5",
            'path': "8e69cd3670561737c5975467a396f9fb.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background7",
            'path': "5e5ba93008e6b8c54981a377ae47144f.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background8",
            'path': "1118769c1e5133f8da8ce82a979bcd7d.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background9",
            'path': "843fd2b329d9c52abab17260e2bf5110.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background10",
            'path': "b20cd7c9e738b20575684238c08f5ab1.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background11",
            'path': "b647096d3aa89de0914385d406292500.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background12",
            'path': "2214ebfba188303ff2c6172b1569e0a5.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background13",
            'path': "3fac25252f477bc111bc19c8e65e9e06.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background14",
            'path': "95dd092a0fc4032bfa202715db043715.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background15",
            'path': "5ad86dce54c0950fb2392207e4e8b4ad.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background16",
            'path': "797b03bdb8cf6ccfc30c0692d533d998.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "background17",
            'path': "13acf40fcbcd9463222708eed62bebf8.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "NewSMBClip",
            'path': "06727c62d7ecf79f1db865e2f2e8f8cb.wav"
        },
        {
            'name': "WitchDoctorClip",
            'path': "8b97a61ea2607280f63a6ed427d63d45.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Flash': [
                self.broadcast_Flash,
            ],
            'broadcast_HeyGuys': [
                self.broadcast_HeyGuys,
            ],
            'broadcast_SlowDownFolks': [
                self.broadcast_SlowDownFolks,
            ],
            'broadcast_Credits': [
                self.broadcast_Credits,
            ],
            'broadcast_ThirdTimeAwkward': [
                self.broadcast_ThirdTimeAwkward,
            ],
            'broadcast_IsThereATrend': [
                self.broadcast_IsThereATrend,
            ],
            'broadcast_ILoveTacos': [
                self.broadcast_ILoveTacos,
            ],
            'broadcast_EvenMoreAwkward': [
                self.broadcast_EvenMoreAwkward,
                self.broadcast_EvenMoreAwkward_1,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'broadcast_Awkward': [
                self.broadcast_Awkward,
            ],
            'broadcast_NowHesAngry': [
                self.broadcast_NowHesAngry,
            ],
            'broadcast_WhatThe': [
                self.broadcast_WhatThe,
            ],
            'broadcast_SoIMustEatTacos': [
                self.broadcast_SoIMustEatTacos,
            ],
            'broadcast_WhereIsIt': [
                self.broadcast_WhereIsIt,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_WitchDoctor': [
                self.broadcast_WitchDoctor,
                self.broadcast_WitchDoctor_1,
            ],
            'broadcast_Lightning': [
                self.broadcast_Lightning,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 0

    async def broadcast_Flash(self, util):
        if not (self.costume['number'] == "15"):
            self.set_effect('brightness', -10)
            self.set_dirty(3)
            await self.sleep(0.01)
            self.set_effect('brightness', -20)
            self.set_dirty(3)
            await self.sleep(0.1)
            self.set_effect('brightness', -10)
            self.set_dirty(3)
            await self.sleep(0.3)
            for _ in range(10):
                await self.sleep(0.01)
                self.change_effect('brightness', -1)
                await self._yield(3)


    async def broadcast_HeyGuys(self, util):
        self.set_effect('brightness', 0)
        util.stage.costume = util.stage.get_costume('background15')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_SlowDownFolks(self, util):
        self.set_effect('brightness', -20)
        util.stage.costume = util.stage.get_costume('background11')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)
        for _ in range(10):
            util.stage.costume = util.stage.get_costume('background11')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.01)
            util.stage.costume = util.stage.get_costume('background12')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.01)
            await self._yield(0)
        for _ in range(10):
            util.stage.costume = util.stage.get_costume('background11')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.05)
            util.stage.costume = util.stage.get_costume('background12')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.05)
            await self._yield(0)
        util.send_event('broadcast_Flash')
        for _ in range(7):
            util.stage.costume = util.stage.get_costume('background11')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.1)
            util.stage.costume = util.stage.get_costume('background12')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.1)
            await self._yield(0)
        for _ in range(4):
            util.stage.costume = util.stage.get_costume('background11')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.2)
            util.stage.costume = util.stage.get_costume('background12')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.2)
            await self._yield(0)
        for _ in range(2):
            util.stage.costume = util.stage.get_costume('background11')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.5)
            util.stage.costume = util.stage.get_costume('background12')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.5)
            await self._yield(0)
        util.send_event('broadcast_Flash')


    async def broadcast_Credits(self, util):
        util.stage.costume = util.stage.get_costume('background16')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_ThirdTimeAwkward(self, util):
        util.stage.costume = util.stage.get_costume('background1')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_IsThereATrend(self, util):
        util.stage.costume = util.stage.get_costume('background1')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_ILoveTacos(self, util):
        util.stage.costume = util.stage.get_costume('background2')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_EvenMoreAwkward(self, util):
        util.stage.costume = util.stage.get_costume('background1')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_Play(self, util):
        util.stage.costume = util.stage.get_costume('background1')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)
        await self.sleep(3.5)
        pass # sound_setvolumeto(33)
        pass # sound_play('NewSMBClip')


    async def broadcast_Awkward(self, util):
        util.stage.costume = util.stage.get_costume('background2')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_NowHesAngry(self, util):
        self.variables['UhOh'] = "0"
        while not (self.variables['UhOh'] == "1"):
            util.stage.costume = util.stage.get_costume('background3')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            util.stage.costume = util.stage.get_costume('background6')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            util.stage.costume = util.stage.get_costume('background4')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            util.stage.costume = util.stage.get_costume('background5')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            await self._yield(0)
        while not (self.variables['UhOh'] == "0"):
            util.stage.costume = util.stage.get_costume('background7')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            util.stage.costume = util.stage.get_costume('background8')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            util.stage.costume = util.stage.get_costume('background9')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            util.stage.costume = util.stage.get_costume('background10')
            util.send_event('onbackdrop_' + self.costume['name'])
            self.set_dirty(3)
            await self.sleep(0.07)
            await self._yield(0)
        util.stage.costume = util.stage.get_costume('background14')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_WhatThe(self, util):
        util.stage.costume = util.stage.get_costume('background13')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)
        await self.sleep(1)
        util.send_event('broadcast_Flash')


    async def broadcast_SoIMustEatTacos(self, util):
        util.stage.costume = util.stage.get_costume('background2')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_EvenMoreAwkward_1(self, util):
        util.stage.costume = util.stage.get_costume('background1')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)


    async def broadcast_WhereIsIt(self, util):
        util.stage.costume = util.stage.get_costume('background12')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)
        await self.sleep(1)
        util.send_event('broadcast_Flash')


    async def green_flag(self, util):
        self.variables['Dark'] = "0"
        self.clear_effects()
        self.set_dirty(3)


    async def broadcast_WitchDoctor(self, util):
        util.stage.costume = util.stage.get_costume('background17')
        util.send_event('onbackdrop_' + self.costume['name'])
        self.set_dirty(3)
        while True:
            await self.sleep(0.1)
            self.change_effect('color', 10)
            await self._yield(3)


    async def broadcast_WitchDoctor_1(self, util):
        while True:
            pass # sound_playuntildone('WitchDoctorClip')
            await self._yield(0)


    async def broadcast_Lightning(self, util):
        self.set_effect('brightness', 50)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', 0)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', 30)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(30):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)



class title(engine.Target):
    costume = 2
    xpos, ypos = 0, 0
    direction = 90
    visible = True

    costumes = [
        {
            'name': "costume1",
            'path': "2ef224532430544b62a7725a592e4ab8.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "6198baa69c42985d5eeaa4930706111f.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "c9061b829c9fa2edf23b52b3030411ab.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "TheBeginningClip",
            'path': "0d24f6607ebfbe3f88487369bfb07585.wav"
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
        self.sprite.layer = 5

    async def green_flag(self, util):
        self.set_effect('pixelate', 0)
        self.set_dirty(3)
        while not (self.variables['Menu'] == "0"):
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


    async def green_flag1(self, util):
        self.variables['Menu'] = "1"
        self.set_effect('brightness', -100)
        self.xpos = 0
        self.ypos = 0
        pass # sound_setvolumeto(100)
        self.set_effect('ghost', 0)
        self.visible = 1
        self.set_dirty(3)
        await self.sleep(1)
        for _ in range(10):
            self.change_effect('brightness', 10)
            self.set_dirty(3)
            await self.sleep(0.1)
            await self._yield(0)
        while not (self.variables['Menu'] == "0"):
            pass # sound_playuntildone('TheBeginningClip')
            await self._yield(0)


    async def broadcast_Play(self, util):
        self.variables['Menu'] = "0"
        for _ in range(10):
            pass # sound_changevolumeby(-10)
            self.change_effect('ghost', 10)
            self.set_dirty(3)
            await self.sleep(0.2)
            await self._yield(0)
        pass # sound_stopallsounds()
        self.visible = 0
        self.set_dirty(1)


    async def green_flag2(self, util):
        self.set_costume('costume2')
        self.set_dirty(3)
        while not (self.variables['Menu'] == "0"):
            await self.sleep(0.1)
            self.set_costume('costume3')
            self.set_dirty(3)
            await self.sleep(0.1)
            self.set_costume('costume2')
            await self._yield(3)



class play(engine.Target):
    costume = 0
    xpos, ypos = -178, -15
    direction = 90
    visible = False

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
            'green_flag': [
                self.green_flag,
                self.green_flag1,
            ],
            'sprite_clicked': [
                self.sprite_clicked,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 29

    async def green_flag(self, util):
        self.set_effect('pixelate', 0)
        self.set_dirty(3)
        while not (self.variables['Menu'] == "0"):
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


    async def green_flag1(self, util):
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


    async def sprite_clicked(self, util):
        for _ in range(5):
            self.change_effect('ghost', 10)
            self.set_dirty(3)
            await self.sleep(0.2)
            await self._yield(0)
        util.send_event('broadcast_Play')
        for _ in range(5):
            self.change_effect('ghost', 10)
            self.set_dirty(3)
            await self.sleep(0.2)
            await self._yield(0)
        self.visible = 0
        self.set_dirty(1)



class Sprite3(engine.Target):
    costume = 68
    xpos, ypos = 20, -60
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "1bd1f273007870cbc4fc013b14874a82.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "a63f1b6cdbd6778c474f7c2ec2f9e46f.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "3988f5f8a5ba5eeb6bb2608472517617.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "b335761d88315b7f2d8b53f8a3b9f767.png",
            'center': (114, 290),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "7a666ee7a957f6b44e115c7c65f6bbd0.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "68220ed38a14b957e71cdc0f1d359925.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "68220ed38a14b957e71cdc0f1d359925.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "106f245e9dda216243831dabcd344ad5.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "3f324689623c96163a4218e95b01dc55.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "3988f5f8a5ba5eeb6bb2608472517617.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "7a666ee7a957f6b44e115c7c65f6bbd0.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "3988f5f8a5ba5eeb6bb2608472517617.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "70a4687235890503e924ae1c2e986637.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "374c74321aa97c82ff1860ae1a42005b.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "f36c4555557c18174f675ec2e5fccb4e.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "3988f5f8a5ba5eeb6bb2608472517617.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "3988f5f8a5ba5eeb6bb2608472517617.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume29",
            'path': "374c74321aa97c82ff1860ae1a42005b.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume30",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume31",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume32",
            'path': "ffbd0461f1f8a156f963ed1f914847e2.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume33",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume34",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume35",
            'path': "3f10b273f8b1513b67794dc308906a1c.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume36",
            'path': "f36c4555557c18174f675ec2e5fccb4e.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume37",
            'path': "3988f5f8a5ba5eeb6bb2608472517617.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume38",
            'path': "70a4687235890503e924ae1c2e986637.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume39",
            'path': "70a4687235890503e924ae1c2e986637.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume41",
            'path': "70a4687235890503e924ae1c2e986637.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume40",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume42",
            'path': "7443233cf65d67b7e85c3434814f3df7.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume43",
            'path': "56c4e8c0183c1646b187e931e0022aa2.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume46",
            'path': "56c4e8c0183c1646b187e931e0022aa2.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume47",
            'path': "56c4e8c0183c1646b187e931e0022aa2.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume45",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume48",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume49",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume54",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume50",
            'path': "3f10b273f8b1513b67794dc308906a1c.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume51",
            'path': "7a666ee7a957f6b44e115c7c65f6bbd0.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume52",
            'path': "70a4687235890503e924ae1c2e986637.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume53",
            'path': "374c74321aa97c82ff1860ae1a42005b.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume55",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume56",
            'path': "56c4e8c0183c1646b187e931e0022aa2.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume57",
            'path': "3663d7f27b1b9bdd070fcf64ae21acfd.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume58",
            'path': "374c74321aa97c82ff1860ae1a42005b.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume59",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume60",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume61",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume62",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume63",
            'path': "a89d9f294177f68d676c087a596d4990.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume64",
            'path': "3988f5f8a5ba5eeb6bb2608472517617.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume65",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume66",
            'path': "279f3f7ba9295ab745be8180c628a034.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume67",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume68",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume69",
            'path': "a4cb93275fdad304ddbc655aa75b85e4.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume71",
            'path': "c9ad37ee17652fc9444d934ff6b71ed1.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume70",
            'path': "0fc961259c3bcfd9ef903bd5f8a70a50.png",
            'center': (112, 290),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "TheTaco",
            'path': "974378b0dd0111b396f2ad636a4845d3.wav"
        },
        {
            'name': "ThePerfectCombin",
            'path': "a1471d4cb7955179714fec8bec6fd8e6.wav"
        },
        {
            'name': "Cheese",
            'path': "4cd92fda24987d125eb82caf22d8e01d.wav"
        },
        {
            'name': "Substances",
            'path': "13404a53a0a09c82bfa087d744c0862a.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 4

    async def broadcast_Play(self, util):
        self.set_effect('ghost', 100)
        self.xpos = -180
        self.ypos = -60
        self.set_costume('costume3')
        self.visible = 1
        self.set_dirty(3)
        for _ in range(5):
            self.change_effect('ghost', -20)
            self.set_dirty(3)
            await self.sleep(0.2)
            await self._yield(0)
        for _ in range(10):
            for _ in range(5):
                await self.sleep(0.01)
                self.xpos += 2
                await self._yield(2)
            self.set_costume('costume4')
            self.ypos += 3
            self.set_dirty(3)
            for _ in range(5):
                await self.sleep(0.01)
                self.xpos += 2
                await self._yield(2)
            self.set_costume('costume3')
            self.ypos += -3
            await self._yield(3)
        self.set_costume('costume5')
        pass # sound_play('TheTaco')
        self.set_dirty(3)
        for _ in range(10):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        pass # sound_play('ThePerfectCombin')
        for _ in range(25):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.2)
        pass # sound_play('Cheese')
        for _ in range(5):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.2)
        pass # sound_play('Substances')
        for _ in range(24):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        util.send_event('broadcast_ImGonnaEatIt')
        await self.sleep(0.01)
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite4(engine.Target):
    costume = 19
    xpos, ypos = 40, -60
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "1bd1f273007870cbc4fc013b14874a82.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "a63f1b6cdbd6778c474f7c2ec2f9e46f.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "5ff1fff8d7a88aea4b101775895363fb.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "9f2c153172d2d808d5948241c80094ec.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "b3cd721641c8a02696d98c795e9d6b6d.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "9f2c153172d2d808d5948241c80094ec.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "f2f2a6793ab057db7138b02e0a22413a.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "3cea93484db13fdabab46cfd91e3753e.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "7530542f1854dbcb04603ce5f9a646ab.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "b3cd721641c8a02696d98c795e9d6b6d.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "ad2ebf37e139b0841b933abadfa469bb.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "7530542f1854dbcb04603ce5f9a646ab.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "7354a47e24f70d12d5f304e82e9068f3.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "f2f2a6793ab057db7138b02e0a22413a.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "1b9fa172bd4c541712d3669d079f2e15.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "1a457e81e5627e456aa0e35fbd09b42e.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "c465d2e8bdbfe65e086fb2df014146c6.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "b9b5cc2eea32caacb0cff8087e5f2c24.png",
            'center': (112, 290),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "1deb8cb09813eacda255ae91bf5b736e.png",
            'center': (112, 278),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "dfe31c63e254bdb27a4d1f472428d48d.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "a6cd054868f94322538e313df10544b0.png",
            'center': (236, 308),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "81efcb16197ff4cb7a90bf647f0c3308.png",
            'center': (236, 308),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "33faa2f7c690e6fdc063cb38604769fc.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume41",
            'path': "33faa2f7c690e6fdc063cb38604769fc.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "853250ac942832d9be387a96416f1b75.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "a431933896ac28d119f45797821d0d42.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume36",
            'path': "a431933896ac28d119f45797821d0d42.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "282c59208f1a2b148aa7426224c69e20.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "bfc70f871d87182f8646f0bcdfbe795b.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume37",
            'path': "bfc70f871d87182f8646f0bcdfbe795b.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume43",
            'path': "13e3c776895c02009f65cb6cdca21d07.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "282c59208f1a2b148aa7426224c69e20.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume29",
            'path': "f5d898af621681a0484a20a160a55434.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume30",
            'path': "bfc70f871d87182f8646f0bcdfbe795b.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume31",
            'path': "a431933896ac28d119f45797821d0d42.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume38",
            'path': "a431933896ac28d119f45797821d0d42.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume32",
            'path': "47ac902aa08b5b51464a2576bd309652.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume39",
            'path': "47ac902aa08b5b51464a2576bd309652.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume40",
            'path': "47ac902aa08b5b51464a2576bd309652.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume45",
            'path': "47ac902aa08b5b51464a2576bd309652.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume46",
            'path': "9d23f370f5d6496619f22720b0f30eeb.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume33",
            'path': "282c59208f1a2b148aa7426224c69e20.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume55",
            'path': "282c59208f1a2b148aa7426224c69e20.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume34",
            'path': "853250ac942832d9be387a96416f1b75.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume42",
            'path': "853250ac942832d9be387a96416f1b75.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume44",
            'path': "9033b35f165e8c40861e0fced4ccf3b2.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume35",
            'path': "f5d898af621681a0484a20a160a55434.png",
            'center': (236, 290),
            'scale': 2
        },
        {
            'name': "costume47",
            'path': "cc92b0293990094fe3df4710734d1209.png",
            'center': (228, 290),
            'scale': 2
        },
        {
            'name': "costume48",
            'path': "067e68e7a4a47e40279ec5b373d26fdd.png",
            'center': (228, 290),
            'scale': 2
        },
        {
            'name': "costume52",
            'path': "9117c25cb014d8683415fb1d557e14d0.png",
            'center': (228, 290),
            'scale': 2
        },
        {
            'name': "costume50",
            'path': "0ead5bcfa3b02459de37db21288f0750.png",
            'center': (228, 290),
            'scale': 2
        },
        {
            'name': "costume51",
            'path': "bf75827f4e8faf6388339af1e1ba6986.png",
            'center': (228, 290),
            'scale': 2
        },
        {
            'name': "costume53",
            'path': "12c417c42146859ee580ded2fe78d41e.png",
            'center': (228, 290),
            'scale': 2
        },
        {
            'name': "costume54",
            'path': "9117c25cb014d8683415fb1d557e14d0.png",
            'center': (228, 290),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "GonnaEatIt",
            'path': "dc4bbc629249ddf7765bbd320a56ae4f.wav"
        },
        {
            'name': "CarminaBurana",
            'path': "28c2261fae1a6a05b96d6d1110aff3a4.wav"
        },
        {
            'name': "WAAAIT",
            'path': "3e3d5f61491bfecba87345f992062025.wav"
        },
        {
            'name': "whoosh",
            'path': "6394551b397c5a9669d02786b4d8e91d.wav"
        },
        {
            'name': "DiscScratch1",
            'path': "6be738764383696b4e066d680abb00e1.wav"
        },
        {
            'name': "WhyCantIEatIt",
            'path': "72b7596613d30a9a8c3c5787ef22ada7.wav"
        },
        {
            'name': "No",
            'path': "f06a3ad3e043fa8e8d2125058cc7af75.wav"
        },
        {
            'name': "P",
            'path': "053cfdca74be25ecbc5dae7f9bcd3614.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_SoIMustEatTacos': [
                self.broadcast_SoIMustEatTacos,
            ],
            'broadcast_No': [
                self.broadcast_No,
            ],
            'broadcast_ThirdTimeAwkward': [
                self.broadcast_ThirdTimeAwkward,
            ],
            'broadcast_EvenMoreAwkward': [
                self.broadcast_EvenMoreAwkward,
            ],
            'broadcast_ImGonnaEatIt': [
                self.broadcast_ImGonnaEatIt,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_WhyCantIEatIt': [
                self.broadcast_WhyCantIEatIt,
            ],
            'broadcast_IsThereATrend': [
                self.broadcast_IsThereATrend,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 15

    async def broadcast_SoIMustEatTacos(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_No(self, util):
        self.set_costume('costume48')
        self.set_dirty(3)
        await self.sleep(0.08)
        self.set_costume('costume52')
        pass # sound_play('P')
        self.set_dirty(3)
        await self.sleep(1)
        pass # sound_play('No')
        next_costume = self.costume['number'] + 1
        if next_costume == len(self.costumes):
            self.set_costume(0)
        else:
            self.set_costume(next_costume)
        self.set_costume('costume50')
        self.set_dirty(3)
        for _ in range(3):
            await self.sleep(0.1)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(2)
        util.send_event('broadcast_NowHesAngry')
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ThirdTimeAwkward(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_EvenMoreAwkward(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_ImGonnaEatIt(self, util):
        self.visible = 1
        pass # sound_setvolumeto(100)
        other = util.targets['Sprite3']
        self.xpos, self.ypos = other.xpos, other.ypos
        self.set_costume('costume4')
        self.set_dirty(3)
        await self.sleep(0.5)
        pass # sound_play('GonnaEatIt')
        for _ in range(10):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        util.send_event('broadcast_MouthOpensDramatically')
        self.set_costume('costume15')
        pass # sound_stopallsounds()
        pass # sound_setvolumeto(50)
        pass # sound_play('CarminaBurana')
        self.set_dirty(3)
        for _ in range(2):
            await self.sleep(1.8)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(2.4)
        pass # sound_stopallsounds()
        pass # sound_setvolumeto(80)
        pass # sound_playuntildone('DiscScratch1')
        pass # sound_playuntildone('WAAAIT')
        util.send_event('broadcast_Umm')
        self.set_costume('costume18')
        self.set_dirty(3)
        await self.sleep(1)
        pass # sound_play('whoosh')
        self.set_costume('costume19')
        self.set_dirty(3)
        await self.sleep(0.05)
        self.xpos += 10
        self.set_costume('costume22')
        self.set_dirty(3)
        await self.sleep(0.05)
        self.xpos += 10
        self.set_costume('costume20')
        self.set_dirty(3)
        await self.sleep(1)
        util.send_event('broadcast_Awkward')
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WhyCantIEatIt(self, util):
        pass # sound_play('WhyCantIEatIt')
        self.set_costume('costume23')
        self.set_dirty(3)
        for _ in range(24):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        util.send_event('broadcast_ILoveTacos')
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_IsThereATrend(self, util):
        self.set_costume('costume47')
        self.visible = 1
        self.set_dirty(3)



class Sprite1(engine.Target):
    costume = 2
    xpos, ypos = -148, -57
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "191afa828fa6236158a7152515e70d1e.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "ab16af524d6db75684aa0112acff9db6.png",
            'center': (202, 258),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "2bd5adfc1abf5d3a83d5955fe4ad4a83.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "38dfeec1fe76b31aa7a4f81f60cb1e93.png",
            'center': (202, 258),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "42f9e8339bb382221a7f8e9a38329c2a.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "130c5721d3613f4db2d4e28276afd3ea.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "6492407f7ea9c56caa1ce629542a35d2.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "d50fe6b9b4be8f80571826897e9164f6.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "c1bc418bf403cd7f451c2646d0d9e3a2.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "013da338eb05711d619df643b4245ec8.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "837581a941a7a3d5db056ff422bc830d.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "a1fb58f2ee31021497a5c36daa82ecae.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "0c18d8cb3658e4bf26f5d60494608f6d.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "b1b4e11170e8f6134cc4463434ee7d9b.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "130c5721d3613f4db2d4e28276afd3ea.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "41f4e4a1489f3a3947a055160ba624fd.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "d50fe6b9b4be8f80571826897e9164f6.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "6492407f7ea9c56caa1ce629542a35d2.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "e4765f211bad3139ceca57ab9822d836.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "86bddeb730ed57ff689542bc097d3c4e.png",
            'center': (100, 258),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "StepOnGrass",
            'path': "a5315d37dfa4b2ac66ed6793f38ea4d1.wav"
        },
        {
            'name': "GiveMeTheTaco",
            'path': "6e57606dfc3c945c9283c9ad8a353710.wav"
        },
        {
            'name': "Crickets",
            'path': "f4e767071648efe324789bcb3b88c038.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_NowHesAngry': [
                self.broadcast_NowHesAngry,
            ],
            'broadcast_ThirdTimeAwkward': [
                self.broadcast_ThirdTimeAwkward,
            ],
            'broadcast_ILoveTacos': [
                self.broadcast_ILoveTacos,
            ],
            'broadcast_EvenMoreAwkward': [
                self.broadcast_EvenMoreAwkward,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_IsThereATrend': [
                self.broadcast_IsThereATrend,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 32

    async def broadcast_NowHesAngry(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ThirdTimeAwkward(self, util):
        self.xpos = -129
        self.ypos = -66
        self.set_costume('costume4')
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        await self.sleep(0.5)
        pass # sound_playuntildone('Crickets')
        pass # sound_play('StepOnGrass')
        self.xpos = -148
        self.ypos = -57
        self.set_costume('costume3')
        util.send_event('broadcast_IsThereATrend')
        self.set_dirty(3)


    async def broadcast_ILoveTacos(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_EvenMoreAwkward(self, util):
        self.xpos = -129
        self.ypos = -66
        self.set_costume('costume2')
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        await self.sleep(0.5)
        pass # sound_playuntildone('Crickets')
        pass # sound_play('StepOnGrass')
        self.xpos = -148
        self.ypos = -57
        self.set_costume('costume3')
        self.set_dirty(3)
        await self.sleep(1)
        util.send_event('broadcast_WhyCantIEatIt')


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_IsThereATrend(self, util):
        pass # sound_play('StepOnGrass')
        self.xpos = -148
        self.ypos = -57
        self.set_costume('costume3')
        self.set_dirty(3)
        await self.sleep(1)
        self.set_costume('costume6')
        pass # sound_play('GiveMeTheTaco')
        self.set_dirty(3)
        for _ in range(14):
            await self.sleep(0.06)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(1)
        util.send_event('broadcast_No')



class Sprite5(engine.Target):
    costume = 0
    xpos, ypos = 66, -5
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume2",
            'path': "41fb1754f0428a2c0f1be78ffbad556d.png",
            'center': (52, 36),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Umm': [
                self.broadcast_Umm,
            ],
            'broadcast_MouthOpensDramatically': [
                self.broadcast_MouthOpensDramatically,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 30

    async def broadcast_Umm(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_MouthOpensDramatically(self, util):
        self.xpos = 66
        self.ypos = -5
        self.front_layer(util)
        self.visible = 1
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite6(engine.Target):
    costume = 30
    xpos, ypos = -96, -40
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "57c6ec48b886cd092ada961516119772.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "82ad19c185f725b229ba55474947661f.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "90ca80e98343ec3406b0cbab79bb5a1b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "157c8121e5c2e6744aaab6ff911aaac0.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "f2e9208319b9a8393c2a5fe3f929270d.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "aef49094dc838ef4a064e19a660d233a.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "3453c8717a7ff60e8a741171d1e8bf99.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "e3f9c3cfe49a038d184cccfb5be5ed92.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "48534cfa5d19896ba70efa422fdc3bf6.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "ce6433d91265c6f03d1f9af89408b2ad.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "aef49094dc838ef4a064e19a660d233a.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "853890d69b1db573ed442df6fbc280bd.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "3da96479609e2927d5e4a878fe90f5bf.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "a6a49c2592954933daf6bcdd24831119.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "021f567149fca555bb90979d4fdea61f.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "889f9bb84bba294b07524bc7754075c2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "3453c8717a7ff60e8a741171d1e8bf99.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "e3f9c3cfe49a038d184cccfb5be5ed92.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "48534cfa5d19896ba70efa422fdc3bf6.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "3da96479609e2927d5e4a878fe90f5bf.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "a6a49c2592954933daf6bcdd24831119.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "3453c8717a7ff60e8a741171d1e8bf99.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "9b1eff3d40aad90eb9684b9f6b460a81.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "3c0d5a573050e6088aba9610f186b35b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "7f8b47c37bb4c2d2be499141f2a095cb.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "c2c62d3265dc64b1c47ba6f02dfce246.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume29",
            'path': "8f08c789b80bbe1b8d1d094cec0a1212.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume30",
            'path': "c789cf971cf599e5a77a2e4beb591e56.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume31",
            'path': "75dce02e47282d061269a66a1a1d7ac7.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume32",
            'path': "1c275ba4cea354ad212224fe66369c62.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume33",
            'path': "4ec28f8fa5b8d63280bafb96ff8227f4.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume34",
            'path': "3c0d5a573050e6088aba9610f186b35b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume45",
            'path': "224795c199c5cf3b455bb7f5fa5470d0.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume35",
            'path': "acee023a8dc8f66ab66f52ef3caab8b7.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume37",
            'path': "3c0d5a573050e6088aba9610f186b35b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume38",
            'path': "4ec28f8fa5b8d63280bafb96ff8227f4.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume39",
            'path': "8f08c789b80bbe1b8d1d094cec0a1212.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume44",
            'path': "4ec28f8fa5b8d63280bafb96ff8227f4.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume46",
            'path': "4ec28f8fa5b8d63280bafb96ff8227f4.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume40",
            'path': "7f8b47c37bb4c2d2be499141f2a095cb.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume41",
            'path': "c2c62d3265dc64b1c47ba6f02dfce246.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume47",
            'path': "c3fe503ff5973f4e31708b86e4b7fc99.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume43",
            'path': "4ec28f8fa5b8d63280bafb96ff8227f4.png",
            'center': (330, 260),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "ILoveTacos",
            'path': "196bf76f87105187896bf6e10f6cf000.wav"
        },
        {
            'name': "SoIMustEatTacos",
            'path': "fabb1d8fc222a42beca18f66604fab84.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_SoIMustEatTacos': [
                self.broadcast_SoIMustEatTacos,
            ],
            'broadcast_EvenMoreAwkward': [
                self.broadcast_EvenMoreAwkward,
            ],
            'broadcast_Awkward': [
                self.broadcast_Awkward,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_ILoveTacos': [
                self.broadcast_ILoveTacos,
            ],
            'broadcast_ThirdTimeAwkward': [
                self.broadcast_ThirdTimeAwkward,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 6

    async def broadcast_SoIMustEatTacos(self, util):
        self.size = 130
        self.xpos = -96
        self.ypos = -40
        self.set_costume('costume26')
        self.visible = 1
        pass # sound_play('SoIMustEatTacos')
        self.set_dirty(3)
        for _ in range(7):
            await self.sleep(0.09)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.1)
        for _ in range(3):
            await self.sleep(0.09)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.07)
        for _ in range(9):
            await self.sleep(0.08)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(4)
        util.send_event('broadcast_IsThereATrend')
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_EvenMoreAwkward(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Awkward(self, util):
        self.size = 130
        self.xpos = -96
        self.ypos = -40
        self.set_costume('costume4')
        self.visible = 1
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ILoveTacos(self, util):
        self.size = 130
        self.xpos = -96
        self.ypos = -40
        self.set_costume('costume6')
        self.visible = 1
        pass # sound_play('ILoveTacos')
        self.set_dirty(3)
        for _ in range(17):
            await self.sleep(0.09)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        util.send_event('broadcast_ThirdTimeAwkward')
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ThirdTimeAwkward(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite7(engine.Target):
    costume = 0
    xpos, ypos = 76, -92
    direction = 130
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "30bdf4d9da96413afec7c7539d96292f.png",
            'center': (120, 146),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_ThirdTimeAwkward': [
                self.broadcast_ThirdTimeAwkward,
            ],
            'broadcast_ILoveTacos': [
                self.broadcast_ILoveTacos,
            ],
            'broadcast_Awkward': [
                self.broadcast_Awkward,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_SoIMustEatTacos': [
                self.broadcast_SoIMustEatTacos,
            ],
            'broadcast_IsThereATrend': [
                self.broadcast_IsThereATrend,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 31

    async def broadcast_ThirdTimeAwkward(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ILoveTacos(self, util):
        self.size = 186
        self.xpos = 76
        self.ypos = -92
        self.set_direction(120)
        self.set_costume('costume1')
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        for _ in range(10):
            await self.sleep(0.05)
            self.set_direction(self.direction + 1)
            await self._yield(3)


    async def broadcast_Awkward(self, util):
        self.size = 186
        self.xpos = 76
        self.ypos = -92
        self.set_direction(120)
        self.set_costume('costume1')
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        for _ in range(10):
            await self.sleep(0.05)
            self.set_direction(self.direction + 1)
            await self._yield(3)
        await self.sleep(2)
        util.send_event('broadcast_EvenMoreAwkward')
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_SoIMustEatTacos(self, util):
        self.size = 186
        self.xpos = 76
        self.ypos = -92
        self.set_direction(120)
        self.set_costume('costume1')
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        await self.sleep(1)
        for _ in range(10):
            await self.sleep(0.05)
            self.set_direction(self.direction + 1)
            await self._yield(3)


    async def broadcast_IsThereATrend(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite8(engine.Target):
    costume = 17
    xpos, ypos = -67, 23
    direction = 100
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "df3db9623cdefc7eaec2072363ef0507.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "941fd91fc7decc66d4344ef8925f9be2.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "1371db0d6d2fdb8b77d68bbe81b8745a.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "9380057577500642e060459451383119.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "3563cda96eb029f79ded9441b8316a15.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "9e9536f77d8e354bd67d040f0d4b65eb.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "05dd071555be301db651967e3b21601e.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "05dd071555be301db651967e3b21601e.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "1371db0d6d2fdb8b77d68bbe81b8745a.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "1371db0d6d2fdb8b77d68bbe81b8745a.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "941fd91fc7decc66d4344ef8925f9be2.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "1371db0d6d2fdb8b77d68bbe81b8745a.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "1371db0d6d2fdb8b77d68bbe81b8745a.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "941fd91fc7decc66d4344ef8925f9be2.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "1d1caaf136313f587f6d29e15b27a59d.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "c6240cdc536afc8bb281bcc4a9aed1d4.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "2f420230828f1afae129d3c80e2be706.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "39d1984909aa3109e1874614e94d2122.png",
            'center': (252, 290),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "e81ea96be82bc915a2958e40797db1fe.png",
            'center': (252, 290),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "GIVEMETHETACO",
            'path': "c89907bbca6e570dcc9f643f6b78de58.wav"
        },
        {
            'name': "Intense",
            'path': "50074debdbf98e1bc4ff02962451d061.wav"
        },
        {
            'name': "Arrrrrrgh",
            'path': "9c4df806e575a68fbc779fe043d97f02.wav"
        },
        {
            'name': "Lightning",
            'path': "bc4fea116f6795e0bbe03983dcdf370b.wav"
        },
        {
            'name': "Lightning1",
            'path': "f7a85705e4eda971b4222115915947b6.wav"
        },
        {
            'name': "Lightning2",
            'path': "79f46530d1f720f112bb17934e267c37.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Running': [
                self.broadcast_Running,
            ],
            'broadcast_NowHesAngry': [
                self.broadcast_NowHesAngry,
                self.broadcast_NowHesAngry_1,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Lightning': [
                self.broadcast_Lightning,
            ],
            'broadcast_IsThisTheEnd': [
                self.broadcast_IsThisTheEnd,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 9

    async def broadcast_Running(self, util):
        self.set_direction(100)
        self.xpos = -148
        self.ypos = -68
        self.size = 59
        self.set_costume('costume21')
        self.visible = 1
        pass # sound_play('Arrrrrrgh')
        await self.glide(5, -112, 41)
        util.send_event('broadcast_Lightning')
        self.set_dirty(3)


    async def broadcast_NowHesAngry(self, util):
        pass # sound_play('Intense')


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_NowHesAngry_1(self, util):
        self.xpos = -105
        self.ypos = -53
        self.size = 116
        self.visible = 1
        self.set_costume('costume2')
        util.send_event('broadcast_Lightning')
        self.set_dirty(3)
        for _ in range(5):
            await self.sleep(0.09)
            self.ypos += 2
            self.xpos += 1
            await self._yield(2)
        pass # sound_setvolumeto(500)
        pass # sound_play('GIVEMETHETACO')
        self.set_costume('costume2')
        self.set_dirty(3)
        for _ in range(16):
            await self.sleep(0.08)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            self.ypos += 2
            self.xpos += 1
            await self._yield(3)
        for _ in range(12):
            await self.sleep(0.09)
            self.ypos += 2
            self.xpos += 1
            await self._yield(2)
        util.send_event('broadcast_Lightning')
        for _ in range(5):
            await self.sleep(0.09)
            self.ypos += 2
            self.xpos += 1
            await self._yield(2)
        util.send_event('broadcast_OhNo')
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Lightning(self, util):
        pass # sound_play(random.randint(4, 6))
        self.set_effect('brightness', 50)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', 0)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', 30)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(30):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def broadcast_IsThisTheEnd(self, util):
        await self.glide(4, 44, -27)
        util.send_event('broadcast_Kablammie')
        self.visible = 0
        self.set_dirty(2)



class Sprite11(engine.Target):
    costume = 0
    xpos, ypos = -67, 23
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "99046765854aa1df6c58bf47eef52e67.png",
            'center': (330, 318),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "158fc9c3de52bf12314a60621368a9a6.png",
            'center': (302, 334),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "e119ec93c1c3b65bda55741803196a14.png",
            'center': (350, 330),
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
            'broadcast_Running': [
                self.broadcast_Running,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_OhNo': [
                self.broadcast_OhNo,
            ],
            'broadcast_NowHesAngry': [
                self.broadcast_NowHesAngry,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 3

    async def broadcast_Kablammie(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Running(self, util):
        self.size = 59
        self.visible = 1
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_OhNo(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_NowHesAngry(self, util):
        self.xpos = -105
        self.ypos = -53
        self.size = 116
        self.set_effect('ghost', 25)
        self.visible = 1
        self.change_layer(util, -99)
        self.set_costume('costume1')
        self.set_dirty(3)
        while True:
            await self.sleep(0.1)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            other = util.targets['Sprite8']
            self.xpos, self.ypos = other.xpos, other.ypos
            await self._yield(3)



class Sprite9(engine.Target):
    costume = 1
    xpos, ypos = 89, -90
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "f8832d08f0fc8f88ef26d2bbf0404cfc.png",
            'center': (106, 322),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "801a7fbe13d50e4609b0ffb0af1e599f.png",
            'center': (106, 322),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "801a7fbe13d50e4609b0ffb0af1e599f.png",
            'center': (96, 322),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "d609af5833c732796840791df60e0421.png",
            'center': (278, 206),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "f985262954fa747ec697e62ddba5d8f4.png",
            'center': (272, 322),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "24262e36bceb6bfd9236a56114d3a15c.png",
            'center': (272, 322),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "0eeed6187ece48d03356e048d52de5ed.png",
            'center': (272, 360),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "3877aae28c7df737b6e8821952fb5acb.png",
            'center': (272, 360),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "GIVEMETHETACO",
            'path': "c89907bbca6e570dcc9f643f6b78de58.wav"
        },
        {
            'name': "Intense",
            'path': "50074debdbf98e1bc4ff02962451d061.wav"
        },
        {
            'name': "Piff",
            'path': "1b59efcfa3b640a8c8fd7233b9b30833.wav"
        },
        {
            'name': "whoosh",
            'path': "6394551b397c5a9669d02786b4d8e91d.wav"
        },
        {
            'name': "ShortScream",
            'path': "ab66262ea60f9764ca61785e4ce1179f.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Lightning': [
                self.broadcast_Lightning,
            ],
            'broadcast_IsThisTheEnd': [
                self.broadcast_IsThisTheEnd,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_OhNo': [
                self.broadcast_OhNo,
            ],
            'broadcast_Running': [
                self.broadcast_Running,
            ],
            'broadcast_Kablammie': [
                self.broadcast_Kablammie,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 16

    async def broadcast_Lightning(self, util):
        self.set_effect('brightness', 50)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', 0)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', 30)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(30):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def broadcast_IsThisTheEnd(self, util):
        pass # sound_play('whoosh')
        self.set_direction(105)
        self.set_dirty(3)
        for _ in range(4):
            await self.sleep(0.07)
            self.ypos += 1
            self.set_costume('costume7')
            self.set_dirty(3)
            await self.sleep(0.07)
            self.ypos += -1
            self.set_costume('costume8')
            self.xpos += 4
            await self._yield(3)
        pass # sound_play('ShortScream')
        for _ in range(4):
            await self.sleep(0.07)
            self.ypos += 1
            self.set_costume('costume7')
            self.set_dirty(3)
            await self.sleep(0.07)
            self.ypos += -1
            self.set_costume('costume8')
            self.xpos += -2
            await self._yield(3)
        for _ in range(3):
            for _ in range(4):
                await self.sleep(0.07)
                self.ypos += 1
                self.set_costume('costume7')
                self.set_dirty(3)
                await self.sleep(0.07)
                self.ypos += -1
                self.set_costume('costume8')
                self.xpos += 4
                await self._yield(3)
            for _ in range(4):
                await self.sleep(0.07)
                self.ypos += 1
                self.set_costume('costume7')
                self.set_dirty(3)
                await self.sleep(0.07)
                self.ypos += -1
                self.set_costume('costume8')
                self.xpos += -2
                await self._yield(3)
            await self._yield(0)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_OhNo(self, util):
        self.set_effect('ghost', 0)
        self.xpos = 89
        self.ypos = -90
        self.set_direction(90)
        self.size = 116
        self.set_costume('costume2')
        self.visible = 1
        self.set_dirty(3)
        for _ in range(15):
            await self.sleep(0.01)
            self.set_direction(self.direction + 1)
            await self._yield(3)
        await self.sleep(1)
        for _ in range(10):
            self.set_costume('costume3')
            self.set_dirty(3)
            await self.sleep(0.01)
            self.set_costume('costume2')
            self.set_dirty(3)
            await self.sleep(0.01)
            await self._yield(0)
        util.send_event('broadcast_Lightning')
        for _ in range(10):
            self.set_costume('costume3')
            self.set_dirty(3)
            await self.sleep(0.01)
            self.set_costume('costume2')
            self.set_dirty(3)
            await self.sleep(0.01)
            await self._yield(0)
        self.xpos = 170
        self.ypos = -86
        pass # sound_play('Piff')
        self.set_direction(90)
        self.set_effect('ghost', 50)
        self.set_costume('costume4')
        self.set_dirty(3)
        for _ in range(5):
            await self.sleep(0.08)
            self.change_effect('ghost', 10)
            await self._yield(3)
        await self.sleep(1)
        self.variables['UhOh'] = "1"
        util.send_event('broadcast_Running')


    async def broadcast_Running(self, util):
        self.set_direction(75)
        self.xpos = 89
        self.ypos = -90
        self.size = 59
        self.set_effect('ghost', 0)
        self.set_costume('costume5')
        self.set_dirty(3)
        for _ in range(4):
            for _ in range(4):
                await self.sleep(0.07)
                self.ypos += 1
                self.set_costume('costume6')
                self.set_dirty(3)
                await self.sleep(0.07)
                self.ypos += -1
                self.set_costume('costume5')
                self.xpos += 3
                await self._yield(3)
            for _ in range(4):
                await self.sleep(0.07)
                self.ypos += 1
                self.set_costume('costume6')
                self.set_dirty(3)
                await self.sleep(0.07)
                self.ypos += -1
                self.set_costume('costume5')
                self.xpos += -3
                await self._yield(3)
            await self._yield(0)
        util.send_event('broadcast_IsThisTheEnd')


    async def broadcast_Kablammie(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite10(engine.Target):
    costume = 0
    xpos, ypos = 99, -51
    direction = -61
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
        self.sprite.layer = 14

    async def broadcast_Kablammie(self, util):
        self.variables['UhOh'] = "0"
        self.xpos = -152
        self.ypos = -28
        self.size = 57
        pass # sound_stopallsounds()
        self.set_effect('ghost', 0)
        self.visible = 1
        self.set_effect('brightness', 0)
        self.set_dirty(3)
        for _ in range(10):
            self.variables['#'] = random.randint(1, 12)
            pass # sound_play(self.variables['#'])
            self.set_direction(self.direction + random.randint(-30, 30))
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            self.set_dirty(3)
            await self.sleep(0.1)
            self.xpos += 50
            await self._yield(2)
        util.send_event('broadcast_SlowDownFolks')
        self.xpos = 99
        self.ypos = -51
        self.set_effect('brightness', -20)
        self.set_costume('costume1')
        self.size = 134
        self.set_dirty(3)
        for _ in range(4):
            for _ in range(12):
                self.variables['#'] = random.randint(1, 12)
                pass # sound_play(self.variables['#'])
                self.set_direction(self.direction + random.randint(-30, 30))
                next_costume = self.costume['number'] + 1
                if next_costume == len(self.costumes):
                    self.set_costume(0)
                else:
                    self.set_costume(next_costume)
                self.set_dirty(3)
                await self.sleep(0.1)
                await self._yield(0)
            await self._yield(0)
        util.send_event('broadcast_NowZeke')
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('ghost', 10)
            await self._yield(3)
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite15(engine.Target):
    costume = 0
    xpos, ypos = 0, 0
    direction = 90
    visible = False

    costumes = [
        {
            'name': "background1",
            'path': "d8ee44bdec07f0f4aa7f3b803da8d75e.png",
            'center': (-178, 222),
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
            'broadcast_SlowDownFolks': [
                self.broadcast_SlowDownFolks,
            ],
            'broadcast_Kablammie': [
                self.broadcast_Kablammie,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 23

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_SlowDownFolks(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Kablammie(self, util):
        self.xpos = 0
        self.ypos = 0
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(2)



class Sprite12(engine.Target):
    costume = 0
    xpos, ypos = 56, -124
    direction = 75
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "b7d0d369d49323580ded2ec39fc2e8b6.png",
            'center': (204, 198),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "TheTaco",
            'path': "974378b0dd0111b396f2ad636a4845d3.wav"
        },
        {
            'name': "ThePerfectCombin",
            'path': "a1471d4cb7955179714fec8bec6fd8e6.wav"
        },
        {
            'name': "Cheese",
            'path': "4cd92fda24987d125eb82caf22d8e01d.wav"
        },
        {
            'name': "Substances",
            'path': "13404a53a0a09c82bfa087d744c0862a.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Flash': [
                self.broadcast_Flash,
            ],
            'broadcast_HeyGuys': [
                self.broadcast_HeyGuys,
            ],
            'broadcast_WhatThe': [
                self.broadcast_WhatThe,
            ],
            'broadcast_NowZeke': [
                self.broadcast_NowZeke,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_WhereIsIt': [
                self.broadcast_WhereIsIt,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 19

    async def broadcast_Flash(self, util):
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', -20)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def broadcast_HeyGuys(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WhatThe(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_NowZeke(self, util):
        self.set_direction(75)
        self.xpos = 56
        self.ypos = -124
        self.set_effect('brightness', -20)
        self.visible = 1
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WhereIsIt(self, util):
        self.visible = 1
        self.set_dirty(1)



class Sprite13(engine.Target):
    costume = 24
    xpos, ypos = 28, -6
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "d0bff393f8f52fbd1128885ce252d116.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "9242ef51b80e8ee52d04d55bf5889885.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "64ac8d62ba03190e565a381c6659b467.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "17fda3ecedb6e971233fbf64d88b9ccf.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "fb88d7033f94b57b2603ec3b946cf747.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "39fc795593a8cace93e32dbef7b384cd.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "d0b9f7eb002470bf817a9d2dd7093504.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "689c6634c48a8423bd166ec5a518af48.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "689c6634c48a8423bd166ec5a518af48.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "689c6634c48a8423bd166ec5a518af48.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "64ac8d62ba03190e565a381c6659b467.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "d0b9f7eb002470bf817a9d2dd7093504.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "caf10935c1656be59ea584d739ca4c13.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "caf10935c1656be59ea584d739ca4c13.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "eb246dbd0e6291697188d961f882dd1c.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "9242ef51b80e8ee52d04d55bf5889885.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "689c6634c48a8423bd166ec5a518af48.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "689c6634c48a8423bd166ec5a518af48.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "e5b1d9e7d80bc17276e18fcc0401efaf.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "17fda3ecedb6e971233fbf64d88b9ccf.png",
            'center': (98, 252),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "ac36b93354264d6a56bc4a66949ea671.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "1ddbb10ad79e1e6298583b4af9eed8b3.png",
            'center': (100, 282),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "5c81455b1379e0009ef0359b3e9fe953.png",
            'center': (100, 242),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "d3613507abf302ec3519157a8683525b.png",
            'center': (100, 258),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "c71e7506ce46c061469ea101283ae658.png",
            'center': (100, 258),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "NowZeke",
            'path': "c73dbfc5ef65f3e0fc7127b9ada7bb8b.wav"
        },
        {
            'name': "GiveMeThe",
            'path': "b199d18519b6f01b10ca9edcdb92d2ab.wav"
        },
        {
            'name': "whoosh",
            'path': "6394551b397c5a9669d02786b4d8e91d.wav"
        },
        {
            'name': "DaveGasp",
            'path': "87dc97e02d271f180493e77ff31737a3.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Flash': [
                self.broadcast_Flash,
            ],
            'broadcast_NowZeke': [
                self.broadcast_NowZeke,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_WhereIsIt': [
                self.broadcast_WhereIsIt,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 24

    async def broadcast_Flash(self, util):
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', -20)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def broadcast_NowZeke(self, util):
        self.xpos = 57
        self.ypos = -6
        self.set_costume('costume10')
        self.set_effect('brightness', -20)
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        await self.sleep(2)
        pass # sound_play('NowZeke')
        self.set_costume('costume2')
        self.set_dirty(3)
        for _ in range(8):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(1)
        pass # sound_play('GiveMeThe')
        self.set_costume('costume12')
        self.set_dirty(3)
        for _ in range(8):
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        util.send_event('broadcast_WhatThe')
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WhereIsIt(self, util):
        self.set_costume('costume21')
        self.visible = 1
        self.set_dirty(3)
        await self.sleep(1)
        pass # sound_play('whoosh')
        self.set_costume('costume23')
        self.set_dirty(3)
        await self.sleep(0.05)
        self.set_costume('costume22')
        self.xpos = 28
        self.ypos = -6
        self.set_dirty(3)
        await self.sleep(0.05)
        self.set_costume('costume24')
        self.set_dirty(3)
        await self.sleep(0.8)
        self.set_costume('costume25')
        pass # sound_playuntildone('DaveGasp')
        self.set_dirty(3)
        await self.sleep(1)
        util.send_event('broadcast_HeyGuys')
        self.visible = 0
        self.set_dirty(1)



class Sprite14(engine.Target):
    costume = 15
    xpos, ypos = 0, 0
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "38d27d919b11a94ddb10ba31fb297357.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "f92aba0c9efdad88ba8c8701c5fc6f88.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "7a2bad2523ee1944f4904fe4bfcce7eb.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "552d3cd3c6008d94e9b2fa86fcf67d71.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "f4d898bfe974d2f272cda82d7978d5af.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "27916f725b36f24e7f0c9151a299e990.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "94f9b36bd7b96f2ebe09ce2bd08827b2.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "c64f673722cf22556a366e828a4b145e.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "29cc34e4892df204c8886b8b15262074.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "7a2bad2523ee1944f4904fe4bfcce7eb.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "c64f673722cf22556a366e828a4b145e.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "128c618e642eda0ffdc658e114452649.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "27916f725b36f24e7f0c9151a299e990.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "f92aba0c9efdad88ba8c8701c5fc6f88.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "424315fc57595f5033147f65fd5c5164.png",
            'center': (328, 308),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "27916f725b36f24e7f0c9151a299e990.png",
            'center': (328, 308),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "WheresTheTaco",
            'path': "eea07780614a660b11a29354e030fa4b.wav"
        },
        {
            'name': "Gasp",
            'path': "c20525e74b7c405de2c9a072bae14f80.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Flash': [
                self.broadcast_Flash,
            ],
            'broadcast_WhatThe': [
                self.broadcast_WhatThe,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 7

    async def broadcast_Flash(self, util):
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', -20)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def broadcast_WhatThe(self, util):
        self.xpos = 0
        self.ypos = 0
        self.set_costume('costume1')
        self.set_effect('brightness', -15)
        self.visible = 1
        pass # sound_play('WheresTheTaco')
        self.set_dirty(3)
        for _ in range(14):
            await self.sleep(0.08)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        self.set_costume('costume16')
        pass # sound_playuntildone('Gasp')
        self.set_dirty(3)
        await self.sleep(1)
        util.send_event('broadcast_WhereIsIt')
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite17(engine.Target):
    costume = 0
    xpos, ypos = 40, -60
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "fecec238df426b1a51dc64409467f2d0.png",
            'center': (198, -146),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_NowHesAngry': [
                self.broadcast_NowHesAngry,
            ],
            'broadcast_IsThereATrend': [
                self.broadcast_IsThereATrend,
            ],
            'broadcast_ThirdTimeAwkward': [
                self.broadcast_ThirdTimeAwkward,
            ],
            'broadcast_EvenMoreAwkward': [
                self.broadcast_EvenMoreAwkward,
            ],
            'broadcast_SoIMustEatTacos': [
                self.broadcast_SoIMustEatTacos,
                self.broadcast_SoIMustEatTacos_1,
            ],
            'broadcast_ILoveTacos': [
                self.broadcast_ILoveTacos,
            ],
            'broadcast_Awkward': [
                self.broadcast_Awkward,
            ],
            'broadcast_ImGonnaEatIt': [
                self.broadcast_ImGonnaEatIt,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 1

    async def broadcast_NowHesAngry(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_IsThereATrend(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_ThirdTimeAwkward(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_EvenMoreAwkward(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_SoIMustEatTacos(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ILoveTacos(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Awkward(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_SoIMustEatTacos_1(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ImGonnaEatIt(self, util):
        self.variables['Zeke1or2'] = "2"


    async def broadcast_Play(self, util):
        self.variables['Zeke1or2'] = "1"
        self.visible = 1
        self.set_dirty(1)
        while True:
            if (self.variables['Zeke1or2'] == "1"):
                other = util.targets['Sprite3']
                self.xpos, self.ypos = other.xpos, other.ypos
                self.change_layer(util, -99)
                self.set_effect('ghost', 75)
                self.set_dirty(3)
            if (self.variables['Zeke1or2'] == "2"):
                other = util.targets['Sprite4']
                self.xpos, self.ypos = other.xpos, other.ypos
                self.change_layer(util, -99)
                self.set_effect('ghost', 75)
                self.set_dirty(3)
            await self._yield(0)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite18(engine.Target):
    costume = 0
    xpos, ypos = -148, -57
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "fecec238df426b1a51dc64409467f2d0.png",
            'center': (198, -146),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_WhatThe': [
                self.broadcast_WhatThe,
            ],
            'broadcast_NowHesAngry': [
                self.broadcast_NowHesAngry,
            ],
            'broadcast_Play': [
                self.broadcast_Play,
            ],
            'broadcast_IsThereATrend': [
                self.broadcast_IsThereATrend,
            ],
            'broadcast_ThirdTimeAwkward': [
                self.broadcast_ThirdTimeAwkward,
            ],
            'broadcast_EvenMoreAwkward': [
                self.broadcast_EvenMoreAwkward,
            ],
            'broadcast_SoIMustEatTacos': [
                self.broadcast_SoIMustEatTacos,
                self.broadcast_SoIMustEatTacos_1,
            ],
            'broadcast_ILoveTacos': [
                self.broadcast_ILoveTacos,
            ],
            'broadcast_Awkward': [
                self.broadcast_Awkward,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 2

    async def broadcast_WhatThe(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_NowHesAngry(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Play(self, util):
        self.visible = 0
        self.set_dirty(1)
        while True:
            other = util.targets['Sprite1']
            self.xpos, self.ypos = other.xpos, other.ypos
            self.change_layer(util, -99)
            self.set_effect('ghost', 75)
            await self._yield(3)


    async def broadcast_IsThereATrend(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_ThirdTimeAwkward(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_EvenMoreAwkward(self, util):
        self.visible = 1
        self.set_dirty(1)


    async def broadcast_SoIMustEatTacos(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_ILoveTacos(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Awkward(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_SoIMustEatTacos_1(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite19(engine.Target):
    costume = 0
    xpos, ypos = 0, 0
    direction = 90
    visible = False

    costumes = [
        {
            'name': "background2",
            'path': "9600252351ef03b45467c2ad6c6d97bb.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Flash': [
                self.broadcast_Flash,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_HeyGuys': [
                self.broadcast_HeyGuys,
            ],
            'broadcast_Credits': [
                self.broadcast_Credits,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 25

    async def broadcast_Flash(self, util):
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', -20)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_HeyGuys(self, util):
        self.xpos = 0
        self.ypos = 0
        self.set_effect('brightness', -20)
        self.visible = 1
        self.front_layer(util)
        self.change_layer(util, -1)
        self.set_dirty(3)


    async def broadcast_Credits(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite20(engine.Target):
    costume = 0
    xpos, ypos = 83, -61
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "92eec3f9c0df7b2d97e06064ff621bfd.png",
            'center': (242, 254),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Flash': [
                self.broadcast_Flash,
            ],
            'broadcast_HeyGuys': [
                self.broadcast_HeyGuys,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Credits': [
                self.broadcast_Credits,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 26

    async def broadcast_Flash(self, util):
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', -20)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def broadcast_HeyGuys(self, util):
        self.xpos = 83
        self.ypos = -61
        self.set_effect('brightness', -20)
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Credits(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite21(engine.Target):
    costume = 25
    xpos, ypos = -39, 90
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "3610afbc81d267acd68141e5d2b413b1.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "7540aabc26e4eecdcae53193ac1a28d2.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "42629c7c3721df70e12ab9cce24ae34c.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "42629c7c3721df70e12ab9cce24ae34c.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "b891fbf221e3504b7ea095d795681b27.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "a97c9d3a5585761bac337c100305a02d.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "fba24422df58df601e020387a442364a.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "fba24422df58df601e020387a442364a.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "b891fbf221e3504b7ea095d795681b27.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "a97c9d3a5585761bac337c100305a02d.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "3545aa2d51c9ef45491339d407154f16.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "520c110b11477def63d8eff8f2f1a9da.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "871538192b9fb7cbfdd3205d7af6bc30.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "d95f69f26c115ac217673795de3e3c24.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "42629c7c3721df70e12ab9cce24ae34c.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "a97c9d3a5585761bac337c100305a02d.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "42629c7c3721df70e12ab9cce24ae34c.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "b891fbf221e3504b7ea095d795681b27.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "871538192b9fb7cbfdd3205d7af6bc30.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "42629c7c3721df70e12ab9cce24ae34c.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "fba24422df58df601e020387a442364a.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "42629c7c3721df70e12ab9cce24ae34c.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "a97c9d3a5585761bac337c100305a02d.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "a97c9d3a5585761bac337c100305a02d.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "7540aabc26e4eecdcae53193ac1a28d2.png",
            'center': (56, 76),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "a1edd1d32209438d1b9a45343e9a6d35.png",
            'center': (40, 56),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "LookWhatIGot",
            'path': "9e16edbe2540029ed9d998d6590bb0d3.wav"
        },
        {
            'name': "Dash",
            'path': "c9a9e79183c87b3c86cd665a1cc84632.wav"
        },
        {
            'name': "LookWhatIGot1",
            'path': "89ab3c76f4b0984f4b31dad7baf2371d.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_HeyGuys': [
                self.broadcast_HeyGuys,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 8

    async def broadcast_HeyGuys(self, util):
        self.xpos = -133
        self.ypos = 99
        self.visible = 1
        pass # sound_play('LookWhatIGot1')
        self.set_costume('costume22')
        self.set_dirty(3)
        for _ in range(23):
            await self.sleep(0.1)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(1)
        self.set_costume('costume26')
        pass # sound_play('Dash')
        await self.glide(0.1, -39, 90)
        self.visible = 0
        self.set_dirty(3)
        await self.sleep(2)
        util.send_event('broadcast_WhatIMiss')


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite22(engine.Target):
    costume = 9
    xpos, ypos = -186, -12
    direction = 85
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "0a47bc0d26cb34b311ef854c903c2755.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "fff866aa215be0be6ab7d790a18c4f51.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "a37cdf75361ae323480a2457a20b45a1.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "a8f78a256605f6a376b756503eb6cacc.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "a6692a5244f10b1f06b6b2b8231e476d.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "fff866aa215be0be6ab7d790a18c4f51.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "f18a77bada77760250b180b08be01aa5.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "77509b0137988c4d081824cf88487d97.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "187b5a30a4b3bdf5c8b15bf7b3c3d65a.png",
            'center': (366, 312),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "8f50393494ebd8a8fa728cd343d44239.png",
            'center': (366, 312),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "MetalBang1",
            'path': "c65d6897a07652fb0269c238c919f625.wav"
        },
        {
            'name': "MetalBang2",
            'path': "9487c49c76158fd86e05316c8e092734.wav"
        },
        {
            'name': "MetalBang3",
            'path': "50e30769e178bb5abd077bc2a4bae0d8.wav"
        },
        {
            'name': "MetalBang4",
            'path': "8e00a874d67269f947795e33845434ad.wav"
        },
        {
            'name': "WhatIMiss",
            'path': "bce16023d8dbc227273a770f043168dd.wav"
        },
        {
            'name': "YouMissed",
            'path': "9c5cc2a6a73b5ade267226fc166c705e.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_Flash': [
                self.broadcast_Flash,
            ],
            'broadcast_WhatIMiss': [
                self.broadcast_WhatIMiss,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_Credits': [
                self.broadcast_Credits,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 27

    async def broadcast_Flash(self, util):
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.01)
        self.set_effect('brightness', -20)
        self.set_dirty(3)
        await self.sleep(0.1)
        self.set_effect('brightness', -10)
        self.set_dirty(3)
        await self.sleep(0.3)
        for _ in range(10):
            await self.sleep(0.01)
            self.change_effect('brightness', -1)
            await self._yield(3)


    async def broadcast_WhatIMiss(self, util):
        self.set_direction(75)
        self.xpos = -166
        self.ypos = -312
        self.set_costume('costume2')
        self.set_effect('brightness', -20)
        self.visible = 1
        self.front_layer(util)
        self.set_direction(105)
        await self.glide(0.8, -132, -141)
        self.set_direction(75)
        await self.glide(0.3, -209, -100)
        pass # sound_play('MetalBang2')
        util.send_event('broadcast_Flash')
        self.set_dirty(3)
        await self.sleep(1)
        self.set_direction(105)
        await self.glide(0.8, -174, -34)
        self.set_direction(85)
        await self.glide(0.3, -186, -12)
        pass # sound_play('MetalBang3')
        self.set_dirty(3)
        await self.sleep(0.5)
        pass # sound_play('WhatIMiss')
        self.set_costume('costume3')
        self.set_dirty(3)
        for _ in range(7):
            await self.sleep(0.07)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(0.5)
        pass # sound_playuntildone('YouMissed')
        await self.sleep(1)
        util.send_event('broadcast_TheEnd')


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_Credits(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite23(engine.Target):
    costume = 0
    xpos, ypos = 0, 0
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "6107c46dcec6e37489e78c09e96edbed.png",
            'center': (480, 360),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "08f59afd55fefac5641b3608fc7af292.png",
            'center': (480, 360),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "Suspense",
            'path': "4797dd003d3c54aa258eaa45a5705916.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_TheEnd': [
                self.broadcast_TheEnd,
                self.broadcast_TheEnd_1,
            ],
            'broadcast_ClickLoveIt': [
                self.broadcast_ClickLoveIt,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 28

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_TheEnd(self, util):
        self.xpos = 0
        self.ypos = 0
        self.set_effect('ghost', 100)
        self.set_effect('brightness', 0)
        self.set_costume('costume1')
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        for _ in range(100):
            await self.sleep(0.05)
            self.change_effect('ghost', -1)
            await self._yield(3)
        await self.sleep(2)
        for _ in range(10):
            await self.sleep(0.07)
            self.change_effect('brightness', -10)
            await self._yield(3)
        self.set_costume('costume2')
        util.send_event('broadcast_Credits')
        self.set_dirty(3)
        for _ in range(10):
            await self.sleep(0.07)
            self.change_effect('brightness', 10)
            await self._yield(3)


    async def broadcast_TheEnd_1(self, util):
        pass # sound_playuntildone('Suspense')


    async def broadcast_ClickLoveIt(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite24(engine.Target):
    costume = 2
    xpos, ypos = 0, 194
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "2a14cdb1b15631b42ccd27d5dac3aecc.png",
            'center': (480, 30),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "7f3d0eb857e413fb7469f19e5c6f7922.png",
            'center': (484, 342),
            'scale': 2
        },
        {
            'name': "costume3",
            'path': "37b0f3f52b2d54486a3afd7aaeae7840.png",
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
            'path': "0bf5a63d8089786a999ca2cf1d0f1ca5.png",
            'center': (476, 364),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "1b5bf8f93574db8015c34546548b6a55.png",
            'center': (530, 342),
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
        self.sprite.layer = 20

    async def broadcast_Credits(self, util):
        self.set_costume('costume1')
        self.xpos = 0
        self.ypos = -180
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        for _ in range(6):
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
        util.send_event('broadcast_ClickLoveIt')
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite25(engine.Target):
    costume = 67
    xpos, ypos = 60, -20
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume3",
            'path': "dc921a6e27c387cc16bdb976f326f7d0.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume4",
            'path': "7f3c991a7942395cc079a1d7bafb5643.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume5",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume6",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume7",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume8",
            'path': "a8159e4301d193ede4227cfbcb154f11.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume9",
            'path': "c1855938df397c03092bcd61bcafd261.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume10",
            'path': "1a73a19b1ef8f817594f7f81fc69a25d.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume11",
            'path': "80b46e9f2182677a72b8c9c4bf624a5b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume12",
            'path': "a101b5d3fab62d7a4496c7a7593bf095.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume13",
            'path': "a8159e4301d193ede4227cfbcb154f11.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume14",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume15",
            'path': "d816b46753cf62d153a073fa5ee7c38c.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume16",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume17",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume18",
            'path': "4131c209068f6240952998d855290833.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume19",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume20",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume21",
            'path': "a8159e4301d193ede4227cfbcb154f11.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume22",
            'path': "c1855938df397c03092bcd61bcafd261.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume23",
            'path': "1a73a19b1ef8f817594f7f81fc69a25d.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume24",
            'path': "7f3c991a7942395cc079a1d7bafb5643.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume25",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume26",
            'path': "80b46e9f2182677a72b8c9c4bf624a5b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume27",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume28",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume30",
            'path': "d816b46753cf62d153a073fa5ee7c38c.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume31",
            'path': "a101b5d3fab62d7a4496c7a7593bf095.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume32",
            'path': "80b46e9f2182677a72b8c9c4bf624a5b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume33",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume34",
            'path': "4131c209068f6240952998d855290833.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume35",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume36",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume37",
            'path': "b28727635c60e765823366571e464403.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume38",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume41",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume42",
            'path': "4131c209068f6240952998d855290833.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume43",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume44",
            'path': "c9f0a1a054ff47ad1fdf717b719bd9a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume45",
            'path': "b28727635c60e765823366571e464403.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume46",
            'path': "a101b5d3fab62d7a4496c7a7593bf095.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume47",
            'path': "c9f0a1a054ff47ad1fdf717b719bd9a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume48",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume50",
            'path': "c1855938df397c03092bcd61bcafd261.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume52",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume53",
            'path': "a101b5d3fab62d7a4496c7a7593bf095.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume54",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume55",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume56",
            'path': "b28727635c60e765823366571e464403.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume57",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume58",
            'path': "c1855938df397c03092bcd61bcafd261.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume59",
            'path': "1a73a19b1ef8f817594f7f81fc69a25d.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume60",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume61",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume62",
            'path': "c9f0a1a054ff47ad1fdf717b719bd9a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume63",
            'path': "7f3c991a7942395cc079a1d7bafb5643.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume64",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume65",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume66",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume67",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume68",
            'path': "80b46e9f2182677a72b8c9c4bf624a5b.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume69",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume70",
            'path': "ad2e05f9b51e5d91723b0783c53648a2.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume71",
            'path': "96ac2fce34e0ba6ea063644922a50a6e.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume72",
            'path': "dedc6e0dc9644cfe89bfbe4763943642.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume73",
            'path': "a101b5d3fab62d7a4496c7a7593bf095.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume74",
            'path': "a8159e4301d193ede4227cfbcb154f11.png",
            'center': (330, 260),
            'scale': 2
        },
        {
            'name': "costume75",
            'path': "b28727635c60e765823366571e464403.png",
            'center': (330, 260),
            'scale': 2
        },
    ]

    sounds = [
        {
            'name': "whoosh",
            'path': "6394551b397c5a9669d02786b4d8e91d.wav"
        },
        {
            'name': "DidYouLikeThis",
            'path': "c97dfe4cb15e100284b1193e97c76a17.wav"
        },
        {
            'name': "ClickLoveIt",
            'path': "d3131176dc57bf52960888ad721a52bc.wav"
        },
        {
            'name': "UntilNextTime",
            'path': "923ea30288c95fe0b1f589c3c0e13563.wav"
        },
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_ClickLoveIt': [
                self.broadcast_ClickLoveIt,
            ],
            'green_flag': [
                self.green_flag,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 10

    async def broadcast_ClickLoveIt(self, util):
        pass # sound_stopallsounds()
        self.set_costume('costume4')
        self.visible = 1
        self.xpos = 60
        self.ypos = -336
        pass # sound_play('whoosh')
        await self.glide(0.3, 60, -20)
        self.set_dirty(3)
        await self.sleep(1)
        pass # sound_play('DidYouLikeThis')
        self.set_costume('costume5')
        self.set_dirty(3)
        for _ in range(19):
            await self.sleep(0.07)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(1)
        self.set_costume('costume24')
        pass # sound_play('ClickLoveIt')
        self.set_dirty(3)
        for _ in range(34):
            await self.sleep(0.06)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(1)
        pass # sound_play('UntilNextTime')
        self.set_costume('costume64')
        self.set_dirty(3)
        for _ in range(11):
            await self.sleep(0.08)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)
        await self.sleep(1)
        util.send_event('broadcast_WitchDoctor')
        self.visible = 0
        self.set_dirty(1)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite26(engine.Target):
    costume = 1
    xpos, ypos = -97, -60
    direction = 70
    visible = False

    costumes = [
        {
            'name': "costume1",
            'path': "3ba619eb5cff9bf2360806ae7a88c952.png",
            'center': (120, 146),
            'scale': 2
        },
        {
            'name': "costume2",
            'path': "7da90a62ccbbbf301e1c1c5395a70161.png",
            'center': (76, 48),
            'scale': 2
        },
    ]

    sounds = [
    ]

    def __init__(self, util):
        self.hats = {
            'broadcast_ClickLoveIt': [
                self.broadcast_ClickLoveIt,
            ],
            'green_flag': [
                self.green_flag,
            ],
            'broadcast_WitchDoctor': [
                self.broadcast_WitchDoctor,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 11

    async def broadcast_ClickLoveIt(self, util):
        self.set_costume('costume2')
        self.xpos = -97
        self.ypos = -205
        self.visible = 1
        self.set_dirty(3)
        await self.sleep(0.1)
        await self.glide(0.15, -97, -60)
        self.set_dirty(2)


    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WitchDoctor(self, util):
        self.visible = 0
        self.set_dirty(1)



class Sprite27(engine.Target):
    costume = 7
    xpos, ypos = 215, -38
    direction = 90
    visible = False

    costumes = [
        {
            'name': "troll-dance",
            'path': "3c3f00001c04588cb25ad437255bc960.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance1",
            'path': "35925bbfa3e9db689a7a64c81e63a637.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance2",
            'path': "2499d65f61106eb99c18aee5db37c29a.png",
            'center': (238, 334),
            'scale': 2
        },
        {
            'name': "troll-dance3",
            'path': "4bb0f55cbff875bafbe35b1750171047.png",
            'center': (282, 312),
            'scale': 2
        },
        {
            'name': "troll-dance4",
            'path': "22252ae4d0bbcd7d734eb96576a746bc.png",
            'center': (308, 354),
            'scale': 2
        },
        {
            'name': "troll-dance5",
            'path': "a8cbd0e34d5d8e717ed4b6d0d03abb92.png",
            'center': (324, 360),
            'scale': 2
        },
        {
            'name': "troll-dance6",
            'path': "adc49d22eecb6090f51494d4e6d43c45.png",
            'center': (336, 360),
            'scale': 2
        },
        {
            'name': "troll-dance7",
            'path': "ba10f4ecf2a5039a826ea8d938a0470f.png",
            'center': (312, 336),
            'scale': 2
        },
        {
            'name': "troll-dance8",
            'path': "c39761c98989b24b74a3be3767e2adfc.png",
            'center': (268, 302),
            'scale': 2
        },
        {
            'name': "troll-dance9",
            'path': "90eb421eaaae34f103d4898f75010465.png",
            'center': (238, 310),
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
            'broadcast_WitchDoctor': [
                self.broadcast_WitchDoctor,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 12

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WitchDoctor(self, util):
        self.xpos = 215
        self.ypos = -38
        self.set_direction(90)
        self.set_costume('troll-dance')
        self.visible = 1
        self.set_dirty(3)
        while True:
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)



class Sprite28(engine.Target):
    costume = 7
    xpos, ypos = -215, -38
    direction = -90
    visible = False

    costumes = [
        {
            'name': "troll-dance",
            'path': "3c3f00001c04588cb25ad437255bc960.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance1",
            'path': "35925bbfa3e9db689a7a64c81e63a637.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance2",
            'path': "2499d65f61106eb99c18aee5db37c29a.png",
            'center': (238, 334),
            'scale': 2
        },
        {
            'name': "troll-dance3",
            'path': "4bb0f55cbff875bafbe35b1750171047.png",
            'center': (282, 312),
            'scale': 2
        },
        {
            'name': "troll-dance4",
            'path': "22252ae4d0bbcd7d734eb96576a746bc.png",
            'center': (308, 354),
            'scale': 2
        },
        {
            'name': "troll-dance5",
            'path': "a8cbd0e34d5d8e717ed4b6d0d03abb92.png",
            'center': (324, 360),
            'scale': 2
        },
        {
            'name': "troll-dance6",
            'path': "adc49d22eecb6090f51494d4e6d43c45.png",
            'center': (336, 360),
            'scale': 2
        },
        {
            'name': "troll-dance7",
            'path': "ba10f4ecf2a5039a826ea8d938a0470f.png",
            'center': (312, 336),
            'scale': 2
        },
        {
            'name': "troll-dance8",
            'path': "c39761c98989b24b74a3be3767e2adfc.png",
            'center': (268, 302),
            'scale': 2
        },
        {
            'name': "troll-dance9",
            'path': "90eb421eaaae34f103d4898f75010465.png",
            'center': (238, 310),
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
            'broadcast_WitchDoctor': [
                self.broadcast_WitchDoctor,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 13

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WitchDoctor(self, util):
        self.xpos = -215
        self.ypos = -38
        self.set_direction(-90)
        self.set_costume('troll-dance')
        self.visible = 1
        self.set_dirty(3)
        while True:
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)



class Sprite29(engine.Target):
    costume = 7
    xpos, ypos = 0, -38
    direction = -90
    visible = False

    costumes = [
        {
            'name': "troll-dance",
            'path': "3c3f00001c04588cb25ad437255bc960.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance1",
            'path': "35925bbfa3e9db689a7a64c81e63a637.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance2",
            'path': "2499d65f61106eb99c18aee5db37c29a.png",
            'center': (238, 334),
            'scale': 2
        },
        {
            'name': "troll-dance3",
            'path': "4bb0f55cbff875bafbe35b1750171047.png",
            'center': (282, 312),
            'scale': 2
        },
        {
            'name': "troll-dance4",
            'path': "22252ae4d0bbcd7d734eb96576a746bc.png",
            'center': (308, 354),
            'scale': 2
        },
        {
            'name': "troll-dance5",
            'path': "a8cbd0e34d5d8e717ed4b6d0d03abb92.png",
            'center': (324, 360),
            'scale': 2
        },
        {
            'name': "troll-dance6",
            'path': "adc49d22eecb6090f51494d4e6d43c45.png",
            'center': (336, 360),
            'scale': 2
        },
        {
            'name': "troll-dance7",
            'path': "ba10f4ecf2a5039a826ea8d938a0470f.png",
            'center': (312, 336),
            'scale': 2
        },
        {
            'name': "troll-dance8",
            'path': "c39761c98989b24b74a3be3767e2adfc.png",
            'center': (268, 302),
            'scale': 2
        },
        {
            'name': "troll-dance9",
            'path': "90eb421eaaae34f103d4898f75010465.png",
            'center': (238, 310),
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
            'broadcast_WitchDoctor': [
                self.broadcast_WitchDoctor,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 21

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WitchDoctor(self, util):
        self.xpos = 0
        self.ypos = -38
        self.set_direction(-90)
        self.set_costume('troll-dance')
        self.visible = 1
        self.front_layer(util)
        self.set_dirty(3)
        while True:
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)



class Sprite30(engine.Target):
    costume = 7
    xpos, ypos = -110, -141
    direction = -90
    visible = False

    costumes = [
        {
            'name': "troll-dance",
            'path': "3c3f00001c04588cb25ad437255bc960.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance1",
            'path': "35925bbfa3e9db689a7a64c81e63a637.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance2",
            'path': "2499d65f61106eb99c18aee5db37c29a.png",
            'center': (238, 334),
            'scale': 2
        },
        {
            'name': "troll-dance3",
            'path': "4bb0f55cbff875bafbe35b1750171047.png",
            'center': (282, 312),
            'scale': 2
        },
        {
            'name': "troll-dance4",
            'path': "22252ae4d0bbcd7d734eb96576a746bc.png",
            'center': (308, 354),
            'scale': 2
        },
        {
            'name': "troll-dance5",
            'path': "a8cbd0e34d5d8e717ed4b6d0d03abb92.png",
            'center': (324, 360),
            'scale': 2
        },
        {
            'name': "troll-dance6",
            'path': "adc49d22eecb6090f51494d4e6d43c45.png",
            'center': (336, 360),
            'scale': 2
        },
        {
            'name': "troll-dance7",
            'path': "ba10f4ecf2a5039a826ea8d938a0470f.png",
            'center': (312, 336),
            'scale': 2
        },
        {
            'name': "troll-dance8",
            'path': "c39761c98989b24b74a3be3767e2adfc.png",
            'center': (268, 302),
            'scale': 2
        },
        {
            'name': "troll-dance9",
            'path': "90eb421eaaae34f103d4898f75010465.png",
            'center': (238, 310),
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
            'broadcast_WitchDoctor': [
                self.broadcast_WitchDoctor,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 17

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WitchDoctor(self, util):
        self.xpos = -110
        self.ypos = -141
        self.set_direction(-90)
        self.set_costume('troll-dance')
        self.visible = 1
        self.set_dirty(3)
        while True:
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)



class Sprite31(engine.Target):
    costume = 7
    xpos, ypos = 110, -141
    direction = 90
    visible = False

    costumes = [
        {
            'name': "troll-dance",
            'path': "3c3f00001c04588cb25ad437255bc960.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance1",
            'path': "35925bbfa3e9db689a7a64c81e63a637.png",
            'center': (218, 360),
            'scale': 2
        },
        {
            'name': "troll-dance2",
            'path': "2499d65f61106eb99c18aee5db37c29a.png",
            'center': (238, 334),
            'scale': 2
        },
        {
            'name': "troll-dance3",
            'path': "4bb0f55cbff875bafbe35b1750171047.png",
            'center': (282, 312),
            'scale': 2
        },
        {
            'name': "troll-dance4",
            'path': "22252ae4d0bbcd7d734eb96576a746bc.png",
            'center': (308, 354),
            'scale': 2
        },
        {
            'name': "troll-dance5",
            'path': "a8cbd0e34d5d8e717ed4b6d0d03abb92.png",
            'center': (324, 360),
            'scale': 2
        },
        {
            'name': "troll-dance6",
            'path': "adc49d22eecb6090f51494d4e6d43c45.png",
            'center': (336, 360),
            'scale': 2
        },
        {
            'name': "troll-dance7",
            'path': "ba10f4ecf2a5039a826ea8d938a0470f.png",
            'center': (312, 336),
            'scale': 2
        },
        {
            'name': "troll-dance8",
            'path': "c39761c98989b24b74a3be3767e2adfc.png",
            'center': (268, 302),
            'scale': 2
        },
        {
            'name': "troll-dance9",
            'path': "90eb421eaaae34f103d4898f75010465.png",
            'center': (238, 310),
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
            'broadcast_WitchDoctor': [
                self.broadcast_WitchDoctor,
            ],
        }
        super().__init__(util)
        self.sprite.layer = 18

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)


    async def broadcast_WitchDoctor(self, util):
        self.xpos = 110
        self.ypos = -141
        self.set_direction(90)
        self.set_costume('troll-dance')
        self.visible = 1
        self.set_dirty(3)
        while True:
            await self.sleep(0.05)
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.set_costume(0)
            else:
                self.set_costume(next_costume)
            await self._yield(3)



class Sprite32(engine.Target):
    costume = 0
    xpos, ypos = 0, 0
    direction = 90
    visible = False

    costumes = [
        {
            'name': "costume2",
            'path': "6198baa69c42985d5eeaa4930706111f.png",
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
        self.sprite.layer = 22

    async def green_flag(self, util):
        self.visible = 0
        self.set_dirty(1)

SPRITES = {
    'Stage': Stage,
    'title': title,
    'play': play,
    'Sprite3': Sprite3,
    'Sprite4': Sprite4,
    'Sprite1': Sprite1,
    'Sprite5': Sprite5,
    'Sprite6': Sprite6,
    'Sprite7': Sprite7,
    'Sprite8': Sprite8,
    'Sprite11': Sprite11,
    'Sprite9': Sprite9,
    'Sprite10': Sprite10,
    'Sprite15': Sprite15,
    'Sprite12': Sprite12,
    'Sprite13': Sprite13,
    'Sprite14': Sprite14,
    'Sprite17': Sprite17,
    'Sprite18': Sprite18,
    'Sprite19': Sprite19,
    'Sprite20': Sprite20,
    'Sprite21': Sprite21,
    'Sprite22': Sprite22,
    'Sprite23': Sprite23,
    'Sprite24': Sprite24,
    'Sprite25': Sprite25,
    'Sprite26': Sprite26,
    'Sprite27': Sprite27,
    'Sprite28': Sprite28,
    'Sprite29': Sprite29,
    'Sprite30': Sprite30,
    'Sprite31': Sprite31,
    'Sprite32': Sprite32,
}

if __name__ == '__main__':
    engine.main(SPRITES)
