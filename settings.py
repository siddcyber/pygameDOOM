# game settings
from win32api import GetSystemMetrics
width = int(GetSystemMetrics(0) / 2)
height = int(GetSystemMetrics(1) / 2)
resolution = width, height
frameRate = 60
playerPosition = 1.5, 5  # mini map
playerAngle = 0
playerSpeed = 1
playerRotationSpeed = 1
