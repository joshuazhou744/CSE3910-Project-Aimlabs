import pygame
from MySprite import MySprite

class ImageSprite(MySprite):

    def __init__(self, image_file_location):
        MySprite.__init__(self)
        self.file_location = image_file_location
        self.surface = pygame.image.load(self.file_location).convert_alpha() # works with pngs only
        self.image_dir_x = True
    def WASDMove(self, pressed_keys):
        # Polymorphism example of modifying the WASDMove() method
        MySprite.WASDMove(self, pressed_keys)
        if pressed_keys[pygame.K_a] and self.image_dir_x:
            # if a key is pressed and image is looking to the right
            self.surface = pygame.transform.flip(self.surface, True, False)
            self.image_dir_x = False
        if pressed_keys[pygame.K_d] and not self.image_dir_x:
            # if d key is pressed nad image is looking to the left
            self.surface = pygame.transform.flip(self.surface, True, False)
            self.image_dir_x = True
    def getWidth(self):
        return self.surface.get_width()

    def getHeight(self):
        return self._surface.get_height()

