import pygame
from constants import *
from circleshape import *
from player import *

pygame.mixer.quit() #ensure the mixer doesn't initialize

def main():
        pygame.init()
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        
        Clock = pygame.time.Clock()
        dt = 0
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
                screen.fill("black")
                player.draw(screen)
                pygame.display.flip()
                dt = (Clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
