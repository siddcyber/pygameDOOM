import pygame as pg
import math
from settings import *
from Map import mapScaling


class RayCasting:
    def __init__(self, game):
        self.game = game

        def rayCast(self):
            playerx, playery = self.game.player.position
            xMap, yMap = self.game.player.mapPosition

            rayAngle = self.game.player.angle - halfFOV + 0.0001
            for ray in range(noOfRays):
                sin_a = math.sin(rayAngle)
                cos_a = math.cos(rayAngle)
                #  Horizontal
                if sin_a > 0:
                    y_horz = yMap + 1
                    dy = 1
                else:
                    y_horz = yMap - 1e-6
                    dy = -1
                depth_horz = (y_horz - playery) / sin_a
                x_horz = playerx + depth_horz * cos_a
                deltaDepth = dy / sin_a
                dx = deltaDepth * cos_a
                for i in range(maxDepth):
                    tile_horz = int(x_horz), int(y_horz)
                    if tile_horz in self.game.Map.world_map:
                        break
                    x_horz += dx
                    y_horz += dy
                    depth_horz += deltaDepth
                #  vertical
                if cos_a > 0:
                    x_vert = xMap + 1
                    dx = 1
                else:
                    x_vert = xMap - 1e-6
                    dx = -1
                depth_vert = (x_vert - playerx) / cos_a
                y_vert = playery + depth_vert * sin_a
                deltaDepth = dx / cos_a
                dy = deltaDepth * sin_a
                for i in range(maxDepth):
                    tile_vert = int(x_vert), int(y_vert)
                    if tile_vert in self.game.Map.world_map:
                        break
                    x_vert += dx
                    y_vert += dy
                    depth_vert = deltaDepth
                if depth_vert < depth_horz:
                    depth = depth_vert
                else:
                    depth = depth_horz
                #  draw for debug
                pg.draw.line(self.game.screen, "yellow", (playerx * mapScaling, playery * mapScaling),
                             (playerx * mapScaling + mapScaling * depth * cos_a,
                              playery * mapScaling + mapScaling * depth * sin_a),2)
                rayAngle += deltaAngle

        def update(self):
            self.rayCast()
