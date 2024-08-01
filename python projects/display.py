import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hacker Display")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Characters
characters = "!@#$%^&*()_-+=~`,./<>?;:'\"[{}]\\|"
font = pygame.font.SysFont("monospace", 24)

# Text particles
particles = []

# Particle class
class Particle:
    def __init__(self, x, y, char, speed):
        self.x = x
        self.y = y
        self.char = char
        self.speed = speed

    def update(self):
        self.y += self.speed

# Generate initial particles
for _ in range(50):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    char = random.choice(characters)
    speed = random.randint(1, 5)
    particles.append(Particle(x, y, char, speed))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw and update particles
    for particle in particles:
        text_surface = font.render(particle.char, True, GREEN)
        screen.blit(text_surface, (particle.x, particle.y))
        particle.update()

        # Reset particle position if it goes off the screen
        if particle.y > HEIGHT:
            particle.y = 0
            particle.x = random.randint(0, WIDTH)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
