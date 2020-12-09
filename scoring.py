import pygame

class Scoring():
    
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