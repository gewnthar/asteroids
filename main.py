import pygame
import sys
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from shieldpickup import ShieldPickup  # Import ShieldPickup class

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()

    # Create groups for updatable, drawable, asteroids, shots, and shield pickups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shield_pickups = pygame.sprite.Group()  # New group for shields

    # Set containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    ShieldPickup.containers = (shield_pickups, drawable)

    # Initialize game elements
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score = Score()

    playing = True
    while playing:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        # Randomly spawn shield pickups
        if random.random() < SHIELD_SPAWN_RATE:
            x, y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
            ShieldPickup(x, y)

        # Update all objects
        for obj in updatable:
            obj.update(dt)

        # Check collisions between player and shield pickups
        for shield in shield_pickups:
            if player.check_collision(shield):
                player.add_shield(MAX_SHIELD_STRENGTH // 2)  # Add half the max shield strength
                shield.kill()  # Remove the shield pickup

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                # Determine damage based on asteroid size
                if asteroid.radius >= LARGE_ASTEROID_RADIUS:
                    player.take_damage(LARGE_ASTEROID_DAMAGE)
                elif asteroid.radius >= MEDIUM_ASTEROID_RADIUS:
                    player.take_damage(MEDIUM_ASTEROID_DAMAGE)
                else:
                    player.take_damage(SMALL_ASTEROID_DAMAGE)
                
                asteroid.split()  # Split asteroid on collision

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    if asteroid.radius == LARGE_ASTEROID_RADIUS:
                        score.add_points(LARGE_ASTEROID_POINTS)
                    elif asteroid.radius == MEDIUM_ASTEROID_RADIUS:
                        score.add_points(MEDIUM_ASTEROID_POINTS)
                    else:
                        score.add_points(SMALL_ASTEROID_POINTS)

                    asteroid.split()
                    shot.kill()
                    break

        # Render all objects
        screen.fill(BLACK)
        for obj in drawable:
            obj.draw(screen)

        # Draw the score and optionally the shield level on the screen
        score.draw(screen)
        shield_text = pygame.font.Font(None, 30).render(f"Shield: {player.shield}", True, WHITE)
        screen.blit(shield_text, (10, 40))  # Display shield level below score

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
