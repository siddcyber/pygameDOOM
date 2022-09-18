import pygame as game
from settings import width

_ = False
minimap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, _, 1, _, _, _, 1, _, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

mapScaling = int(width // int(len(minimap[0])))


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
            # top, left, length, width
            game.draw.rect(self.game.screen, 'darkgray',
                           (pos[0] * mapScaling, pos[1] * mapScaling, mapScaling, mapScaling))
