import Actor
import pygame


class Player(Actor.Actor):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(self.image, (200, 200))

    def handleInput(self):
        from globals import KEYS_PRESSED
        if KEYS_PRESSED[pygame.K_RIGHT]:
            self.velocity[0] = 5
        if KEYS_PRESSED[pygame.K_LEFT]:
            self.velocity[0] = -5
        if KEYS_PRESSED[pygame.K_UP]:
            self.velocity[1] = -5
        if KEYS_PRESSED[pygame.K_DOWN]:
            self.velocity[1] = 5
