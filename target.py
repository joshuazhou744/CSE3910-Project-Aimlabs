'''
title: target class
date-created: 5/23/2024
author: kevin li
'''
from my_sprite import MySprite
from image_sprite import ImageSprite
import pygame
from colors import Color

class Target(ImageSprite):
    def __init__(self, image_file_location, radius=1, x=1, y=1, speed=1):
        ImageSprite.__init__(self, image_file_location=image_file_location)
        MySprite.__init__(self, x=x, y=y, speed=speed)
        self.color = Color.red
        self.radius = radius
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.is_clicked = False
        self.is_x_mouse_over = False
        self.is_y_mouse_over = False
        self.is_mouse_over = False

    def setRadius(self, radius):
        self.radius = radius

    def checkMouseOver(self):
        '''
        detects if the mouse is hovering over the object
        :return: None
        '''
        if self.x < self.mouse_x < self.x + self.radius*2:
            self.is_x_mouse_over = True
        else:
            self.is_x_mouse_over = False

        if self.y < self.mouse_y < self.y + self.radius*2:
            self.is_y_mouse_over = True
        else:
            self.is_y_mouse_over = False

        if self.is_y_mouse_over and self.is_x_mouse_over:
            self.is_mouse_over = True
        else:
            self.is_mouse_over = False

    def isClicked(self, event_list):
        for event in event_list:
            self.checkMouseOver()
            if self.is_mouse_over and event == pygame.MOUSEBUTTONDOWN:
                self.is_clicked = True
        else:
            self.is_clicked = False








