import pygame

class Settings():
    def __init__(self):

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.upgrade_screen = False
        pygame.display.set_caption("Stupid Clicker")

        # Sound settings
        self.gunshot = pygame.mixer.Sound('assets/gunshot.wav')

        # Score settings
        self.score = 0

        # Achievement settings
        self.military_bg = pygame.image.load('assets/military_bg.jpg')

        # Upgrade settings
        self.ppc = 1
        self.super_clicker_price = 25

        # Runs the whole game
        self.gogo = True
