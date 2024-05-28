from target import Target
import pygame
from window import Window
from image_sprite import ImageSprite
from box import Box
from random import *

if __name__ == '__main__':
    pygame.init()

    window = Window("Aim Trainer")

    bg_img = ImageSprite("assets/background.png")
    bg_img.setScale(3, 1.7)

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth() // 2 - crosshair.getWidth() // 2,
                          window.getVirtualHeight() // 2 - crosshair.getHeight() // 2)

    target = Target("assets/target.png", 0, 0, speed=0.32)
    target.setScale(0.1)

    pygame.mouse.set_pos(window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)
    pygame.mouse.set_visible(True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                # Get mouse movement
                mouse_x, mouse_y = event.rel
                target.x += mouse_x * target.speed
                target.y += mouse_y * target.speed
                # Center the mouse cursor again
                pygame.mouse.set_pos(window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = event.pos
                if target.isCollision(25,25, (window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)):
                    target.setPosition(-100,-100)

        keys_pressed = pygame.key.get_pressed()

        window.clearScreen()
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        window.getScreen().blit(target.getSurface(), target.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        window.updateFrame()