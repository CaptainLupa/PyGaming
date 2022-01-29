import pygame
import sys
import globals
import Scene
import DefaultScene
import MainMenu


class ProgramManager:
    def __init__(self):
        self.screen = pygame.display.set_mode(globals.SIZE)
        self.aspectRatio = globals.WIDTH / globals.HEIGHT
        self.clock = pygame.time.Clock()
        self.scene = MainMenu.MainMenu(self)

    def mainLoop(self):
        fps = pygame.font.SysFont("", 25)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    sys.exit()

            globals.KEYS_PRESSED = pygame.key.get_pressed()
            globals.MOUSE_BUTTONS = pygame.mouse.get_pressed()
            globals.MOUSE_POS = pygame.mouse.get_pos()

            self.scene.update(self.clock.get_time())
            # print(self.clock.get_time())

            self.screen.fill(self.scene.bkgndColor)
            self.scene.draw(self.screen)
            self.screen.blit(fps.render(str(round(self.clock.get_fps())), True, (255, 255, 255)), (0, 0))
            self.clock.tick()
            pygame.display.flip()

    def changeScene(self, scene: Scene.Scene):
        self.scene = scene

    @staticmethod
    def delScene(scene):
        del scene
