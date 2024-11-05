# https://www.pygame.org/docs/ref/pygame.html
import pygame
from constants import *
from player import Player


def main():
    #initialize pygame before main()
    pygame.init()
    #display.set_mode() makes a GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game Loop Flag! WE GO!
    playing = True
    #Make Go While loop, infinate if you are good enough
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
