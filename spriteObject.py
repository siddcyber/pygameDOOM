import pygame as pg
from settings import *
import os
from collections import deque


class AnimatedSprites:
    def __init__(self, game, path='resources/sprites/animated_sprites/green_light/0.png', pos=(5, 5), scale=0.8,
                 shift=0.27, animationTime=120):
        # super().__init__(game, path, pos, scale, shift)
        self.animationTime = animationTime
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.prevAnimationTime = pg.time.get_ticks()
        self.animationTrigger = False

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
        # super().update()
        self.getsprites()
        self.checkAnimationTime()
        self.animate(self.images)

    def animate(self, images):
        if self.animationTrigger:
            images.rotate(-1)
            self.image = images[0]

    def checkAnimationTime(self):
        self.animationTrigger = False
        currentTime = pg.time.get_ticks()
        if currentTime - self.prevAnimationTime > self.animationTime:
            self.prevAnimationTime = currentTime
            self.animationTrigger = True

    def get_images(self, path):
        images = deque()
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                img = pg.image.load(path + '/' + filename).convert_alpha()
                images.append(img)
        return images


# class SpriteObject:
#     def __init__(self, game, path='resources/sprites/static_sprites/candlebra.png', pos=(1.2, 1.2), Scale=0.7,
#                  shift=0.27):
#         self.game = game
#         self.player = game.player
#         self.x, self.y = pos
#         self.image = pg.image.load(path).convert_alpha()
#         self.imageWidth = self.image.get_width()
#         self.imageHalfWidth = self.image.get_width() // 2
#         self.imageRatio = self.imageWidth / self.image.get_height()
#         self.dx, self.dy, self.theta, self.screen_x, self.dist, self.normDist = 0, 0, 0, 0, 1, 1
#         self.spriteHalfWidth = 0
#         self.spriteScale = Scale
#         self.spriteHeightShift = shift
#
#     def getSpriteProjecttion(self):
#         proj = screenDistance / self.normDist * self.spriteScale
#         projWidth, projHeight = proj * self.imageRatio, proj
#         image = pg.transform.scale(self.image, (int(projWidth), int(projHeight)))
#         self.spriteHalfWidth = projWidth // 2
#         heightShift = projHeight * self.spriteHeightShift
#         pos = self.screenX - self.spriteHalfWidth, half_height - projHeight // 2 + heightShift
#         self.game.raycasting.objectsToRender.append((self.normDist, image, pos))
#
#     def getsprites(self):
#         dx = self.x - self.player.x
#         dy = self.y - self.player.y
#         self.dx, self.dy = dx, dy
#         self.theta = math.atan2(dy, dx)
#         delta = self.theta - self.player.angle
#         if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
#             delta += math.tau
#         deltaRays = delta / deltaAngle
#         self.screenX = (halfNoOfRays + deltaRays) * scale
#         self.dist = math.hypot(dx, dy)
#         self.normDist = self.dist * math.cos(delta)
#         if -self.imageHalfWidth < self.screenX < (width + self.imageHalfWidth) and self.normDist > 0.5:
#             self.getSpriteProjecttion()
#
#     def update(self):
#         self.getsprites()
