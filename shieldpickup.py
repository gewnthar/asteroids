import pygame
import random
from circleshape import CircleShape
from constants import *

class ShieldPickup(CircleShape):
    containers = () 

    def __init__(self, x, y):
        super().__init__(x, y, 10)
        self.color = (0, 255, 255)  

        for group in ShieldPickup.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        pass

