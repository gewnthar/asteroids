import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,0)

        for group in Asteroid.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius, 2)


    def update(self,dt):
        self.position += self.velocity * dt
