import pygame
from ball import Ball

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Control FPS
clock = pygame.time.Clock()

# Create ball object
ball = Ball(WIDTH, HEIGHT)

running = True
while running:
    # White background
    screen.fill((255, 255, 255))

    # Handle system events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move ball using arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -ball.speed)
            elif event.key == pygame.K_DOWN:
                ball.move(0, ball.speed)
            elif event.key == pygame.K_LEFT:
                ball.move(-ball.speed, 0)
            elif event.key == pygame.K_RIGHT:
                ball.move(ball.speed, 0)

    # Draw ball on screen
    ball.draw(screen)

    # Update display
    pygame.display.flip()

    # Limit FPS for smooth movement
    clock.tick(60)

pygame.quit()