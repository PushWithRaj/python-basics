import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Player
player_width, player_height = 50, 50
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Enemies
enemy_width, enemy_height = 50, 50
enemies = []

def spawn_enemy():
    enemy_x = random.randint(0, WIDTH - enemy_width)
    enemy_y = random.randint(-HEIGHT, 0)
    enemies.append([enemy_x, enemy_y])

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Spawn enemies
    if random.randint(1, 50) == 1:
        spawn_enemy()

    # Move enemies
    for enemy in enemies:
        enemy[1] += 5

    # Check for collisions with enemies
    for enemy in enemies:
        if (
            player_x < enemy[0] < player_x + player_width
            and player_y < enemy[1] < player_y + player_height
        ):
            pygame.quit()
            sys.exit()

    # Remove enemies that go off the screen
    enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw player
    pygame.draw.rect(screen, WHITE, [player_x, player_y, player_width, player_height])

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, [enemy[0], enemy[1], enemy_width, enemy_height])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
