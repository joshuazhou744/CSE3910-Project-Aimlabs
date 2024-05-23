import pygame
from my_sprite import MySprite

class ImageSprite(MySprite):

    def __init__(self, image_file_location):
        MySprite.__init__(self)
        self.file_location = image_file_location
        self.surface = pygame.image.load(self.file_location).convert_alpha() # works with pngs only
        self.image_dir_x = True

    def setScale(self, scaleX, scaleY=None):
        if scaleY == None:
            scaleY = scaleX
        self.surface = pygame.transform.scale(self.surface, (self.getWidth()*scaleX, self.getHeight()*scaleY))
    def getWidth(self):
        return self.surface.get_width()

    def getHeight(self):
        return self.surface.get_height()

