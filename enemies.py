import pygame as py
import random

py.init()

enemy_velocities = [-3,-2,-1,1,2,3]

class Enemies(py.sprite.Sprite):

    def __init__(self,window,max_width,max_height,top_height):
        py.sprite.Sprite.__init__(self)
        self.xvelocity = random.choice(enemy_velocities)
        self.yvelocity = random.choice(enemy_velocities)
        self.max_width = max_width
        self.max_height = max_height
        self.top_height = top_height
        self.width = 25
        self.height = 25
        self.color = (255,0,0)
        self.window = window
        self.enemy_rect = py.Rect(0,0,self.width,self.height)
        self.enemy_rect.right = max_width
        self.enemy_rect.top = 250

    def draw(self):
        py.draw.rect(self.window,self.color,self.enemy_rect)

    def move(self):
        if self.enemy_rect.top <= self.top_height or self.enemy_rect.bottom >= self.max_height:
            self.yvelocity *= -1
        if self.enemy_rect.right > self.max_width or self.enemy_rect.left <= 0:
            self.xvelocity *= -1

        self.enemy_rect.y += self.yvelocity
        self.enemy_rect.x += self.xvelocity