import pygame as py

py.init()

PLAYER_COLOR = (0,255,255)
width = 25
height = 25
player_velocity = 5


class Player(py.sprite.Sprite):


    def __init__(self,color,width,height):
        py.sprite.Sprite.__init__(self) # constructor for base sprite class, necessary when inheriting

        self.color = PLAYER_COLOR # sets the color for the player to be made to the constant above
        self.image = py.Surface((width,height)) # creates a surface the same size as the player, allows stuff to be
                                                # done to the player like getting the rectangle around it for collision

        self.rect = self.image.get_rect()
        py.draw.rect(self.image, self.color, py.Rect(0, 0, width, height))  # actually draws the rectangle to the screen

    def move(self,MAX_WIDTH,MAX_HEIGHT,TOP_MARGIN_HEIGHT):
        keys = py.key.get_pressed()

        if keys[py.K_UP]:
            if self.rect.top <= TOP_MARGIN_HEIGHT:
                self.rect.top = TOP_MARGIN_HEIGHT
            else:
                self.rect.y += -player_velocity
        if keys[py.K_DOWN]:
            if self.rect.bottom >= MAX_HEIGHT:
                self.rect.bottom = MAX_HEIGHT
            else:
                self.rect.y += player_velocity
        if keys[py.K_RIGHT]:
            if self.rect.right >= MAX_WIDTH:
                self.rect.right = MAX_WIDTH
            else:
                self.rect.x += player_velocity
        if keys[py.K_LEFT]:
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.x += -player_velocity

    def collision_check(self,player,enemies,healthbar):

        if py.sprite.spritecollideany(player,enemies):
            healthbar.take_damage()

    def draw(self,window):
        window.blit(self.image,(self.rect.x,self.rect.y)) # draws the player to the screen

def create_player():
    player_1 = Player((0,255,255),width,height)

    player_1.rect.center = (800/2,500/2)

    return player_1

