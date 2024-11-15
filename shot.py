import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity  # Ensure velocity is stored as an attribute

    def update(self, dt):
        # Ensure x and y are updated
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw using the inherited position
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, width=2)
