import pygame as pg
from settings import *
vect = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vel=vect(0,0)
        self.pos=vect(x,y)*TILESIZE
    def get_keys(self):
            self.vel = vect(0,0)
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.vel.x = -PLAYER_SPEED
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.vel.x = PLAYER_SPEED
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.vel.y = -PLAYER_SPEED
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.vel.y = PLAYER_SPEED
            if self.vel.x != 0 and self.vel.y != 0:
                self.vel*= 0.7071
    def update(self):
        self.get_keys()