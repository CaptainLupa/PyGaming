import pygame
import globals
import Actor
from UIElement import UIElement as UIE


class Scene:
    def __init__(self):
        self.spriteGroup = pygame.sprite.Group()
        self.uiGroup = pygame.sprite.Group()
        self.bkgndColor = globals.BLUE
        self.buildScene()

    def update(self, dt):
        self.spriteGroup.update(dt=dt)
        self.uiGroup.update()

    def addActor(self, actor: Actor.Actor):
        self.spriteGroup.add(actor)

    def addUIElement(self, uiElement: UIE):
        self.uiGroup.add(uiElement)

    # override in subclass
    def buildScene(self):
        pass

    def draw(self, surface: pygame.surface):
        self.spriteGroup.draw(surface)
        self.uiGroup.draw(surface)
