'''
title: flash class
author: joshua z
date-created: 2024-06-03
'''
import time

import pygame.time
import pygame
class Flash:
    def __init__(self):
        self.sight_time = 2000

    def flash_image(self, window, flash_img):
        window.clearScreen()
        window.getScreen().blit(flash_img.getSurface(), flash_img.getPosition())
        pygame.display.update()

    def updateTime(self):
        self.sight_time -= 50