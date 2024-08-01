import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Player
player_width, player_height = 50, 50
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Falling Object
object_width, object_height = 50, 50
object_speed = 5
object_frequency = 25  # Add an object every 25 frames
objects = []

# Fonts
font = pygame.font.SysFont(None, 40)

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_width, player_height])

def draw_object(x, y):
    pygame.draw.rect(screen, RED, [x, y, object_width, object_height])

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Game loop
score = 0
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

    # Spawn falling objects
    if random.randint(1, object_frequency) == 1:
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0
        objects.append([object_x, object_y])

    # Move falling objects
    for obj in objects:
        obj[1] += object_speed

    # Check for collisions
    for obj in objects:
        if (
            player_x < obj[0] < player_x + player_width
            and player_y < obj[1] < player_y + player_height
        ):
            objects.remove(obj)
            score += 1

    # Remove objects that go off the screen
    objects = [obj for obj in objects if obj[1] < HEIGHT]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw player and falling objects
    draw_player(player_x, player_y)
    for obj in objects:
        draw_object(obj[0], obj[1])

    # Display the score
    display_score(score)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
