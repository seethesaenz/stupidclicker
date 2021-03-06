import pygame
from settings import Settings
from upgrades import Sprites
from scoring import Scoring


class game():
    def __init__(self):
        pygame.init()
        self.declare_objects()
        self.run()

    def declare_objects(self):
        self.settings = Settings()
        self.score_text = Scoring(self.settings.score, self.settings.screen, self.settings.BLACK)
        self.click_it = bullshit(self.settings.screen_width // 2, self.settings.screen_height // 2)
        self.upgrade = upgrades(self.settings.screen)

        self.upgrade_layout = Sprites(self.settings.screen, 'UPGRADES', (200, 50), (25, 20), self.settings.WHITE)
        self.upgrade_price = Sprites(self.settings.screen, 'PRICE', (200, 50), (245, 20), self.settings.WHITE)
        self.upgrade_quantity = Sprites(self.settings.screen, 'QUANTITY', (200, 50), (465, 20), self.settings.WHITE)
        self.back_button = Sprites(self.settings.screen, 'Back', (100, 50), (875, 90), self.settings.WHITE)
        self.super_clicker = Sprites(self.settings.screen, "Super Clicker", (200, 50), (25, 90), self.settings.RED)
        self.super_clicker_quantity = Sprites(self.settings.screen, f'{self.settings.super_clicker_quantity}', (200, 50), (465, 90), self.settings.WHITE)
        self.super_click_price = Sprites(self.settings.screen, f'{self.settings.super_clicker_price}', (200, 50), (245, 90), self.settings.WHITE)
        self.current_points_per_click_layout = Sprites(self.settings.screen, "C.P.P.C.", (100, 50), (685, 20), self.settings.WHITE)
        self.current_points_per_click = Sprites(self.settings.screen, str(self.settings.ppc), (100, 50), (685, 90), self.settings.WHITE)
        self.declare_groups()
        

    def declare_groups(self):
        self.click_group = pygame.sprite.GroupSingle(self.click_it)
        self.upgrade_group = pygame.sprite.Group()
        self.upgrade_group.add(self.super_clicker)
        self.upgrade_group.add(self.back_button)
        self.upgrade_group.add(self.upgrade_layout)
        self.upgrade_group.add(self.upgrade_price)
        self.upgrade_group.add(self.upgrade_quantity)
        self.upgrade_group.add(self.super_clicker_quantity)
        self.upgrade_group.add(self.super_click_price)
        self.upgrade_group.add(self.current_points_per_click)
        self.upgrade_group.add(self.current_points_per_click_layout)
    def run(self):
        while self.settings.gogo:
            self.upgrade_page()
            self.draw(self.settings.screen)
            pygame.display.flip()
            self.event_handler()
        pygame.quit()

    def update_sprites(self):
        if self.settings.score >= self.settings.super_clicker_price:
            self.super_clicker.update_sprite(None, self.settings.GREEN)
        else:
            self.super_clicker.update_sprite(None, self.settings.RED)
        
        
            

    def upgrade_page(self):
        while self.settings.upgrade_screen:
            self.settings.screen.fill(self.settings.BLACK)
            self.draw_upgrades(self.settings.screen)
            pygame.display.flip()
            self.upgrade_event_handler()
            self.update_sprites()

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
                if pygame.sprite.collide_rect(mouse, self.super_clicker):
                    if self.settings.score >= self.settings.super_clicker_price:
                        self.settings.ppc *= 2
                        self.settings.score -= self.settings.super_clicker_price
                        self.settings.super_clicker_price *= 3
                        self.settings.super_clicker_quantity += 1
                        self.super_clicker_quantity.update_sprite(f'{self.settings.super_clicker_quantity}', None)
                        self.super_click_price.update_sprite(f'{self.settings.super_clicker_price}', None)
                        self.current_points_per_click.update_sprite(str(self.settings.ppc), None)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings.gogo = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                mouse = mouse_sprite(x, y)
                for i in self.click_group:
                    if pygame.sprite.collide_rect(mouse, i):
                        if not self.settings.mute:
                            self.settings.gunshot.play()
                        self.settings.score += self.settings.ppc
                    if pygame.sprite.collide_rect(self.upgrade, mouse):
                        self.settings.upgrade_screen = True

    def draw_upgrades(self, surface):
        self.upgrade_group.draw(surface)

        # self.machine_gunner.draw()
        # self.better_machine_gunner.draw()
        # self.even_better_machine_gunner.draw()

    def draw(self, surface):
        self.settings.screen.blit(self.settings.military_bg, self.settings.screen.get_rect())
        self.click_group.draw(surface)
        self.score_text.show_score(self.settings.score)
        self.upgrade.draw()


class mouse_sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)


# main clicker sprite class
class bullshit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        size = (100, 100)
        self.image = pygame.Surface(size)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect().move(x - size[0] // 2, y - size[1] // 2)


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
