from spriteObject import *

class ObjectHandler:
    def __init__(self,game):
        self.game = game
        self.spriteList = []
        self.staticSpritePath = 'resources/sprites/static_sprites/'
        self.animatedSpritePath = 'resources/sprites/animated_sprites/'
        addSprites = self.addSprites

        #  Sprite Map
        addSprites(SpriteObject(game))
        addSprites(AnimatedSprites(game))

    def update(self):
        [sprite.update() for sprite in self.spriteList]

    def addSprites(self, sprite):
        self.spriteList.append(sprite)
