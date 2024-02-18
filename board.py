import pygame
import random
import math
pygame.init()

# screenWidth = 1000
# screenLength = 800
# color = (250,250,250)
# screen = pygame.display.set_mode((screenWidth, screenLength))


# run = True

# Constants
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

# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     screen.fill(color)
#     pygame.display.flip()
# pygame.quit()
#
# class Board:
#
#     def random_board(self):
#         tiles = ['desert', 'wood', 'wood', 'wood', 'wood', 'sheep', 'sheep', 'sheep', 'sheep', 'wheat', 'wheat', 'wheat', 'wheat', 'brick', 'brick', 'brick', 'ore', 'ore', 'ore']
#         probs = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
#         board = [[], [], [], []]
#         row_lengths = [3, 4, 5, 4, 3]
#         for i in range(5):
#             while len(board[i]) < row_lengths[i]:
#                 tile = random.choice(tiles)
#                 board[i].append(tile)
#                 tiles.remove(tile)
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 if board[i][j] != 'desert':
#                     number = random.choice(probs)
#                     board[i][j] += f' {number}'
#                     probs.remove(number)

