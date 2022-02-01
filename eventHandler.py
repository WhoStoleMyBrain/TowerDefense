import pygame
from settings import GameDefaults
from Tower import ArrowTower
import os


class EventHandler:
    def __init__(self):
        self.gameDefaults = GameDefaults()
        pass

    def handle_events(self, events, game):
        for event in events:
            if event.type == pygame.QUIT:
                game.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                arrow_tower = ArrowTower(os.path.join('Assets', 'axeDouble2.png'),
                                         os.path.join('Assets', 'Grenade+1.mp3'), (x, y),
                                         (game.gameDefaults.TILESIZE, game.gameDefaults.TILESIZE) )
                arrow_tower.place(game.Towers)
                square_x, square_y = game.transformKoordinatesToSquares(x, y)
                """
                
                if (square_x, square_y) in game.squares:
                    game.squares.remove((square_x, square_y))
                else:
                    game.squares.append((square_x, square_y))
                #game.fillSquare(square_x, square_y)
                """
                print(f'Square {square_x}, {square_y} was filled in yellow.')



