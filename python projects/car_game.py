import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Car
car_width, car_height = 50, 100
car_x = (WIDTH - car_width) // 2
car_y = HEIGHT - car_height - 10
car_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw car
    pygame.draw.rect(screen, RED, [car_x, car_y, car_width, car_height])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
