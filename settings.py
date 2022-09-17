import math
from win32api import GetSystemMetrics

# game settings
width = int(GetSystemMetrics(0))
height = int(GetSystemMetrics(1))
resolution = width, height
HALF_width = width // 2
HALF_HEIGHT = height // 2
FPS = 60

playerPosition = 1.5, 5  # mini_map
playerAngle = 0
playerSpeed = 1
# playerSpeed = 0.004
playerRotationSpeed = 1
# playerRotationSpeed = 0.002
