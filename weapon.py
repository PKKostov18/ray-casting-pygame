import pygame as pg
from settings import *

class Weapon:
    def __init__(self, game):
        self.game = game
        path = self.game.resource_path('resources/sprites/weapon/shotgun/0.png')
        self.image = pg.image.load(path).convert_alpha()

        scale = 0.4
        width = self.image.get_width() * scale
        height = self.image.get_height() * scale
        self.scaled_image = pg.transform.smoothscale(self.image, (int(width), int(height)))

        self.weapon_pos = (HALF_WIDTH - width // 2, HEIGHT - height)

        self.reloading = False
        self.damage = 50
        self.reload_time = 400
        self.last_shot_time = 0

    def update(self):
        if self.reloading:
            if pg.time.get_ticks() - self.last_shot_time > self.reload_time:
                self.reloading = False

    def draw(self):
        self.game.screen.blit(self.scaled_image, self.weapon_pos)

    def fire(self):
        if not self.reloading:
            self.reloading = True
            self.last_shot_time = pg.time.get_ticks()
            self.game.sound.shotgun.play()
            self.game.player.shot = True