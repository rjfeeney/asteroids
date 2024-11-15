import pygame

pygame.display.init()  # Only initialize the display module
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Test Window')

# Add a basic event loop to prevent immediate closing
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
