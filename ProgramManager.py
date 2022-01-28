import pygame
import sys
import globals
import Scene
import DefaultScene


class ProgramManager:
    def __init__(self):
        self.screen = pygame.display.set_mode(globals.SIZE)
        self.scene = DefaultScene.DefaultScene()
        self.clock = pygame.time.Clock()

    def mainLoop(self):
        fps = pygame.font.SysFont("", 25)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            globals.KEYS_PRESSED = pygame.key.get_pressed()

            self.scene.update(self.clock.get_time())
            # print(self.clock.get_time())

            self.screen.fill(self.scene.bkgndColor)
            self.scene.draw(self.screen)
            self.screen.blit(fps.render(str(round(self.clock.get_fps())), True, (255, 255, 255)), (0, 0))
            self.clock.tick()
            pygame.display.flip()

    def changeScene(self, scene: Scene.Scene):
        self.scene = scene
