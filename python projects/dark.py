import pygame
import sys
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Light Source")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Light source
light_radius = 150
light_x, light_y = WIDTH // 2, HEIGHT // 2

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw light source
    pygame.draw.circle(screen, YELLOW, (light_x, light_y), light_radius)

    # Draw rays from the light source
    for angle in range(0, 360, 10):
        radian_angle = math.radians(angle)
        end_x = light_x + int(light_radius * math.cos(radian_angle))
        end_y = light_y + int(light_radius * math.sin(radian_angle))
        pygame.draw.line(screen, YELLOW, (light_x, light_y), (end_x, end_y), 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
