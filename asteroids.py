import pygame
import random
from constants import *
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-1 * random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity_1 * 1.2)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity_2 * 1.2)
        for group in self.groups():
            group.add(new_asteroid_1, new_asteroid_2)
