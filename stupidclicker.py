import pygame
import pathlib
from settings import Settings

class game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.declare_objects()
        self.declare_groups()
        self.run()
    
    def declare_objects(self):
        self.score_text = Score(self.settings.score, self.settings.screen, self.settings.bg_color)
        self.click_it = bullshit(self.settings.screen_width//2, self.settings.screen_height//2)
        self.upgrade = upgrades(self.settings.screen)
        self.back_button = back(self.settings.screen)
        self.super_click = double_click(self.settings.screen)

    def declare_groups(self):
        self.click_group = pygame.sprite.GroupSingle(self.click_it)
        self.upgrade_group = pygame.sprite.Group()
        self.upgrade_group.add(self.super_click)
        self.upgrade_group.add(self.back_button)
        

    def run(self):
        while self.settings.gogo:
            self.upgrade_page()
            self.draw(self.settings.screen)
            pygame.display.flip()
            self.event_handler()
        pygame.quit()

    def upgrade_page(self):
        while self.settings.upgrade_screen:
                self.settings.screen.fill(self.settings.bg_color)
                self.upgrade_event_handler()
                self.draw_upgrades(self.settings.screen)
                pygame.display.flip()

    def upgrade_event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings.gogo = False
                self.settings.upgrade_screen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                mouse = mouse_sprite(x, y)
                if pygame.sprite.collide_rect(mouse, self.back_button):
                    self.settings.upgrade_screen = False
                if pygame.sprite.collide_rect(mouse, self.super_click):
                    if self.settings.score >= self.settings.super_clicker_price:
                        self.settings.ppc *= 2
                        self.settings.score -= self.settings.super_clicker_price
                        self.settings.super_clicker_price *= 4
                    else:
                        print('send error message to screen!')

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings.gogo = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                mouse = mouse_sprite(x, y)
                for i in self.click_group:
                    if pygame.sprite.collide_rect(mouse, i):
                        self.settings.gunshot.play()
                        self.settings.score += self.settings.ppc
                    if pygame.sprite.collide_rect(self.upgrade, mouse):
                        self.settings.upgrade_screen = True

    def draw_upgrades(self, surface):
        self.upgrade_group.draw(surface)
        #self.machine_gunner.draw()
        #self.better_machine_gunner.draw()
        #self.even_better_machine_gunner.draw()

    def draw(self, surface):
        self.settings.screen.blit(self.settings.military_bg, self.settings.screen.get_rect())
        self.click_group.draw(surface)
        self.score_text.show_score(self.settings.score)
        self.upgrade.draw()

class back(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.text = pygame.font.SysFont(None, 48)
        self.back_image = self.text.render('Back', True, (0, 0, 0), (255, 255, 255))
        self.image = pygame.Surface((100, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect().move(875, 40)
        self.image.blit(self.back_image, self.rect)


class double_click(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.back_image = pygame.font.SysFont(None, 48).render('Super Clicker', True, (0, 0, 0), (255, 255, 255))
        self.image = pygame.Surface((100, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect().move(25, 40)





class mouse_sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)
        

class Score():

    def __init__(self, score, screen, bg_color):
        
        # Set the dimensions and properties of the score and button.
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = bg_color
        self.score = score
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # The score text
        self.prep_score(score)

    def prep_score(self, score):
        """Turn msg into a rendered image"""
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.screen_rect.center
        self.score_rect.top = 20

    def show_score(self, points):
        # Draw the score
        self.score_image = self.font.render(str(points), True, self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.screen_rect.center
        self.score_rect.top = 20
        self.screen.blit(self.score_image, self.score_rect)
        
#main clicker sprite class
class bullshit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        size = (100, 100)
        self.image = pygame.Surface(size)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect().move(x-size[0]//2, y-size[1]//2)

class upgrades(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        size = (200, 75)
        self.upgrades_image = pygame.font.SysFont(None, 48).render('UPGRADES', True, (0, 0, 0), (255, 0, 0))
        self.image = pygame.Surface(size)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect().move(25, 935)
    
    def draw(self):
        self.screen.blit(self.upgrades_image, self.rect)
        
    
        


if __name__ == "__main__":
    test = game()
