# Here is the link for when you push or commit
# https://github.com/Kcred12/KeaghonChini_Final2.git
import pygame as py
import sys
from create_gui import *
from player import *
from enemies import *

py.init()

TOP_MARGIN_HEIGHT = 45

def main():
    """This is the main method and is where the methods are called to set
    up the game. It also contains the game loop, where events are handled"""

    # This makes the actual window appear, as well as returning the width and height of the window
    # This lets me pass the nums as parameters for bounding boxes instead of hard coding values
    (window, MAX_WIDTH, MAX_HEIGHT) = make_window()


    top_margin = make_top_margin(window,MAX_WIDTH, TOP_MARGIN_HEIGHT)
    py.draw.rect(window,(128,128,128),top_margin)

    healthbar = Healthbar(window)
    healthbar.draw()


    player_1 = create_player()

    player_list = py.sprite.Group()
    player_list.add(player_1)
    player_list.draw(window)

    enemy = Enemies(window,MAX_WIDTH,MAX_HEIGHT,TOP_MARGIN_HEIGHT)
    enemy.draw()

    clock = py.time.Clock()

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()

        player_1.move(MAX_WIDTH, MAX_HEIGHT, TOP_MARGIN_HEIGHT)
        enemy.move()
        print(enemy.enemy_rect.right)
        window.fill((0, 0, 0))

        py.draw.rect(window, (128, 128, 128), top_margin)
        healthbar.draw()
        player_1.draw(window)
        enemy.draw()

        py.display.update()
        clock.tick(120)



if __name__ == '__main__':
    main()
