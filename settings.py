import math
from win32api import GetSystemMetrics

# game settings
windowSize = "1080p"
# windowSize = "720p"

if windowSize == "1080p":
    width = int(GetSystemMetrics(0))
    height = int(GetSystemMetrics(1))
elif windowSize == "720p":
    width = int(GetSystemMetrics(0)) // 2
    height = int(GetSystemMetrics(1)) // 2

resolution = width, height
half_width = int(width / 2)
half_height = int(height / 2)
FPS = 60
playerPosition = 1.5, 1.5  # mini_map
playerAngle = 0
playerSpeed = 0.004
playerRotationSpeed = 0.004
playerSizeScale = 180
# raycasting settings
FOV = math.pi / 3
halfFOV = FOV / 2
noOfRays = width // 2
halfNoOfRays = noOfRays // 2
deltaAngle = FOV / noOfRays
maxDepth = 40
screenDistance = half_width / math.tan(halfFOV)
scale = width // noOfRays

# texture
textureSize = 256
half_textureSize = textureSize//2

#  Mouse settings
mouseSensitivity = 0.0003
mouseMaxRel = 100
mouseBorderLeft = 0
mouseBorderRight = width - mouseBorderLeft
