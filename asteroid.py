import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    containers = ()  # Will be set to include groups for asteroids, etc.

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # Default velocity

        # Add the asteroid to specified groups
        for group in Asteroid.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Move asteroid in a straight line based on its velocity
        self.position += self.velocity * dt

    def split(self):
        # Destroy the current asteroid
        self.kill()

        # If the asteroid is small, don't split further
        if self.radius <= SMALL_ASTEROID_RADIUS:
            return

        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - SMALL_ASTEROID_RADIUS

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocities by rotating the original velocity vector
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Slightly faster
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Slightly faster in the opposite direction

        # Create two new asteroids at the current position with the new radius and velocities
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2

