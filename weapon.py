from sprite_object import *
import pygame as pg

class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=0.6, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)

        # Презаписваме анимацията, заредена от родителския клас.
        # Оставяме само едно статично изображение (0.png).
        static_image_path = '../ray-casting-pygame/resources/sprites/weapon/shotgun/0.png'
        single_image = pg.image.load(static_image_path).convert_alpha()
        scaled_image = pg.transform.smoothscale(
            single_image, (int(single_image.get_width() * scale), int(single_image.get_height() * scale))
        )
        self.images = deque([scaled_image])

        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()