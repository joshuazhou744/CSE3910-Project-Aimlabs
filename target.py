'''
title: target class
date-created: 5/23/2024
author: kevin li
'''
from my_sprite import MySprite
from image_sprite import ImageSprite
import pygame
from colors import Color

class Target(MySprite):
    def __init__(self, image_file_location, x=1, y=1, speed=1):
        MySprite.__init__(self, x=x, y=y, speed=speed)
        self.file_location = image_file_location
        self.surface = pygame.image.load(self.file_location).convert_alpha()  # works with pngs only
        self.image_dir_x = True
        self.color = Color.red
        self.is_clicked = False
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.is_x_mouse_over = False
        self.is_y_mouse_over = False
        self.is_mouse_over = False

    def setScale(self, scaleX, scaleY=None):
        if scaleY == None:
            scaleY = scaleX
        self.surface = pygame.transform.scale(self.surface, (self.getWidth() * scaleX, self.getHeight() * scaleY))

    def checkMouseOver(self, mouse_position):
        '''
        detects if the mouse is hovering over the object
        :return: None
        '''
        self.mouse_x, self.mouse_y = mouse_position
        if self.x < self.mouse_x < self.x + self.width*2:
            self.is_x_mouse_over = True
        else:
            self.is_x_mouse_over = False

        if self.y < self.mouse_y < self.y + self.height*2:
            self.is_y_mouse_over = True
        else:
            self.is_y_mouse_over = False

        if self.is_y_mouse_over and self.is_x_mouse_over:
            self.is_mouse_over = True
        else:
            self.is_mouse_over = False

    def checkClicked(self, event_list, mouse_position):
        for event in event_list:
            self.checkMouseOver(mouse_position)
            if self.is_mouse_over and event == pygame.MOUSEBUTTONDOWN:
                self.is_clicked = True
        else:
            self.is_clicked = False

    def getWidth(self):
        return self.surface.get_width()

    def getHeight(self):
        return self.surface.get_height()







