# import pygame as pg
# from spriteObject import *
# from settings import *
import sys
import Map
from Map import *
from player import *
from Raycasting import *
from object_Renderer import *
from objectHandler import *

class DoomGameMain:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.newGame()

    def newGame(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.objecthandler = ObjectHandler(self)
        # self.staticSprite = SpriteObject(self)
        # self.animatedSprite = AnimatedSprites(self)

    def updateMain(self):
        self.player.update()
        self.raycasting.update()
        self.objecthandler.update()
        # self.staticSprite.update()
        # self.animatedSprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def checkEvent(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.checkEvent()
            self.draw()
            self.updateMain()


if __name__ == '__main__':
    DOOM = DoomGameMain()
    DOOM.run()
