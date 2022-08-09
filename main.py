import pygame as game
import sys
from settings import *
from Map import *

class Game:
    def __init__(self):
        game.init()
        self.screen = game.display.set_mode(resolution)
        self.clock = game.time.Clock()
        self.newGame()
    def newGame(self):
        self.map = Map(self)

    def update(self):
        game.display.flip()
        self.clock.tick(frameRate)
        game.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
    def checkEvent(self):
        for event in game.event.get():
            if event.type ==game.QUIT or (event.type == game.KEYDOWN and event.type == game.K_ESCAPE):
                game.quit()
                sys.exit()
    def run(self):
        while True:
            self.checkEvent()
            self.update()
            self.draw()

if __name__ == '__main__':
    DOOM = Game()
    DOOM.run()