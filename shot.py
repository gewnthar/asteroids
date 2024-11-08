import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    containers = ()  # This will be set to include the shots group

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        # Add the shot to the specified groups
        for group in Shot.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Move the shot in a straight line based on its velocity
        self.position += self.velocity * dt

