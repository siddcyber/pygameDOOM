from spriteObject import *
class Weapon(AnimatedSprites):
    def __init__(self,game, path='resources/sprites/weapon/shotgun/0.png', scale=0.4, animationTime=80):
        super().__init__(game=game, path=path, scale=scale, animationTime=animationTime)
        self.images = deque(
            [pg.transform.smoothscale(img, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
             for img in self.images])
        self.weaponPosition = (half_width - self.images[0].get_width() // 2, height - self.images[0].get_height())
        self.reloading = False
        self.numImages = len(self.images)
        self.frame_counter = 0
        self.damage = 50

    def animateShot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animationTrigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.numImages:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weaponPosition)

    def update(self):
        self.checkAnimationTime()
        self.animateShot()
        