import pygame



class Tower:

    def __init__(self):
        """Should initialize all relevant variables"""
        pass

    def setSprite(self):
        """Set the sprite used by the tower"""
        pass

    def setProjectile(self):
        """set the projectile that the tower shoots"""
        pass

    def fireProjectile(self):
        """shooting projectiles if an enemy is in range"""
        pass

    def Draw(self, gameDefaults):
        """Draw the current tower to the field in which it is set"""
        pass

"""
class ArrowTower(Tower):

    def __init__(self, x, y):
        super().__init__()
        self.range = 200
        self.damage = 20
        self.level = 1
        self.x = x
        self.y = y
        self.Sprite = (0, 0, 255)
        self.Projectile = (0, 255, 0)

    def Draw(self, gameDefaults):
        left = self.x * gameDefaults.TILESIZE + gameDefaults.MARGIN + gameDefaults.GRIDWIDTH
        top = self.y * gameDefaults.TILESIZE + gameDefaults.MARGIN + gameDefaults.GRIDWIDTH
        rect = pygame.Rect(left, top, gameDefaults.TILESIZE - gameDefaults.GRIDWIDTH,
                           gameDefaults.TILESIZE - gameDefaults.GRIDWIDTH)
        pygame.draw.rect(gameDefaults.mainWindow.WIN, self.Sprite, rect)
"""


class ArrowTower(pygame.sprite.Sprite):

    def __init__(self, picture_path, sound_path, position):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.position = position
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound(sound_path)

    def place(self, tower_group):
        if len(pygame.sprite.spritecollide(self, tower_group, False)) <= 0:
            tower_group.add(self)
        else:
            pass

    def update(self):
        self.rect.center = self.position

