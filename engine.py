"""

"""

from pygame.sprite import DirtySprite
from pygame import transform
from pygame.math import Vector2


class SpriteBase(DirtySprite):
    """Holds the base sprite"""
    rect = None
    image = None
    visible = 1
    dirty = 0

    variable = {}
    lists = {}

    costumes = {}
    sounds = {}
    xpos, ypos = 0, 0
    direction = 90
    #draggable = False
    #visible = True
    size = 100
    current_costume = 0

    # rotationStyle
    #volume = 100
    #tempo = 60
    #videoTransparency = 50
    # videoState
    # textToSpeechLanguage

    def set_direction(self, degrees):
        """Sets and wraps the direction"""
        self.direction = degrees - ((degrees + 179) // 360 * 360)

    def update_image(self):
        """Updates and transforms the sprites image"""
        self.image = transform.rotozoom(
            self.costumes[self.current_costume], -self.direction, self.size/100)
        self.update_rect()

    def update_rect(self):
        """Updates the rect to match the sprite's position and orientation"""
        offset = self.costumes[self.current_costume]["offset"].rotate(
            self.direction)
        self.rect = self.image.get_rect(
            center=offset + Vector2(self.x, self.y))

    def switch_costume(self, costume):
        """Switches the costume based on a name or number"""
        raise NotImplementedError
