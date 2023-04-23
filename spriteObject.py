import pygame as pg
from settings import *


class SpriteObject:
    def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png', pos=(1, 1), scale=0.7, shift=0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.imageWidth = self.image.get_width()
        self.imageHalfWidth = self.image.get_width() // 2
        self.imageRatio = self.imageWidth / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.normDist = 0, 0, 0, 0, 1, 1
        self.spriteHalfWidth = 0
        self.spriteScale = scale
        self.spriteHeightShift = shift

    def getSpriteProjecttion(self):
        proj = screenDistance / self.normDist * self.spriteScale
        projWidth, projHeight = proj * self.imageRatio, proj
        image = pg.transform.scale(self.image, (int(projWidth), int(projHeight)))
        self.spriteHalfWidth = projWidth // 2
        heightShift = projHeight * self.spriteHeightShift
        pos = self.screenX - self.spriteHalfWidth, half_height - projHeight // 2 + heightShift
        self.game.raycasting.objectsToRender.append((self.normDist, image, pos))

    def getsprites(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        deltaRays = delta / deltaAngle
        self.screenX = (halfNoOfRays + deltaRays) * scale
        self.dist = math.hypot(dx, dy)
        self.normDist = self.dist * math.cos(delta)
        if -self.imageHalfWidth < self.screenX < (width + self.imageHalfWidth) and self.normDist > 0.5:
            self.getSpriteProjecttion()

    def update(self):
        self.getsprites()
