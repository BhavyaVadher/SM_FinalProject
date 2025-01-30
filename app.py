import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Triangle")

# Colors.
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Physics parameters
GRAVITY = 0.5
DAMPING = 0.8

class Triangle:
    def __init__(self, center, size):
        self.center = pygame.Vector2(center)
        self.size = size
        self.angle = 0
        self.rotation_speed = 1  # degrees per frame

    def get_vertices(self):
        vertices = []
        for i in range(3):
            angle_deg = 120 * i + self.angle
            angle_rad = math.radians(angle_deg)
            x = self.center.x + self.size * math.cos(angle_rad)
            y = self.center.y + self.size * math.sin(angle_rad)
            vertices.append(pygame.Vector2(x, y))
        return vertices

    def rotate(self):
        self.angle += self.rotation_speed
        if self.angle >= 360:
            self.angle -= 360

    def draw(self, surface):
        pygame.draw.polygon(surface, WHITE, self.get_vertices(), 2)

class Ball:
    def __init__(self, position, radius):
        self.pos = pygame.Vector2(position)
        self.vel = pygame.Vector2(0, 0)
        self.radius = radius

    def update(self, triangle):
        self.vel.y += GRAVITY
        self.pos += self.vel

        # Check collisions with triangle edges
        vertices = triangle.get_vertices()
        for i in range(3):
            a = vertices[i]
            b = vertices[(i+1)%3]
            self.resolve_collision(a, b)

    def resolve_collision(self, a, b):
        # Find closest point on the edge segment
        edge = b - a
        to_ball = self.pos - a
        t = max(0, min(1, to_ball.dot(edge) / edge.length_squared()))
        closest = a + t * edge

        # Check collision
        dist_vec = self.pos - closest
        distance = dist_vec.length()
        if distance < self.radius:
            # Collision response
            normal = dist_vec.normalize()
            self.pos = closest + normal * self.radius
            self.vel -= 2 * self.vel.dot(normal) * normal * DAMPING

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.pos.x), int(self.pos.y)), self.radius)

# Create objects
triangle = Triangle((WIDTH//2, HEIGHT//2), 250)
ball = Ball((WIDTH//2, HEIGHT//2 - 100), 15)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update objects
    triangle.rotate()
    ball.update(triangle)

    # Draw everything
    screen.fill(BLACK)
    triangle.draw(screen)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()