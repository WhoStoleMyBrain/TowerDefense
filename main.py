import pygame
import os
import sys

from settings import GameDefaults, Window
from eventHandler import EventHandler


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.gameDefaults = GameDefaults()
        self.playing = False
        self.clock = pygame.time.Clock()
        self.mainWindow = Window()

    def mainFrame(self):
        pass

    def drawWindow(self):
        self.mainWindow.WIN.fill(self.gameDefaults.BGCOLOR)#WIN.blit(self.mainWindow.SPACE, (0, 0))
        self.drawGrid()
        pygame.display.flip()  # Can use pygame.display.update()


    def drawGrid(self):
        for grid_x in range(self.gameDefaults.TILES_X + 1):
            x = grid_x * self.gameDefaults.TILESIZE + self.gameDefaults.MARGIN
            self.drawLine((x, self.gameDefaults.MARGIN), (x, self.gameDefaults.HEIGHT - self.gameDefaults.MARGIN))

        for grid_y in range(self.gameDefaults.TILES_Y + 1):
            y = grid_y * self.gameDefaults.TILESIZE + self.gameDefaults.MARGIN
            self.drawLine((self.gameDefaults.MARGIN, y), (self.gameDefaults.WIDTH - self.gameDefaults.MARGIN, y))

    def drawLine(self, point1, point2):
        pygame.draw.line(self.mainWindow.WIN, self.gameDefaults.WHITE, point1, point2,
                         width=self.gameDefaults.GRIDWIDTH)



def main():
    game = Game()
    clock = pygame.time.Clock()
    eventhandler = EventHandler()
    game.playing = True
    while game.playing:
        game.mainFrame()
        clock.tick(game.gameDefaults.FPS)
        eventhandler.handle_events(pygame.event.get(), game)
        if not game.playing:
            pygame.quit()
            break
        game.drawWindow()


if __name__ == '__main__':
    main()
