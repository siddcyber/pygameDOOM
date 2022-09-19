import pygame as pg
import math
from settings import *
from Map import mapScalingWidth, mapScalingHeight


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.position
        x_map, y_map = self.game.player.mapPosition

        ray_angle = self.game.player.angle - halfFOV + 0.0001
        for ray in range(noOfRays):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(maxDepth):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(maxDepth):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
            #     for debug draw
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor
            # pg.draw.line(self.game.screen, "yellow", (mapScalingWidth * ox, mapScalingHeight * oy),
            #              (mapScalingWidth * ox + depth * mapScalingWidth * cos_a,
            #               mapScalingHeight * oy + depth * mapScalingHeight * sin_a),
            #              2)
            # remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)
            # projection
            projectionHeight = screenDistance / (
                    depth + 0.0001)  # (depth *  value that changes the depth perception of the map)
            #  draw walls
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.game.screen, color,
                         (ray * scale, half_height - projectionHeight // 2, scale, projectionHeight))

            ray_angle += deltaAngle

    def update(self):
        self.ray_cast()
