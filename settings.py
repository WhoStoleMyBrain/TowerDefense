import pygame
import os


class GameDefaults:
    def __init__(self):
        self.TITLE = 'Tower Defense'
        self.FPS = 60
        self.TILESIZE = 32
        self.TILES_X = 32
        self.TILES_Y = 24
        self.MARGIN = 5
        self.WIDTH = self.TILESIZE * self.TILES_X + 2 * self.MARGIN
        self.HEIGHT = self.TILESIZE * self.TILES_Y + 2 * self.MARGIN
        self.BREAK = -1
        self.WHITE = (255, 255, 255)
        self.GREY = (220, 220, 220)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BGCOLOR = (30, 30, 30)
        self.GRIDWIDTH = 2




class Window:
    def __init__(self):
        gameDefaults = GameDefaults()
        self.WIN = pygame.display.set_mode((gameDefaults.WIDTH, gameDefaults.HEIGHT))
        self.SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')),
                                            (gameDefaults.WIDTH, gameDefaults.HEIGHT))
        pygame.display.set_caption(gameDefaults.TITLE)
