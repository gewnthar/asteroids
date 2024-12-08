import pygame
from constants import WHITE

class Score:
    def __init__(self, font_size=30):
        # Initialize the score
        self.score = 0
        # Set up the font for displaying the score
        self.font = pygame.font.Font(None, font_size)

    def add_points(self, points):
        # Increase the score by the given number of points
        self.score += points

    def draw(self, screen, color=(255, 255,255)):
        # Render the score text
        score_text = self.font.render(f"Score: {self.score}", True, color)
        # Display it at the top-left corner of the screen
        screen.blit(score_text, (10, 10))

    def reset(self):
        # Reset the score to zero
        self.score = 0
