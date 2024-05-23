from my_sprite import MySprite
from colors import Color
import pygame

class Box(MySprite):
    def __init__(self, width=1, height=1, x=0, y=0, speed=10):
        MySprite.__init__(self, width=width, height=height, x=x, y=y, speed=speed)
        self.color = Color.red
        self.surface = pygame.Surface(self.dimensions, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def setColor(self, new_color):
        MySprite.setColor(self, new_color)
        self.surface.fill(self.color)