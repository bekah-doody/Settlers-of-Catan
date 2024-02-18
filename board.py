import pygame
import random
import math
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HEX_SIZE = 50
HEX_WIDTH = math.sqrt(3) * HEX_SIZE
HEX_HEIGHT = 1.5 * HEX_SIZE
BACKGROUND_COLOR = (0, 157, 196)
HEX_COLOR = (100, 100, 100)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 36
FONT_STYLE = 'Arial'
START_TEXT = "Settlers of Catan \n\n  Press Space to Start\n\n Bekah Doody \n Drew Baine \n Jason Miranda"

COLOR_QUANTITIES = {
    (255, 0, 0): 3, #red -> bricks
    (0, 255, 0): 4, #green -> sheep
    (139, 69, 19): 4, #brown -> wood
    (176, 196, 222):3, #blue-gray -> mountains
    (255, 255, 0): 4, #yellow -> wheat
    (229, 201, 159): 1, #white -desert
}
# Function to draw a hexagon
def generate_hexagon_colors():
    hexagon_colors = []
    colors = list(COLOR_QUANTITIES.keys())  # Get list of colors
    for color, quantity in COLOR_QUANTITIES.items():
        hexagon_colors.extend([color] * quantity)  # Add each color to the list the specified number of times
    random.shuffle(hexagon_colors)  # Shuffle the list of colors
    return hexagon_colors

def draw_hexagon(surface, x, y, color):
    points = []
    for i in range(6):
        angle_deg = 60 * i + 30
        angle_rad = math.pi / 180 * angle_deg
        points.append((x + HEX_SIZE * math.cos(angle_rad),
                       y + HEX_SIZE * math.sin(angle_rad)))
    pygame.draw.polygon(surface, (0, 0, 0), points, 5)  # Draw black border with a line width of 4
    pygame.draw.polygon(surface, color, points)

def draw_text(surface, text, font, color, x, y):
    lines = text.split('\n')  # Split text into lines
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y + i * (FONT_SIZE + 5))  # Adjust vertical position for each line
        surface.blit(text_surface, text_rect)


def start_screen(screen):
    font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        screen.fill(BACKGROUND_COLOR)
        draw_text(screen, START_TEXT, font, FONT_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()
# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Catan Board')

    start_screen(screen)
    hexagon_colors = generate_hexagon_colors()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        screen.fill(BACKGROUND_COLOR)

        # Calculate starting position to center the grid
        start_x = (SCREEN_WIDTH - HEX_WIDTH * 5) / 2
        start_y = (SCREEN_HEIGHT - HEX_HEIGHT * 5) / 2

        # Draw hexagonal grid
        color_index=0
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
                draw_hexagon(screen, x, y, hexagon_colors[color_index])
                color_index += 1

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

