import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()

    # Create updatable and drawable groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set the Player class containers to include both groups
    Player.containers = (updatable, drawable)

    # Asteroids class!
    Asteroid.containers = (asteroids, updatable, drawable)

    # Asteroid field class!
    AsteroidField.containers = (updatable,)


    # Instantiate the player, which will automatically add it to the groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    playing = True
    while playing:
        dt = clock.tick(FPS) / 1000.0  # Calculate delta time

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

        # Clear the screen and draw all objects in the drawable group
        screen.fill(BLACK)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
