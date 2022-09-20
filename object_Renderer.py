import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    @staticmethod
    def get_textures(path, resolution=(textureSize, textureSize)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, resolution)

    def load_wall_textures(self):
        return {
            1: self.get_textures('resources/textures/1.png'),
            2: self.get_textures('resources/textures/2.png'),
            3: self.get_textures('resources/textures/3.png'),
            4: self.get_textures('resources/textures/4.png'),
            5: self.get_textures('resources/textures/5.png'),
        }
