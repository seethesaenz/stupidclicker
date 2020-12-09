import pygame
# class Upgrades():
#     def __init__(self):
#         pass
class Sprites(pygame.sprite.Sprite):
    def __init__(self, screen, text, size, pos):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(center = pos)
        self.image.fill((255, 255, 255))
        self.text_font = pygame.font.SysFont(None, 36)
        self.text_surf = self.text_font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.image.blit(self.text_surf, self.text_rect)