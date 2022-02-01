import pygame
from settings import GameDefaults
from Tower import ArrowTower
import os


class EventHandler:
    def __init__(self):
        pass

    def handle_events(self, events, game):
        for event in events:
            if event.type == pygame.QUIT:
                game.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x_grid, y_grid = game.transformKoordinatesToSquares(x, y)
                x_snapped, y_snapped = game.transformSquaresToCoordinates((x_grid, y_grid))
                arrow_tower = ArrowTower(os.path.join('Assets', 'axeDouble2.png'),
                                         os.path.join('Assets', 'Grenade+1.mp3'), (x_snapped, y_snapped),
                                         (game.gameDefaults.TILESIZE - game.gameDefaults.GRIDWIDTH,
                                          game.gameDefaults.TILESIZE - game.gameDefaults.GRIDWIDTH))
                arrow_tower.place(game.Towers)
                #  square_x, square_y = game.transformKoordinatesToSquares(x, y)
                #  print(f'Square {square_x}, {square_y} was filled in yellow.')



