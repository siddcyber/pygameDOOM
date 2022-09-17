from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, Game):
        self.game = Game
        self.x, self.y = playerPosition
        self.angle = playerAngle

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed_sin = playerSpeed * self.game.delta_time * sin_a
        speed_cos = playerSpeed * self.game.delta_time * cos_a
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
        if keys[pg.K_LEFT]:
            self.angle -= playerRotationSpeed * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += playerRotationSpeed * self.game.delta_time
        # self.x += dx
        # self.y += dy

        self.check_wall_collision(dx, dy)
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                     (self.x * 100 + width * math.cos(self.angle),
                      self.y * 100 + width * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 5)

    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def mapPosition(self):
        return int(self.x), int(self.y)
