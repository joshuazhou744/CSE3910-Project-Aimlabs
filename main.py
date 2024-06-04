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
from flash import Flash
import pygame.mixer
import sounds
from player import Player
def get_font(size):
    return pygame.font.Font("assets/font.ttc", size)


def gridshot(window, sens):
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
        target = Target("assets/target.png", 0, 0, speed=sens)
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
                        sounds.hit_sfx.play()
                        score.updateAccuracy()
                        text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")

        keys_pressed = pygame.key.get_pressed()

        for target in targets:
            target.wrapEdge(1.2 * window.getVirtualWidth(), -1.2 * window.getVirtualWidth(),
                            1.2 * window.getVirtualHeight(), -1.2 * window.getVirtualHeight())

        window.clearScreen()
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        window.getScreen().blit(text.getSurface(), text.getPosition())
        for target in targets:
            window.getScreen().blit(target.getSurface(), target.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        pygame.display.update()
        if check_ended(score.hits, 10):
            pygame.mouse.set_visible(True)
            endscreen(window, score.accuracy)


def webshot(window, sens):
    score = Score()
    counter = 0
    text = Text(text=f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}", font=get_font(24),
                color=Color.black)

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth() // 2 - crosshair.getWidth() // 2,
                          window.getVirtualHeight() // 2 - crosshair.getHeight() // 2)

    pygame.mouse.set_visible(False)

    target = Target("assets/target.png", 0, 0, speed=sens)
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
                    sounds.hit_sfx.play()
                    score.updateAccuracy()
                    text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")

        target.wrapEdge(1.1 * window.getVirtualWidth(), -1.1 * window.getVirtualWidth(),
                            1.1 * window.getVirtualHeight(), -1.1 * window.getVirtualHeight())

        window.clearScreen()
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        window.getScreen().blit(text.getSurface(), text.getPosition())
        window.getScreen().blit(target.getSurface(), target.getPosition())
        window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
        pygame.display.update()
        if check_ended(score.hits, 10):
            pygame.mouse.set_visible(True)
            endscreen(window, score.accuracy)


def flashshot(window, sens):
    score = Score()
    flash = Flash()
    flash_mouse_pos = pygame.mouse.get_pos()

    flash_img = ImageSprite("assets/flash.png")
    flash_img.setScale(0.4,0.5)

    text = Text(text=f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}", font=get_font(24),
                color=Color.black)

    crosshair = ImageSprite("assets/crosshair.png")
    crosshair.setScale(0.01)
    crosshair.setPosition(window.getVirtualWidth() // 2 - crosshair.getWidth() // 2,
                          window.getVirtualHeight() // 2 - crosshair.getHeight() // 2)
    pygame.mouse.set_visible(False)

    targets = []
    target = Target("assets/target.png", 0, 0, speed=sens)
    target.setScale(0.1)
    target.setPosition(randint(int(window.getVirtualWidth() * 0.2),
                               int(window.getVirtualWidth() * 0.8) - target.getWidth()),
                       randint(int(window.getVirtualWidth() * 0.2),
                               int(window.getVirtualHeight() * 0.8) - target.getHeight()))
    targets.append(target)

    target_visible_time = pygame.time.get_ticks()
    flash_screen = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                # Get mouse movement
                mouse_x, mouse_y = event.rel
                for target in targets:
                    target.x += mouse_x * target.speed
                    target.y += mouse_y * target.speed
                # Center the mouse cursor again
                pygame.mouse.set_pos(window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)
            elif event.type == pygame.MOUSEBUTTONDOWN and flash_screen:
                flash_screen = False
                score.shots += 1
                score.updateAccuracy()
                text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")
                for target in targets:
                    if target.isCollision(25, 25, (window.getVirtualWidth() // 2, window.getVirtualHeight() // 2)):
                        flash.flash_image(window, flash_img)
                        target.setPosition(randint(int(window.getVirtualWidth() * 0.2),
                                                   int(window.getVirtualWidth() * 0.8) - target.getWidth()),
                                           randint(int(window.getVirtualWidth() * 0.2),
                                                   int(window.getVirtualHeight() * 0.8) - target.getHeight()))
                        score.hits += 1
                        sounds.hit_sfx.play()
                        score.updateAccuracy()
                        text.setText(f"Shots: {score.shots} Hits: {score.hits} Accuracy: {score.accuracy}")
                target_visible_time = pygame.time.get_ticks()



        if not flash_screen:
            for target in targets:
                target.updatePosition()
                target.wrapEdge(1.1*window.getVirtualWidth(), -1.1*window.getVirtualWidth(), 1.1*window.getVirtualHeight(), -1.1*window.getVirtualHeight())

            window.clearScreen()
            window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
            window.getScreen().blit(text.getSurface(), text.getPosition())
            for target in targets:
                window.getScreen().blit(target.getSurface(), target.getPosition())
            window.getScreen().blit(crosshair.getSurface(), crosshair.getPosition())
            pygame.display.update()

            if not flash_screen and pygame.time.get_ticks() - target_visible_time >= flash.sight_time:
                flash.updateTime()
                flash_screen = True

        if flash_screen:
            flash.flash_image(window, flash_img)

        if check_ended(score.hits, 5):
            pygame.mouse.set_visible(True)
            endscreen(window, score.accuracy)


def main_menu():
    while True:
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        menu_mouse_pos = pygame.mouse.get_pos()

        sens = 0.5

        menu_text = get_font(100).render("Main Menu", True, '#b68f40')
        menu_rect = menu_text.get_rect(center=(window.getVirtualWidth() // 2, 100))

        grid_button = Button(pos=(window.getVirtualWidth() // 2, 220), text_input="Gridshot",
                             font=get_font(30), base_color=Color.red, hover_color=Color.green)
        web_button = Button(pos=(window.getVirtualWidth() // 2, 320), text_input="Webshot",
                            font=get_font(30), base_color=Color.red, hover_color=Color.green)
        flash_button = Button(pos=(window.getVirtualWidth() // 2, 420), text_input="Flashshot",
                              font=get_font(30), base_color=Color.red, hover_color=Color.green)
        quit_button = Button(pos=(window.getVirtualWidth() // 2, 520), text_input="Quit",
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
                    gridshot(window, sens)
                if web_button.checkForInput(menu_mouse_pos):
                    webshot(window, sens)
                if flash_button.checkForInput(menu_mouse_pos):
                    flashshot(window, sens)
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    exit()
        pygame.display.update()

def check_ended(current_score, target_score):
    if current_score >= target_score:
        return True
    else:
        return False

def endscreen(window, accuracy):
    while True:
        window.getScreen().blit(bg_img.getSurface(), bg_img.getPosition())
        end_mouse_pos = pygame.mouse.get_pos()

        end_text = get_font(25).render(f"Game Over! Final Accuracy {accuracy}", True, '#000000')
        end_rect = end_text.get_rect(center=(window.getVirtualWidth() // 2, 250))
        end_button = Button(pos=(window.getVirtualWidth() // 2, 320),
                            text_input=f" Click Here to Return to Main Menu ",
                            font=get_font(30), base_color=Color.red, hover_color=Color.green)

        window.getScreen().blit(end_text, end_rect)

        end_button.changeColor(end_mouse_pos)
        end_button.update(window.getScreen())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if end_button.checkForInput(end_mouse_pos):
                    main_menu()
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

