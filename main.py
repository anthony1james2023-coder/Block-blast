import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Block:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.color = random.choice([RED, GREEN, BLUE])

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Game Initialization  
def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Block Blast')
    return screen

# Main Game Loop  
def main_loop(screen):
    clock = pygame.time.Clock()
    blocks = [Block(random.randint(0, SCREEN_WIDTH - BLOCK_SIZE), random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)) for _ in range(10)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)  # Clear screen
        for block in blocks:
            block.draw(screen)

        pygame.display.flip()  # Update display
        clock.tick(60)  # Maintain 60 FPS

    pygame.quit()

# Main Entry Point  
if __name__ == '__main__':
    screen = initialize_game()
    main_loop(screen)
