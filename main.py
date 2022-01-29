import pygame
import os

from settings import GameDefaults, Window
from eventHandler import EventHandler

gameDefaults = GameDefaults()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption(gameDefaults.TITLE)

mainWindow = Window()


def draw_window():
    mainWindow.WIN.blit(mainWindow.SPACE, (0, 0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    eventHandler = EventHandler()
    run = True
    while run:
        clock.tick(gameDefaults.FPS)
        event_return = eventHandler.handle_events(pygame.event.get())
        if event_return == gameDefaults.BREAK:
            run = False
            pygame.quit()
            break
        draw_window()


if __name__ == '__main__':
    main()
