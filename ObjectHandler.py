from spriteObject import *
from Map import minimap
class ObjectHandler:
    def __init__(self,game):
        self.game = game
        self.spriteList = []
        self.staticSpritePath = 'resources/sprites/static_sprites/'
        self.animatedSpritePath = 'resources/sprites/animated_sprites/'
        addSprites = self.addSprites

        #  Sprite Map pos(width, height)
        # addSprites(SpriteObject(game))
        # addSprites(AnimatedSprites(game))
        addSprites(AnimatedSprites(game, pos=(1.08, 1.08)))
        addSprites(AnimatedSprites(game, pos=(1.08, 1.9)))
        addSprites(AnimatedSprites(game, pos=(7, 1.08)))
        addSprites(AnimatedSprites(game, pos=(10, 1.9)))
        addSprites(AnimatedSprites(game, pos=((len(minimap[0])-1.02), 1.08)))
        # addSprites(AnimatedSprites(game, pos=(10, 1.9)))
        # addSprites(AnimatedSprites(game, pos=(5.5, 3.25)))
        # addSprites(AnimatedSprites(game, pos=(5.5, 4.75)))
        # addSprites(AnimatedSprites(game, pos=(7.5, 2.5)))
        # addSprites(AnimatedSprites(game, pos=(7.5, 5.5)))
        # addSprites(AnimatedSprites(game, pos=(14.5, 1.5)))
        # addSprites(AnimatedSprites(game, pos=(14.5, 4.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(14.5, 5.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(14.5, 7.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(12.5, 7.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(9.5, 7.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(14.5, 12.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(9.5, 20.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(10.5, 20.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(3.5, 14.5)))
        # addSprites(AnimatedSprites(game, path=self.animatedSpritePath + 'red_light/0.png', pos=(3.5, 18.5)))
        # addSprites(AnimatedSprites(game, pos=(14.5, 24.5)))
        # addSprites(AnimatedSprites(game, pos=(14.5, 30.5)))
        # addSprites(AnimatedSprites(game, pos=(1.5, 30.5)))
        # addSprites(AnimatedSprites(game, pos=(1.5, 24.5)))

    def update(self):
        [sprite.update() for sprite in self.spriteList]

    def addSprites(self, sprite):
        self.spriteList.append(sprite)
