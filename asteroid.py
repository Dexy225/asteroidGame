import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS

class Asteroid(CircleShape):
    containers = None  # Will be set in main.py

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(1, 0)  # Default velocity; modify as needed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Kill the current asteroid
        self.kill()

        # If the asteroid is too small, don't split it further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Compute the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the original velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Rotate and increase speed
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Rotate in opposite direction

        # Create two smaller asteroids at the current position with the new velocity
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2