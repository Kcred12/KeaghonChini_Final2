import pygame as py
import random

py.init()

enemy_velocities = [-4, -3, -2, -1, 1, 2, 3, 4]


class Enemies(py.sprite.Sprite):

    width,height = 25,25

    def __init__(self, window, max_width, max_height, top_height):
        py.sprite.Sprite.__init__(self)

        self.xvelocity = random.choice(enemy_velocities)
        self.yvelocity = random.choice(enemy_velocities)
        self.max_width = max_width # The size of the screen, the furthest right
        self.max_height = max_height # The height of the screen, the furthest down it can go
        self.top_height = top_height # The bottom of the margin, highest it can go
        self.color = (255, 0, 0)
        self.window = window
        self.image = py.Surface((Enemies.width,Enemies.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.starting_xpoint = random.randint(0+Enemies.width,self.max_width-Enemies.width)
        self.starting_ypoint = random.randint(self.top_height+Enemies.height,self.max_height-Enemies.height)
        self.rect.left = self.starting_xpoint
        self.rect.top = self.starting_ypoint

    def draw(self):
        py.draw.rect(self.window, self.color, self.rect)

    def update(self):

        self.rect.move_ip(self.xvelocity,self.yvelocity)

        if self.rect.right > self.max_width or self.rect.left < 0:
            self.xvelocity *= -1
        if self.rect.bottom > self.max_height or self.rect.top < self.top_height:
            self.yvelocity *= -1
