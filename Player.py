import Actor
import pygame


class Player(Actor.Actor):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(self.image, (200, 200))

    def handleInput(self):
        from globals import KEYS_PRESSED

        self.velocity = [0, 0]

        if KEYS_PRESSED[pygame.K_RIGHT]:
            self.velocity[0] += 5
        if KEYS_PRESSED[pygame.K_LEFT]:
            self.velocity[0] += -5
        if KEYS_PRESSED[pygame.K_UP]:
            self.velocity[1] += -5
        if KEYS_PRESSED[pygame.K_DOWN]:
            self.velocity[1] += 5

        self.velocity[0] = min(5, max(-5, self.velocity[0]))
        self.velocity[1] = min(5, max(-5, self.velocity[1]))

        if KEYS_PRESSED[pygame.K_k]:
            # shooty
            pass
