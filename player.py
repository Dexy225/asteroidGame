import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=20)
        self.rotation = 0
        self.shoot_timer = 0  # Timer to manage the cooldown between shots

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt, direction):
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360  # Keep rotation between 0 and 360 degrees

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        if self.shoot_timer > 0:
            return  # Prevent shooting if the timer is still active

        # Create a new shot at the player's position
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOOT_SPEED

        # Create the shot and add it to the appropriate group automatically
        Shot(self.position.x, self.position.y, velocity)

        # Reset the timer to the cooldown value
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)
        if keys[pygame.K_d]:
            self.rotate(dt, 1)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
            self.move(dt, -1)

        # Check if the spacebar is pressed and shoot if possible
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Decrease the shoot timer by dt
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
