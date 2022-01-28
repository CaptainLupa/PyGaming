import pygame
import globals


class Scene:
    def __init__(self):
        self.spriteGroup = pygame.sprite.Group()
        self.bkgndColor = globals.BLUE
        self.buildScene()

    def update(self, dt):
        self.spriteGroup.update(dt=dt)

    def addSprite(self, sprite: pygame.sprite.Sprite):
        self.spriteGroup.add(sprite)

    # override in subclass
    def buildScene(self):
        pass

    def draw(self, surface: pygame.surface):
        self.spriteGroup.draw(surface)
