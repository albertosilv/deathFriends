import pygame as pg
from .settings import *
class Bullet:
    def __init__(self,game,pos,dire):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.vel = dire * BULLET_SPEED
        self.life = pg.time.get_ticks()
    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if(pg.time.get_ticks() - self.life >BULLET_LIFE):
            self.kill()
