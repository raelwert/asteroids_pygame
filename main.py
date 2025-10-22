import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    wall_clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    dtForFrame = 0

    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color=(0, 0, 0))

        updatable.update(dtForFrame)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dtForFrame = wall_clock.tick(60) / 1000

        for asteroid in asteroids:
            if asteroid.collided(player):
                print("Game over!")
                sys.exit(0)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collided(shot):
                    shot.kill()
                    asteroid.split()



if __name__ == "__main__":
    main()
