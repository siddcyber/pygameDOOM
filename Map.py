import pygame as game

minimap = [
    [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True],
    [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, True],

    [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, True],
    [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
     True, True, True, True, True],
]


class Map:
    def __init__(self, DOOM):
        self.DOOM = DOOM
        self.minimap = minimap
        self.worldmap = {}
        self.getMap()

    def getMap(self):
        for j, row in enumerate(self.minimap):
            for i, value in enumerate(row):
                if value:
                    self.worldmap[(i, j)] = value

    def draw(self):
        for pos in self.worldmap:
            game.draw.rect(self.DOOM.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
