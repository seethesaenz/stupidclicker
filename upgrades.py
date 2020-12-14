import pygame
from settings import Settings
# class Upgrades():
#     def __init__(self):
#         pass
class Sprites(pygame.sprite.Sprite):
    def __init__(self, screen, text, size, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()
        self.text =text
        self.size = size
        self.pos = pos
        self.screen = screen
        self.image = pygame.Surface(size)
        self.color = color
        self.rect = self.image.get_rect().move(pos[0], pos[1])
        self.image.fill(self.color)
        self.text_font = pygame.font.SysFont(None, 36)
        self.text_surf = self.text_font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (size[0]//2, size[1]//2)
        self.image.blit(self.text_surf, self.text_rect)

    def update_sprite(self, text, color):
        # Draw the score
        if color == None:
            color = self.color
        if text == None:
            text = self.text
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect().move(self.pos[0], self.pos[1])
        self.image.fill(color)
        self.text_font = pygame.font.SysFont(None, 36)
        self.text_surf = self.text_font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (self.size[0]//2, self.size[1]//2)
        self.image.blit(self.text_surf, self.text_rect)