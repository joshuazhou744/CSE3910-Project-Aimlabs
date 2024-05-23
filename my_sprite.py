'''
title: my sprite abstract class
author: kevin li
date-created: 2024-05-14
'''
import pygame

class MySprite:
    '''
    abstract sprite class to build other sprites
    '''

    def __init__(self, width=0, height=0, x=0, y=0, speed=10):
        self.width = width
        self.height = height
        self.dimensions = (self.width, self.height)
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.surface = pygame.Surface
        self.speed = speed
        self.dir_x = 1
        self.dir_y = 1

    # modifier methods (setter methods)
    def marqueeX(self, max_x, min_x=0):
        self.x += self.speed

        if self.x > max_x:
            self.x = min_x - self.surface.getwidth()

        self.updatePosition()

    def WASDMove(self, pressed_keys):
        if pressed_keys[pygame.K_d]:
            self.x += self.speed
        if pressed_keys[pygame.K_a]:
            self.x -= self.speed
        if pressed_keys[pygame.K_w]:
            self.y += self.speed
        if pressed_keys[pygame.K_s]:
            self.y -= self.speed
        self.updatePosition()

    def wrapEdge(self, max_width, max_height, min_width=0, min_height=0):
        if self.x > max_width:
            self.x = min_width - self.surface.get_width()
        elif self.x < min_width - self.surface.get_width():
            self.x = max_width - self.surface.get_width()

        if self.y > max_height:
            self.y = min_height - self.surface.get_height()
        elif self.y < min_height - self.surface.get_height():
            self.y = max_height - self.surface.get_height()
    def setSpeed(self, new_speed):
        self.speed = new_speed

    def setX(self, x):
        self.x = x
        self.updatePosition()

    def setY(self, y):
        self.y = y
        self.updatePosition()
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        # self.position = (self.x, self.y)
        self.updatePosition()

    def updatePosition(self):
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
