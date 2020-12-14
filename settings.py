import pygame

class Settings():
    def __init__(self):

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Stupid Clicker")

        # Sound settings
        self.gunshot = pygame.mixer.Sound('assets/gunshot.wav')

        # Score settings
        self.score = 0
        self.super_clicker_quantity = 0

        # Achievement settings
        self.military_bg = pygame.image.load('assets/military_bg.jpg')

        # Upgrade settings
        self.ppc = 1
        self.super_clicker_price = 25

        # Bools
        self.gogo = True
        self.upgrade_screen = False
        self.mute = False
