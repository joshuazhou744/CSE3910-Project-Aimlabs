from my_sprite import MySprite
from box import Box
from colors import Color
from text import Text
from image_sprite import ImageSprite
from target import Target
from button import Button
from window import Window
import pygame
from random import randint
from score import Score
def get_font(size):
    return pygame.font.Font("assets/font.ttc", size)


def gridshot(window):
    score = Score()
    grid_mouse_pos = pygame.mouse.get_pos()

    text = Text(text=f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}", font=get_font(24), color=Color.black)

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth() // 2 - crosshair.getWidth() // 2,
                          window.getVirtualHeight() // 2 - crosshair.getHeight() // 2)

    pygame.mouse.set_visible(False)

    targets = []
    for i in range(5):
        target = Target("assets/target.png", 0, 0, speed=0.5)
        target.setScale(0.1)
        target.setPosition(randint(int(window.getVirtualWidth()*0.2), int(window.getVirtualWidth()*0.8) - target.getWidth()),
                           randint(int(window.getVirtualWidth()*0.2), int(window.getVirtualHeight()*0.8) - target.getHeight()))
        targets.append(target)

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
                score.shots += 1
                score.updateAccuracy()
                text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")
                for target in targets:
                    if target.isCollision(25, 25, (window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)):
                        target.setPosition(randint(int(window.getVirtualWidth() * 0.4),
                                                   int(window.getVirtualWidth() * 0.6) - target.getWidth()),
                                           randint(int(window.getVirtualWidth() * 0.4),
                                                   int(window.getVirtualHeight() * 0.6) - target.getHeight()))
                        score.hits += 1
                        score.updateAccuracy()
                        text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")

        keys_pressed = pygame.key.get_pressed()

        for target in targets:
            target.WASDMove(keys_pressed)


        window.clearScreen()
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        window.getScreen().blit(text.getSurface(), text.getPosition())
        for target in targets:
            window.getScreen().blit(target.getSurface(), target.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        pygame.display.update()

def webshot():
    score = Score()
    counter = 0
    text = Text(text=f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}", font=get_font(24),
                color=Color.black)

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth() // 2 - crosshair.getWidth() // 2,
                          window.getVirtualHeight() // 2 - crosshair.getHeight() // 2)

    pygame.mouse.set_visible(False)

    target = Target("assets/target.png", 0, 0)
    target.setScale(0.1)
    target.setPosition(400 - target.getWidth() // 2, 300 - target.getHeight() // 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                # Get mouse movement
                mouse_x, mouse_y = event.rel
                target.x += mouse_x*target.speed
                target.y += mouse_y*target.speed

                target.updatePosition()
                # Center the mouse cursor again
                pygame.mouse.set_pos(window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                score.shots += 1
                score.updateAccuracy()
                text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")
                if target.isCollision(25, 25, (window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)):

                    target.setPosition(randint(0, window.getVirtualWidth() - target.getWidth()),
                       randint(0, window.getVirtualHeight() - target.getHeight()))
                    score.hits += 1
                    score.updateAccuracy()
                    text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")

        window.clearScreen()
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        window.getScreen().blit(text.getSurface(), text.getPosition())
        window.getScreen().blit(target.getSurface(), target.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        pygame.display.update()



def flashshot():
    while True:
        flash_mouse_pos = pygame.mouse.get_pos()

        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())

        flash_back = Button(pos=(window.getVirtualWidth()-100, window.getVirtualHeight()-30),
                           text_input="Main Menu", font=get_font(30),base_color=Color.white, hover_color=Color.green)
        flash_back.changeColor(flash_mouse_pos)
        flash_back.update(window.getScreen())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flash_back.checkForInput(flash_mouse_pos):
                    main_menu()

        pygame.display.update()
def main_menu():
    while True:
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Main Menu", True, '#b68f40')
        menu_rect = menu_text.get_rect(center=(window.getVirtualWidth()//2, 100))

        grid_button = Button(pos=(window.getVirtualWidth()//2, 220), text_input="Gridshot",
                             font=get_font(30), base_color=Color.red, hover_color=Color.green)
        web_button = Button(pos=(window.getVirtualWidth()//2, 320), text_input="Webshot",
                            font=get_font(30), base_color=Color.red, hover_color=Color.green)
        flash_button = Button(pos=(window.getVirtualWidth()//2, 420), text_input="Flashshot",
                              font=get_font(30), base_color=Color.red, hover_color=Color.green)
        quit_button = Button(pos=(window.getVirtualWidth()//2, 520), text_input="Quit",
                             font=get_font(30), base_color=Color.red, hover_color=Color.green)

        window.getScreen().blit(menu_text, menu_rect)

        for button in [grid_button, web_button, flash_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(window.getScreen())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if grid_button.checkForInput(menu_mouse_pos):
                    gridshot(window)
                if web_button.checkForInput(menu_mouse_pos):
                    webshot()
                if flash_button.checkForInput(menu_mouse_pos):
                    flashshot()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    exit()
        pygame.display.update()
if __name__ == '__main__':
    pygame.init()

    window = Window("Aim Trainer")

    bg_img = ImageSprite("assets/background.png")
    bg_img.setScale(3, 1.7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        window.clearScreen()
        main_menu()
        window.updateFrame()


