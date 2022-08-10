from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, Game):
        self.game = Game
        self.x, self.y = playerPosition
        self.angle = playerAngle

    def movement(self):
        dx, dy = 0, 0
        speed = playerSpeed * self.game.deltaTime
        speed_sin = speed * math.sin(self.angle)
        speed_cos = speed * math.cos(self.angle)

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        self.x = dx
        self.y = dy
        if keys[pg.K_LEFT]:
            self.angle -= playerRotationSpeed * self.game.deltaTime
        if keys[pg.K_RIGHT]:
            self.angle += playerRotationSpeed * self.game.deltaTime
        self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                       (self.x * 100 * width * math.cos(self.angle),
                        self.y * 100 * width * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def mapPosition(self):
        return int(self.x), int(self.y)
