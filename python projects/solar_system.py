import pygame
import sys
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Motion Solar System")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Celestial bodies
class CelestialBody:
    def __init__(self, color, radius, distance, speed):
        self.color = color
        self.radius = radius
        self.distance = distance
        self.speed = speed
        self.angle = 0

    def update(self):
        self.angle += self.speed
        x = int(WIDTH / 2 + self.distance * math.cos(math.radians(self.angle)))
        y = int(HEIGHT / 2 + self.distance * math.sin(math.radians(self.angle)))
        return x, y

sun = CelestialBody(YELLOW, 30, 0, 0)
earth = CelestialBody(WHITE, 10, 150, 1)
moon = CelestialBody(BLUE, 5, 50, 5)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw sun
    sun_position = sun.update()
    pygame.draw.circle(screen, sun.color, sun_position, sun.radius)

    # Draw earth
    earth_position = earth.update()
    pygame.draw.circle(screen, earth.color, earth_position, earth.radius)

    # Draw moon
    moon_position = moon.update()
    moon_position = (earth_position[0] + moon_position[0], earth_position[1] + moon_position[1])
    pygame.draw.circle(screen, moon.color, moon_position, moon.radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
