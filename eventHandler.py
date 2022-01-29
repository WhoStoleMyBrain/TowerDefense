import pygame
from settings import GameDefaults


class EventHandler:
    def __init__(self):
        self.gameDefaults = GameDefaults()
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return self.gameDefaults.BREAK
