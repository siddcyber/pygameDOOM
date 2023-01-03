import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.skyImage = self.get_textures('resources/textures/sky2.png', (width, half_height))
        self.skyOffset = 0

    def draw(self):
        self.drawBackground()
        self.render_gameObjects()

    def drawBackground(self):
        self.skyOffset = (self.skyOffset + 4.5 * self.game.player.rel) % width
        self.screen.blit(self.skyImage, (-self.skyOffset, 0))
        self.screen.blit(self.skyImage, (-self.skyOffset + width, 0))
        #     Floor
        pg.draw.rect(self.screen, (30, 30, 30), (0, half_height, width, height))

    def render_gameObjects(self):
        listObjects = self.game.raycasting.objectsToRender
        for depth, image, pos in listObjects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_textures(path, resolution=(textureSize, textureSize)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, resolution)

    def load_wall_textures(self):
        return {
            1: self.get_textures('resources/textures/ashwall7.png'),
            2: self.get_textures('resources/textures/2.png'),
            3: self.get_textures('resources/textures/3.png'),
            4: self.get_textures('resources/textures/4.png'),
            5: self.get_textures('resources/textures/5.png'),
        }
