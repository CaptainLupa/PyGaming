import pygame
from pygame import sprite
from typing import Any
from sys import exit


class Actor(sprite.Sprite):
    """Default actor class, basically pygame.sprite.Sprite."""
    def __init__(self, imgName: str = "misato.jpg"):
        super().__init__()
        # noinspection PyBroadException
        try:
            self.originalImage = pygame.image.load(imgName).convert()
            self.image = self.originalImage.copy()
        except:
            print("Failed to load image", imgName)
            exit(66)
        self.rect = self.image.get_rect()
        self.pos = self.rect.x, self.rect.y
        self.velocity = [0, 0]

    def handleInput(self) -> None:
        """Override if needed"""
        pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.handleInput()

        if 'dt' in kwargs:
            self.rect.x = self.velocity[0] * kwargs['dt']
            self.rect.y = self.velocity[1] * kwargs['dt']
