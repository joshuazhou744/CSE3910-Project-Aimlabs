from my_sprite import MySprite
import pygame
class Text(MySprite):
    def __init__(self, text, font_family = "Arial", font_size=36, x=0, y=0, font=0, color=0):
        MySprite.__init__(self, x=x, y=y, color=color)
        self.font_family = font_family
        self.font_size = font_size
        self.font = font
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)

    def setText(self,text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)