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
        self.position += self.velocity * dt
    
    def draw(self, screen):
        # Draw using the inherited position
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
