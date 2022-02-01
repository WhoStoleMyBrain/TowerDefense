import pygame
import os


class Core:
    """
        The core class is the first entry point to the whole game.
        It handles the game settings, game data, windows and more. Everything comes together at the core.
    """

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.Settings = Settings()
        self.playing = False
        self.clock = pygame.time.Clock()
        self.Window = Window(self.Settings)
        self.Towers = pygame.sprite.Group()

    def setWindow(self, window):
        self.Window = window(self.Settings)


class Settings:
    """
        The settings saves the settings of the game. Resolution, window size and others are important
    """
    def __init__(self):
        self.TITLE = 'Tower Defense'
        self.FPS = 60
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.COLORS = {}
        self.setColors()
        self.BGCOLOR = self.COLORS['GREY']

    def setColors(self):
        self.COLORS['WHITE'] = (255, 255, 255)
        self.COLORS['GREY'] = (220, 220, 220)
        self.COLORS['BLACK'] = (0, 0, 0)
        self.COLORS['RED'] = (255, 0, 0)
        self.COLORS['YELLOW'] = (255, 255, 0)
        self.COLORS['GREY'] = (30, 30, 30)


class EventHandler:
    def __init__(self):
        pass

    def handleEvents(self, events, core):
        for event in events:
            if event.type == pygame.QUIT:
                core.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x_grid, y_grid = core.Window.GameData.transformKoordinatesToSquares(x, y)
                x_snapped, y_snapped = core.Window.GameData.transformSquaresToCoordinates((x_grid, y_grid))
                arrow_tower = ArrowTower(os.path.join('Assets', 'axeDouble2.png'),
                                         os.path.join('Assets', 'Grenade+1.mp3'), (x_snapped, y_snapped),
                                         (core.Window.GameData.TILESIZE - core.Window.GameData.GRIDWIDTH,
                                          core.Window.GameData.TILESIZE - core.Window.GameData.GRIDWIDTH))
                arrow_tower.place(core.Window.GameData.Towers)


class Window:
    """
        The Window class holds all elements relevant for displaying any window.
        This can be the main window, but also be the game window
    """
    def __init__(self, settings):
        self.Settings = settings
        self.WIN = pygame.display.set_mode((self.Settings.WIDTH, self.Settings.HEIGHT))
        self.GameData = GameData(self.Settings)
        pygame.display.set_caption(self.Settings.TITLE)

    def drawWindow(self):
        self.WIN.fill(self.Settings.BGCOLOR)#WIN.blit(self.Window.SPACE, (0, 0))
        self.drawGrid()
        self.GameData.Draw(self.WIN)
        pygame.display.flip()  # Can use pygame.display.update(), which can update single elements of the display

    def drawGrid(self):
        for grid_x in range(self.GameData.TILES_X + 1):
            x = grid_x * self.GameData.TILESIZE + self.GameData.MARGIN
            self.drawLine((x, self.GameData.MARGIN), (x, self.Settings.HEIGHT - self.GameData.MARGIN))

        for grid_y in range(self.GameData.TILES_Y + 1):
            y = grid_y * self.GameData.TILESIZE + self.GameData.MARGIN
            self.drawLine((self.GameData.MARGIN, y), (self.Settings.WIDTH - self.GameData.MARGIN, y))

    def drawLine(self, point1, point2):
        pygame.draw.line(self.WIN, self.Settings.COLORS['WHITE'], point1, point2,
                         width=self.GameData.GRIDWIDTH)


class GameData:
    """
        In GameData the relevant Data for the game are stored.
        While Towers, Enemies and Projectiles are part of this class,
        other information such as the Players Life, Money and more is saved here.
    """
    def __init__(self, settings):
        self.TILESIZE = 32
        self.Settings = settings
        self.MARGIN = 5
        self.TILES_X = (self.Settings.WIDTH - 2 * self.MARGIN) // self.TILESIZE #  59
        self.TILES_Y = (self.Settings.HEIGHT - 2 * self.MARGIN) // self.TILESIZE
        self.GRIDWIDTH = 2
        self.Towers = pygame.sprite.Group()

    def transformKoordinatesToSquares(self, x, y):
        square_x = (x - self.MARGIN) // self.TILESIZE
        square_y = (y - self.MARGIN) // self.TILESIZE
        return square_x, square_y

    def transformSquaresToCoordinates(self, position_square):
        x = position_square[0] * self.TILESIZE + self.MARGIN + self.GRIDWIDTH
        y = position_square[1] * self.TILESIZE + self.MARGIN + self.GRIDWIDTH
        return x, y

    def Draw(self, WIN):
        self.Towers.update()
        self.Towers.draw(WIN)


class Sound:
    def __init__(self):
        pass


class LevelSettings:
    """
        The settings required for the different levels are saved here.
        To be more precise, the settings should be loaded from a file.
        Saving to a file would also enable a custom world editor.
    """
    def __init__(self):
        pass


class Tower:
    def __init__(self):
        pass


class ArrowTower(pygame.sprite.Sprite):
    def __init__(self, picture_path, sound_path, position, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), size)
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.sound = pygame.mixer.Sound(sound_path)

    def place(self, tower_group):
        collided_sprites = pygame.sprite.spritecollide(self, tower_group, False)
        if len(collided_sprites) <= 0:
            tower_group.add(self)
        else:
            tower_group.remove(collided_sprites[0])

    def update(self):
        self.rect.topleft = self.position


class Enemy:
    def __init__(self):
        pass


class Projectile:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pass


def main():
    core = Core()
    clock = pygame.time.Clock()
    eventhandler = EventHandler()
    core.playing = True
    while core.playing:
        clock.tick(core.Settings.FPS)

        eventhandler.handleEvents(pygame.event.get(), core)
        if not core.playing:
            pygame.quit()
            break
        core.Window.drawWindow()


if __name__ == '__main__':
    main()
