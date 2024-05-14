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
        self._width = width
        self._height = height
        self._dimensions = (self._width, self._height)
        self._x = x
        self._y = y
        self._position = (self._x, self._y)
        self._color = color
        self._surface = pygame.Surface
        self._speed = speed
        self._dir_x = 1
        self._dir_y = 1

    # modifier methods (setter methods)
    def marqueeX(self, max_x, min_x=0):
        self._x += self._speed

        if self._x > max_x:
            self._x = min_x - self._surface.get_width()

        self.__updatePosition()

    def WASDMove(self, pressed_keys):
        if pressed_keys[pygame.K_d]:
            self._x += self._speed
        if pressed_keys[pygame.K_a]:
            self._x -= self._speed
        if pressed_keys[pygame.K_w]:
            self._y += self._speed
        if pressed_keys[pygame.K_s]:
            self._y -= self._speed
        self.__updatePosition()
    def setSpeed(self, new_speed):
        self._speed = new_speed
    def setColor(self, new_color):
        '''
        this only changes the variable, it does not change the surface
        :param new_color:
        :return:
        '''
        self._color = new_color
    def setX(self, x):
        self._x = x
        self.__updatePosition()

    def setY(self, y):
        self._y = y
        self.__updatePosition()
    def setPosition(self, x, y):
        self._x = x
        self._y = y
        # self.__position = (self.__x, self.__y)
        self.__updatePosition()

    def __updatePosition(self):
        self._position = (self._x, self._y)
        self.rect = pygame.Rect(self._x, self._y, self._width, self._height)


    # accessor methods (getter methods)
    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height
    def getSurface(self):
        return self._surface

    def getPosition(self):
        return self._position
