import pygame as game

_ = False
minimap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, 1, _, _, _, _,  _,1],
    [1, _, _, 1, 1, 1, 1, _, _, 1, 1, 1, 1, _,  _,1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, _, 1, _, _, _, 1, _, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


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
            # length, width
            game.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 1)
