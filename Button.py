from UIElement import UIElement as UI
from typing import Callable, Any
import pygame


class Button(UI):
    def __init__(self, text: str = "",
                 textSize: int = 25,
                 font: str = "",
                 textColor: tuple = (0, 0, 0),
                 rectColor: tuple = (255, 255, 255),
                 rectSize: tuple = (120, 60),
                 rectPos: tuple = (0, 0),
                 imageName: str = "allahLumine.JPG",
                 action=None,
                 args: list = None,
                 ):
        # -----------------------------------
        super().__init__()
        self.text = text
        self.textColor = textColor
        self.fontObj = pygame.font.SysFont(font, textSize)
        self.rect = pygame.rect.Rect(rectPos, rectSize)
        self.image = pygame.image.load(imageName)
        self.image = pygame.transform.scale(self.image, rectSize)
        self.action = action
        self.args = args

    def update(self, *args: Any, **kwargs: Any) -> None:
        from globals import MOUSE_BUTTONS

        if MOUSE_BUTTONS[0]:
            if self.args is not None:
                self.action(self.args)
            else:
                self.action()
