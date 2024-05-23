from my_sprite import MySprite
from box import Box
from colors import Color
from text import Text
from image_sprite import ImageSprite

if __name__ == "__main__":
    from window import Window
    import pygame
    from random import randint

    pygame.init()

    window = Window("Aim Trainer")

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth()//2-crosshair.getWidth()//2, window.getVirtualHeight()//2-crosshair.getHeight()//2)

    boxes = []
    for i in range(3):
        boxes.append(Box(10,10, randint(0,window.getVirtualWidth()), randint(0,window.getVirtualHeight())))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys_pressed = pygame.key.get_pressed()

        for box in boxes:
            box.WASDMove(keys_pressed)
            box.wrapEdge(window.getVirtualWidth(), window.getVirtualHeight())

        window.clearScreen()
        for box in boxes:
            window.getScreen().blit(box.getSurface(), box.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        window.updateFrame()
