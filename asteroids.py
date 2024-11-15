import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity  # Ensure velocity is stored as an attribute
        self.x = x
        self.y = y
        self.radius = radius
    def update(self, dt):
        # Ensure x and y are updated
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), self.radius, width=2)
