import pygame
from colors import Color
class Window:
    '''
    create window that will load for pygame
    return None
    '''
    def __init__(self, title, width=800, height=600, fps=30):
        self.title = title # text in title bar
        self.width = width # width of window
        self.height = height # height of window
        self.dimensions = (self.width, self.height) # window dimensions
        self.fps = fps # frames per second
        self.bg_color = Color.grey # dark grey color
        self.clock = pygame.time.Clock()  # clock that tracks time
        self.screen = pygame.display.set_mode(self.dimensions) # base surface all surfaces are overlaid on top
        self.screen.fill(self.bg_color) # colors screen surface with color
        pygame.display.set_caption(self.title)

    def getScreen(self):
        return self.screen

    def getVirtualWidth(self):
        return self.width

    def getVirtualHeight(self):
        return self.height

    def updateFrame(self):
        '''
        update the window obj based on the fps
        :return: none
        '''
        self.clock.tick(self.fps) # waits the appropriate amount of time for updated frame
        pygame.display.flip() # update window with new frame

    def clearScreen(self):
        '''
        fill the screen with the bg color
        :return: none
        '''
        self.screen.fill(self.bg_color)