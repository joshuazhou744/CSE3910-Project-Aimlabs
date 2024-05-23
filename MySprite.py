'''
title: my sprite abstract class
author: kevin li
date-created: 2024-05-14
'''
from colors import Color
import pygame

class MySprite:
    '''
    abstract sprite class to build other sprites
    '''

    def __init__(self, width=0, height=0, x=0, y=0, speed=10, color=Color.white):
        self.width = width
        self.height = height
        self.dimensions = (self.width, self.height)
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.color = color
        self.surface = pygame.Surface
        self.speed = speed
        self.dir_x = 1
        self.dir_y = 1

    # modifier methods (setter methods)
    def marqueeX(self, max_x, min_x=0):
        self.x += self.speed

        if self.x > max_x:
            self.x = min_x - self.surface.get_width()

        self.__updatePosition()

    def WASDMove(self, pressed_keys):
        if pressed_keys[pygame.K_d]:
            self.x += self.speed
        if pressed_keys[pygame.K_a]:
            self.x -= self.speed
        if pressed_keys[pygame.K_w]:
            self.y += self.speed
        if pressed_keys[pygame.K_s]:
            self.y -= self.speed
        self.__updatePosition()
    def setSpeed(self, new_speed):
        self.speed = new_speed
    def setColor(self, new_color):
        '''
        this only changes the variable, it does not change the surface
        :param new_color:
        :return:
        '''
        self.color = new_color
    def setX(self, x):
        self.x = x
        self.__updatePosition()

    def setY(self, y):
        self.y = y
        self.__updatePosition()
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        # self.__position = (self.__x, self.__y)
        self.__updatePosition()

    def __updatePosition(self):
        self.position = (self.x, self.y)



    # accessor methods (getter methods)
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def getSurface(self):
        return self.surface

    def getPosition(self):
        return self.position
