import pygame
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    wall_clock = pygame.time.Clock()
    dtForFrame = 0

    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        dtForFrame = wall_clock.tick(60)


if __name__ == "__main__":
    main()
