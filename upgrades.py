import pygame
# class Upgrades():
#     def __init__(self):
#         pass
class Sprites(pygame.sprite.Sprite):
    def __init__(self, screen, text, size, pos):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.text = pygame.font.SysFont(None, 48)
        self.back_image = self.text.render(text, True, (0, 0, 0), (255, 255, 255))
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect().move(pos)
        self.image.blit(self.back_image, self.rect)