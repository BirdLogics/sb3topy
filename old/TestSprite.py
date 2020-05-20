#pylint:disable=all
import asyncio
import pygame


class Target:
    name = ""
    costumes = []
    sounds = []
    clones = []

    x = 0
    y = 0
    size = 100
    direction = 0
    draggable = False
    currentCostume = None
    #costume = costumes[currentCostume]
    costumeCount = len(costumes)
    visible = True
    rotationStyle = "all around"
    variables = {}
    lists = {}
    costumes = {}
    sounds = {}
    #textToSpeechLanguage
    #tempo
    #volume
    #videoTransparency
    #videoState

    sprite = None

    def __init__(self, parent={}):
        if parent:
            self.isClone = True
            # Gets either the value in parent or a default value
            #default = lambda k, d: k in parent and parent[k] or d

            # These are linked to the parent
            self.costumes = parent.costumes
            self.sounds = parent.sounds
            self.clones = parent.clones

            # These are not linked
            self.name = parent.name
            self.x = parent.x
            self.y = parent.y
            self.size = parent.size
            self.direction = parent.direction
            self.draggable = parent.draggable
            self.currentCostume = parent.currentCostume
            self.costume = self.costumes[self.currentCostume]
            self.costumeCount = len(self.costumes)
            self.visible = parent.visible
            self.rotationStyle = parent.rotationStyle

            # Copy to prevent linking
            self.variables = parent.variables.copy()
            self.lists = []
            for name, list in parent.lists.items():
                self.lists[name] = list.copy()
    
    def switchCostume(self, name):
        if name in self.costumes:
            self.costume = self.costumes[name]
            self.sprite.rect = self.costume.get_rect()
            self.updatePosition()
    
    def setSize(self, value):
        raise NotImplementedError()
    
    def updatePosition(self):
        self.sprite.rect


class Sprite_sprite1(Target):
    def __init__(self, parent={}):
        if parent:
            super().__init__(parent)
        else:
            self.name = "Cat"

            # Prepare costumes for loading
            self.costumes = {
                "costume1":"asset1.png",
                "costume2":"asset2.png",
            }

            # Prepare sounds for loading
            self.sounds = {
                "Meow":"asset3.wav"
            }

            # Create a pygame sprite
            self.sprite = pygame.sprite.Sprite()

            # Load costumes
            for name, fn in self.costumes.items():
                self.costumes[name] = pygame.image.load("assets/" + fn)
            self.switchCostume(self.currentCostume)
            
            # Load sounds
            for name, fn in self.sounds.items():
                self.sounds[name] = pygame.mixer.Sound("assets/" + fn)
    
    async def block_Flag1(self):
        while True:
            self.x += 10
            self.direction += 1
            
            await asyncio.sleep(0)