import pygame
import random
import math
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HEX_SIZE = 50
HEX_WIDTH = math.sqrt(3) * HEX_SIZE
HEX_HEIGHT = 1.5 * HEX_SIZE
BACKGROUND_COLOR = (255, 255, 255)
HEX_COLOR = (100, 100, 100)

# Function to draw a hexagon
def draw_hexagon(surface, x, y):
    points = []
    for i in range(6):
        angle_deg = 60 * i +30
        angle_rad = math.pi / 180 * angle_deg
        points.append((x + HEX_SIZE * math.cos(angle_rad),
                       y + HEX_SIZE * math.sin(angle_rad)))
    pygame.draw.polygon(surface, HEX_COLOR, points, 2)

# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Catan Board')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Calculate starting position to center the grid
        start_x = (SCREEN_WIDTH - HEX_WIDTH * 5) / 2
        start_y = (SCREEN_HEIGHT - HEX_HEIGHT * 5) / 2

        # Draw hexagonal grid
        for row in range(5):
            if row == 0 or row == 4:
                num_hexes_in_row = 3
            if row == 1 or row == 3:
                num_hexes_in_row = 4
            if row == 2:
                num_hexes_in_row = 5
            row_offset = abs(2 - row) // 2  # Offset for centering hexagons
            if row == 2:  # Adjust offset for middle row
                row_offset = -1
            for col in range(num_hexes_in_row):
                x = start_x + col * HEX_WIDTH + row_offset * HEX_WIDTH / 2
                y = start_y + row * HEX_HEIGHT
                draw_hexagon(screen, x, y)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

