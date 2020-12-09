import pygame
import pathlib

class game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Stupid Clicker')

        self.screen_width = 1000
        self.screen_height = 1000

        self.bg_color = (0, 0, 0)
        self.military_bg = pygame.image.load('assets/military_bg.jpg')
        #self.cookie_pic = pygame.image.load('assets/PerfectCookie.jpg')
        self.score = 0
        self.ppc = 1
        self.super_clicker_price = 25


        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.gunshot = pygame.mixer.Sound('assets/gunshot.wav')

        self.declare_objects()
        self.declare_groups()

        self.gogo = True
        self.upgrade_screen = False

        self.run()
    
    def declare_objects(self):
        self.score_text = Score(self.score, self.screen, self.bg_color)
        self.click_it = bullshit(self.screen_width//2, self.screen_height//2)
        self.upgrade = upgrades(self.screen)
        self.back_button = back(self.screen)
        self.super_click = double_click(self.screen)

    def declare_groups(self):
        self.click_group = pygame.sprite.GroupSingle(self.click_it)
        self.upgrade_group = pygame.sprite.Group()
        self.upgrade_group.add(self.super_click)
        self.upgrade_group.add(self.back_button)
        

    def run(self):
        while self.gogo:
            self.upgrade_page()
            self.draw(self.screen)
            pygame.display.flip()
            self.event_handler()
        pygame.quit()

    def upgrade_page(self):
        while self.upgrade_screen:
                self.screen.fill(self.bg_color)
                self.upgrade_event_handler()
                self.draw_upgrades(self.screen)
                pygame.display.flip()

    def upgrade_event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gogo = False
                self.upgrade_screen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                mouse = mouse_sprite(x, y)
                if pygame.sprite.collide_rect(mouse, self.back_button):
                    self.upgrade_screen = False
                if pygame.sprite.collide_rect(mouse, self.super_click):
                    if self.score >= self.super_clicker_price:
                        self.ppc *= 2
                        self.score -= self.super_clicker_price
                        self.super_clicker_price *= 4
                    else:
                        print('send error message to screen!')

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gogo = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                mouse = mouse_sprite(x, y)
                for i in self.click_group:
                    if pygame.sprite.collide_rect(mouse, i):
                        self.gunshot.play()
                        self.score += self.ppc
                    if pygame.sprite.collide_rect(self.upgrade, mouse):
                        self.upgrade_screen = True

    def draw_upgrades(self, surface):
        self.upgrade_group.draw(surface)
        #self.machine_gunner.draw()
        #self.better_machine_gunner.draw()
        #self.even_better_machine_gunner.draw()

    def draw(self, surface):
        self.screen.blit(self.military_bg, self.screen.get_rect())
        self.click_group.draw(surface)
        self.score_text.show_score(self.score)
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
