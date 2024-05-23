'''
title: target class
date-created: 5/23/2024
author: kevin li
'''
from my_sprite import MySprite
import pygame

class Target(MySprite):
    def __init__(self, radius=1):
        MySprite.__init__(self)
        self.radius = radius
        self.surface = pygame.Surface(self.dimensions, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
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

    def isClicked(self, keys_pressed):
        self.checkMouseOver()
        if self.is_mouse_over and pygame.MOUSEBUTTONDOWN:
            self.is_clicked = True
        else:
            self.is_clicked = False






