import Actor
import pygame


class Player(Actor.Actor):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(self.image, (200, 200))

    def handleInput(self):
        from globals import KEYS_PRESSED

        self.velocity = [0, 0]

        if KEYS_PRESSED[pygame.K_d]:
            self.velocity[0] += 5
        if KEYS_PRESSED[pygame.K_a]:
            self.velocity[0] += -5
        if KEYS_PRESSED[pygame.K_w]:
            self.velocity[1] += -5
        if KEYS_PRESSED[pygame.K_s]:
            self.velocity[1] += 5

        self.velocity[0] = min(5, max(-5, self.velocity[0]))
        self.velocity[1] = min(5, max(-5, self.velocity[1]))

        # print(self.velocity)

        if KEYS_PRESSED[pygame.K_k]:
            # shoot
            pass
