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

    bg_img = ImageSprite("assets/background.png")
    bg_img.setScale(3, 1.7)

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth()//2-crosshair.getWidth()//2, window.getVirtualHeight()//2-crosshair.getHeight()//2)

    boxes = []
    for i in range(3):
        boxes.append(Box(10,10, randint(0,window.getVirtualWidth()), randint(0,window.getVirtualHeight()), speed=0.32))

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
                for box in boxes:
                    box.x += mouse_x*box.speed
                    box.y += mouse_y*box.speed
                # Center the mouse cursor again
                pygame.mouse.set_pos(window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)

        keys_pressed = pygame.key.get_pressed()

        for box in boxes:
            box.WASDMove(keys_pressed)

        window.clearScreen()
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        for box in boxes:
            window.getScreen().blit(box.getSurface(), box.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        window.updateFrame()
