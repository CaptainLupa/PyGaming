import Actor
import pygame


class Player(Actor.Actor):
    def __init__(self):
        super().__init__()
        self.fo = pygame.font.SysFont("", 40)
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.image.blit(self.fo.render("Fart", True, (255, 255, 255)), (0, 0))
        self.textRendered = True

    def toggleText(self):
        if self.textRendered:
            self.image = self.originalImage
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.textRendered = False
        else:
            self.image.blit(self.fo.render("Fart", True, (255, 255, 255)), (0, 0))
            self.textRendered = True

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
            self.toggleText()
