import pygame
from Button import Button
import Scene
from DefaultScene import DefaultScene


class MainMenu(Scene.Scene):
    def __init__(self, main):
        self.startButton = Button(
            action=self.start
        )
        super().__init__()
        self.progMain = main

    def start(self):
        self.progMain.scene = DefaultScene()
        self.progMain.delScene(self)

    def buildScene(self):
        self.uiGroup.add(self.startButton)
