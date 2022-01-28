import pygame
import ProgramManager


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pm = ProgramManager.ProgramManager()
    pm.mainLoop()
