'''
title: gridshot
author: joshua z
date-created: 2024-03-30
'''

from target import Target
from random import randint
from image_sprite import ImageSprite
from text import Text
class Score:
    def __init__(self):
        self.shots = 0
        self.hits = 0
        self.accuracy = 0

    def updateAccuracy(self):
        if self.shots != 0:
            self.accuracy = f"{self.hits/self.shots :.0%}"
