from my_sprite import MySprite
from box import Box
from colors import Color
from text import Text
from image_sprite import ImageSprite
from target import Target

if __name__ == "__main__":
    from window import Window
    import pygame
    from random import randint

    pygame.init()

    window = Window("Aim Trainer")

    bg_img = ImageSprite("assets/background.png")
    bg_img.setScale(3, 1.7)

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth()//2-crosshair.getWidth()//2, window.getVirtualHeight()//2-crosshair.getHeight()//2)

    targets = []
    for i in range(3):
        target = Target("assets/target.png", 0, 0, speed=0.3)
        target.setScale(0.1)
        target.setPosition(randint(0, window.getVirtualWidth() - target.getWidth()),
                           randint(0, window.getVirtualHeight() - target.getHeight()))
        targets.append(target)

    pygame.mouse.set_pos(window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)
    pygame.mouse.set_visible(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                # Get mouse movement
                mouse_x, mouse_y = event.rel
                for target in targets:
                    target.x += mouse_x*target.speed
                    target.y += mouse_y*target.speed
                # Center the mouse cursor again
                pygame.mouse.set_pos(window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for target in targets:
                    if target.isCollision(25, 25, (window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)):
                        target.setPosition(randint(0, window.getVirtualWidth() - target.getWidth()),
                           randint(0, window.getVirtualHeight() - target.getHeight()))


        keys_pressed = pygame.key.get_pressed()

        for target in targets:
            target.WASDMove(keys_pressed)

        window.clearScreen()
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        for target in targets:
            window.getScreen().blit(target.getSurface(), target.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        window.updateFrame()
