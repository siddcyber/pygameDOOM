import pygame as pg
from settings import width, height

_ = False

minimap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 3, 4, 3, 4, _, _, 3, 4, 3, 4, _, _, _, _, _, _, 3, 4, 3, 4, _, _, 3, 4, 3, 4, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, 4, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 3, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, 3, _, _, _, _, _, 1],
    [1, _, _, 4, 3, 4, 3, _, _, 4, 3, 4, 3, _, _, _, _, _, _, 4, 3, 4, 3, _, _, 4, 3, 4, 3, 2, 2, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, 2, 5, 5, 5, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, 2, 5, 5, 5, 2, 2, 2, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 4, 3, 4, _, _, 3, 4, 3, 4, _, _, _, _, _, _, 3, 4, 3, 4, _, _, 3, 4, 3, 4, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, 4, _, _, 4, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 3, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, 3, _, _, _, _, _, 1],
    [1, 2, 2, 4, 3, 4, 3, _, _, 4, 3, 4, 3, _, _, _, _, _, _, 4, 3, 4, 3, _, _, 4, 3, 4, 3, 2, 2, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

mapScalingWidth = int(width / int(len(minimap[0])))
mapScalingHeight = int(height / int(len(minimap)))
SpritePosList = [(1, 1), (2, 2), (10, 10), (15, 15), (len(minimap[0]) - 1.5, len(minimap) - 1.5)]


class Map:
    def __init__(self, game):
        self.game = game
        self.minimap = minimap
        self.world_map = {}
        self.getMap()

    def getMap(self):
        for j, row in enumerate(self.minimap):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            # top, left, width, height
            pg.draw.rect(self.game.screen, 'darkgray',
                           (pos[0] * mapScalingWidth, pos[1] * mapScalingHeight, mapScalingWidth, mapScalingHeight))
