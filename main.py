import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Set up the game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to manage frame rate
    clock = pygame.time.Clock()

    # Initialize delta time (dt) variable
    dt = 0

    # Instantiate the player object at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop and close the window

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the player on the screen
        player.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate and calculate delta time (dt) in seconds
        dt = clock.tick(60) / 1000  # 60 FPS, convert from ms to seconds

if __name__ == "__main__":
    main()
