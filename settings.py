import math
from win32api import GetSystemMetrics

# game settings
width = int(GetSystemMetrics(0))
height = int(GetSystemMetrics(1))
halfWidth = width // 2
halfHeight = height // 2
resolution = width, height
# resolution = halfWidth, halfHeight
FPS = 60

playerPosition = 1.5, 5  # mini_map
playerAngle = 0
playerSpeed = 0.004
# playerSpeed = 0.004
playerRotationSpeed = 0.004
# playerRotationSpeed = 0.002
