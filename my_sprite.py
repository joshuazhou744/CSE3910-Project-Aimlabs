'''
title: my sprite abstract class
author: kevin li
date-created: 2024-05-14
'''
import pygame
from colors import Color

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
        self.surface = pygame.Surface
        self.speed = speed
        self.dir_x = 1
        self.dir_y = 1
        self.color = color

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

    def stopAtEdge(self, max_width, min_width, max_height, min_height):
        if self.x > (max_width-self.getWidth()):
            self.x = max_width-self.getWidth()
        elif self.x < min_width:
            self.x = min_width
        if self.y > (max_height-self.getHeight()):
            self.y = max_height-self.getHeight()
        elif self.y < min_height:
            self.y = min_height
        self.setPosition(self.x, self.y)

    def wrapEdge(self, max_width, min_width, max_height, min_height):
        if self.x > (max_width - self.getWidth()):
            self.x = min_width
        elif self.x < min_width:
            self.x = max_width
        if self.y > (max_height - self.getHeight()):
            self.y = min_height
        elif self.y < min_height:
            self.y = max_height
        self.setPosition(self.x, self.y)

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

    def isCollision(self, WIDTH, HEIGHT, POSITION):
        '''
        use the width, height, and position of an external sprite to test if it is colliding with the given sprite
        :param WIDTH: int
        :param HEIGHT: int
        :param POSITION: tuple
        '''

        if POSITION[0] >= self.x - WIDTH and POSITION[0] <= self.x + self.getWidth() and POSITION[1] >= self.y - HEIGHT and POSITION[1] <= self.y + self.getHeight():
            return True
        else:
            return False
