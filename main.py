import pygame
import os

from settings import GameDefaults, Window

gameDefaults = GameDefaults()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption(gameDefaults.TITLE)

mainWindow = Window()


def draw_window():
    mainWindow.WIN.blit(mainWindow.SPACE, (0, 0))


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(gameDefaults.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
        draw_window()


if __name__ == '__main__':
    main()
