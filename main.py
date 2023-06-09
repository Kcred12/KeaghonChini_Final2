# Here is the link for when you push or commit
# https://github.com/Kcred12/KeaghonChini_Final2.git
import pygame as py
import sys
from create_gui import *
from player import *
from enemies import *
from main_menu import *
import time

py.init()

TOP_MARGIN_HEIGHT = 45

def main():
    """This is the main method and is where the methods are called to set
    up the game. It also contains the game loop, where events are handled"""

    # This makes the actual window appear, as well as returning the width and height of the window
    # This lets me pass the nums as parameters for bounding boxes instead of hard coding values
    (window, MAX_WIDTH, MAX_HEIGHT) = make_window()

    # This shows the main menu, and will fill the screen and effectively
    # clear the screen
    show_main_menu(window)
    window.fill((0, 0, 0))

    # This creates the top gray bar
    top_margin = make_top_margin(MAX_WIDTH, TOP_MARGIN_HEIGHT)
    py.draw.rect(window, (128, 128, 128), top_margin)

    # Creates the healthbar
    healthbar = Healthbar(window)
    healthbar.draw()


    # Creates the player and enemies and
    # adds them to their respective groups
    player_1 = create_player()

    player_list = py.sprite.Group()
    player_list.add(player_1)
    player_list.draw(window)

    enemies = py.sprite.Group()
    for x in range(10):
        enemy = Enemies(window, MAX_WIDTH, MAX_HEIGHT, TOP_MARGIN_HEIGHT)
        enemies.add(enemy)
        enemy.draw()

    clock = py.time.Clock()

    py.display.update()

    # Allows time before the game starts so the player is not thrown in
    time.sleep(2)

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        # Checks for arrow keys and moves player accordingly
        player_1.move(MAX_WIDTH, MAX_HEIGHT, TOP_MARGIN_HEIGHT)

        # Moves enemies in random directions
        enemies.update()
        window.fill((0, 0, 0))

        py.draw.rect(window, (128, 128, 128), top_margin)
        player_1.collision_check(player_1, enemies, healthbar)

        # Sets a kill threshold and kills the game as well
        if healthbar.rect.width == 0:
            py.quit()
            sys.exit()
        healthbar.draw()
        player_1.draw(window)
        enemies.draw(window)


        # Updates all the changes made to the screen to make them visible
        py.display.update()
        clock.tick(120)


if __name__ == '__main__':
    main()
