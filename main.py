from my_sprite import MySprite
from box import Box
from colors import Color
from text import Text
from image_sprite import ImageSprite
from target import Target
from button import Button
from window import Window
import pygame
def get_font(size):
    return pygame.font.Font("assets/font.ttc", size)


def gridshot():
    while True:
        grid_mouse_pos = pygame.mouse.get_pos()

        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())

        grid_back = Button(pos=(window.getVirtualWidth()-100, window.getVirtualHeight()-30),
                           text_input="Main Menu", font=get_font(30),base_color=Color.white, hover_color=Color.green)
        grid_back.changeColor(grid_mouse_pos)
        grid_back.update(window.getScreen())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if grid_back.checkForInput(grid_mouse_pos):
                    main_menu()

        pygame.display.update()

def webshot():
    while True:
        web_mouse_pos = pygame.mouse.get_pos()

        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())

        web_back = Button(pos=(window.getVirtualWidth()-100, window.getVirtualHeight()-30),
                           text_input="Main Menu", font=get_font(30),base_color=Color.white, hover_color=Color.green)
        web_back.changeColor(web_mouse_pos)
        web_back.update(window.getScreen())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if web_back.checkForInput(web_mouse_pos):
                    main_menu()

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
                    gridshot()
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


