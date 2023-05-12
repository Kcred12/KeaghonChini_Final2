import pygame as py
import sys

py.init()

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 75
BUTTON_COLOR = (128,128,128)


def show_main_menu(window):

    # Creates the rectangle for the play button and places it
    play_button_image = py.Surface((BUTTON_WIDTH,BUTTON_HEIGHT))
    play_button_image.fill(BUTTON_COLOR)
    play_button_rect = play_button_image.get_rect()
    play_button_rect.center = ((window.get_width() / 2) - 120,(window.get_height() / 2) + 30)

    # Creates the rectangle for the quit button and places it
    quit_button_image = py.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    quit_button_image.fill(BUTTON_COLOR)
    quit_button_rect = quit_button_image.get_rect()
    quit_button_rect.center = ((window.get_width() / 2) + 120, (window.get_height() / 2) + 30)

    # Draws them to the screen
    py.draw.rect(window, BUTTON_COLOR, play_button_rect)
    py.draw.rect(window, BUTTON_COLOR, quit_button_rect)

    # Making the font object and drawing them to the buttons
    font = py.font.SysFont('Corbel', 50)
    play_text = font.render('Play', True, (255,255,255))
    quit_text = font.render('Quit', True, (255,255,255))

    play_text_rect = play_text.get_rect()
    play_text_rect.center = play_button_rect.center
    quit_text_rect = quit_text.get_rect()
    quit_text_rect.center = quit_button_rect.center

    window.blit(play_text, play_button_rect)
    window.blit(quit_text, quit_button_rect)

    py.display.update()

    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()

            if event.type == py.MOUSEBUTTONDOWN:
                mouse_pos = py.mouse.get_pos()

                if play_button_rect.collidepoint(mouse_pos):
                    running = False
                if quit_button_rect.collidepoint(mouse_pos):
                    py.quit()


            window.fill((0, 0, 0))

            py.draw.rect(window, BUTTON_COLOR, play_button_rect)
            py.draw.rect(window, BUTTON_COLOR, quit_button_rect)

            window.blit(play_text, play_text_rect)
            window.blit(quit_text, quit_text_rect)

            py.display.update()
