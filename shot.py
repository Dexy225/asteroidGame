import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    containers = None  # This will be set in main.py

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)  # Use SHOT_RADIUS as the size of the bullet
        self.velocity = velocity  # Set the velocity for the shot

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        # Move the shot in the direction of its velocity
        self.position += self.velocity * dt
