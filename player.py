import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    containers = ()
    def __init__(self, x, y):
        self.rotation = 0
        super().__init__(x, y, PLAYER_RADIUS)
        self.color = WHITE

        for group in Player.containers:
            group.add(self)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation  += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_KP4]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_KP6]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]  or keys[pygame.K_KP8]:
            self.move(dt, direction=-1)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]  or keys[pygame.K_KP2]:
            self.move(dt)

    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

