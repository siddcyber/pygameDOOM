import pygame as pg
from settings import *


class SpriteObject:
    def __init__(self, game, path='resources/sprite/static_sprites', pos=(10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.imageWidth = self.image.get_width()
        self.imageHalfWidth = self.image.get_width() // 2
        self.imageRatio = self.imageWidth/self.image.get_height()
    def getSpriteProjecttion(self):
        proj = screenDistance /self.normDist
        projWidth, projHeight = self.imageWidth* self.imageRatio, proj
    def getsprites(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        deltaRays = delta / deltaAngle
        self.screenX = (halfNoOfRays + deltaRays) * scale
        self.dist = math.hypot(dx, dy)
        self.normDist = self.dist * math.cos(delta)
        if -self.imageHalfWidth < self.screenX < (width + self.imageHalfWidth) and self.normDist > 0.5:
            self.getSpriteProjecttion()

    def update(self):
        self.getsprites()
