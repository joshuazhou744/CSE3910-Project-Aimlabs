from random import randrange
class Color:
    white = (255, 255, 255)
    grey = (50, 50, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (255, 145, 0)
    purple = (175, 25, 255)

    @staticmethod
    def getRandom():
        return (randrange(256), randrange(256), randrange(256))