import pygame
from constants import * 

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Set up the game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
