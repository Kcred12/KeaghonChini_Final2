import pygame as py

py.init()

size = width, height = (1000, 750)
background_color = (0, 0, 0)


def make_window():
    window = py.display.set_mode(size)
    py.display.set_caption('Squares!')
    window.fill(background_color)

    py.display.flip()

    return window, width, height


def make_top_margin(width, height):
    margin_rect = py.Rect(0, 0, width, height)  # Creates the rect surface of the margin on top
    return margin_rect


class Healthbar:

    def __init__(self, window):
        self.window = window
        self.width = 200
        self.height = 25
        self.color = (0, 255, 0)
        self.rect = py.Rect(0, 0, self.width, self.height)
        self.rect.topleft = (10, 10)

    def take_damage(self):
        if self.rect.width <= 100:
            self.color = (255,255,0)
        if self.rect.width <= 50:
            self.color = (255,0,0)
        self.rect.width -= 2

    def draw(self):
        py.draw.rect(self.window, self.color, self.rect)
