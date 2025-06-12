import pygame as pg
from settings import *
import math

class Minimap:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.map = game.map
        self.player = game.player
        self.scale = 6
        self.map_width = self.map.cols * self.scale
        self.map_height = self.map.rows * self.scale
        self.pos = (10, 10)

    def draw(self):
        # Фон на миникартата
        pg.draw.rect(self.screen, 'black',
                     (self.pos[0], self.pos[1], self.map_width, self.map_height))

        # Стени
        for pos, value in self.map.world_map.items():
            pg.draw.rect(self.screen, 'darkgray',
                         (self.pos[0] + pos[0] * self.scale,
                          self.pos[1] + pos[1] * self.scale,
                          self.scale, self.scale))

        # Чудовища (NPCs) - червени точки
        for npc in self.game.object_handler.npc_list:
            if npc.alive:
                npc_x_on_map = self.pos[0] + npc.x * self.scale
                npc_y_on_map = self.pos[1] + npc.y * self.scale
                pg.draw.circle(self.screen, 'red', (npc_x_on_map, npc_y_on_map), 2)

        # Играч - голяма зелена точка
        player_x_on_map = self.pos[0] + self.player.x * self.scale
        player_y_on_map = self.pos[1] + self.player.y * self.scale
        pg.draw.circle(self.screen, 'green', (player_x_on_map, player_y_on_map), 4)

        # Посока на играча
        line_length = self.scale * 1.5
        end_x = player_x_on_map + line_length * math.cos(self.player.angle)
        end_y = player_y_on_map + line_length * math.sin(self.player.angle)
        pg.draw.line(self.screen, 'yellow', (player_x_on_map, player_y_on_map), (end_x, end_y), 1)