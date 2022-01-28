import pygame
import os


class GameDefaults:
    def __init__(self):
        self.TITLE = 'Tower Defense'
        self.FPS = 60
        self.WIDTH = 900
        self.HEIGHT = 500


class Window:
    def __init__(self):
        gamedefaults = GameDefaults()
        self.WIN = pygame.display.set_mode((gamedefaults.WIDTH, gamedefaults.HEIGHT))
        self.SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')),
                                            (gamedefaults.WIDTH, gamedefaults.HEIGHT))
