import sys
import pygame
from constants import *
from circleshape import *
from asteroids import Asteroid
from asteroidfield import AsteroidField
from player import *

pygame.mixer.quit() #ensure the mixer doesn't initialize

def main():
        pygame.init()
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        
        clock = pygame.time.Clock()
        dt = 0
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()
        # Set a display variable before creating the window
        if not pygame.display.get_init():
            pygame.display.init()
            
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids")
        
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                return
                for thing in updatable:
                        thing.update(dt)
                for asteroid in asteroids:
                        if player.collides_with(asteroid):
                                print("Game over!")
                                sys.exit()
                screen.fill("black")
                for thing in drawable:
                        thing.draw(screen)
                pygame.display.flip()
                dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
