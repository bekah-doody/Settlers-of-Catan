import pygame
import random
import math
from game import *

pygame.init()


SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 750
HEX_SIZE = 70
HEX_WIDTH = math.sqrt(3) * HEX_SIZE
HEX_HEIGHT = 1.5 * HEX_SIZE
BACKGROUND_COLOR = (0, 157, 196)
HEX_COLOR = (100, 100, 100)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 36
FONT_STYLE = 'Arial'
START_TEXT = "\n\nPress Space to Start\n\nBekah Doody \nDrew Baine \nJason Miranda"
NUMBERS = ['2', '3', '3', '4', '4', '5', '5', '6', '6', '8', '8', '9', '9', '10', '10', '11', '11', '12']
COLOR_QUANTITIES = {
    (255, 0, 0): 3,  # red -> bricks
    (0, 255, 0): 4,  # green -> sheep
    (139, 69, 19): 4,  # brown -> wood
    (176, 196, 222): 3,  # blue-gray -> mountains
    (255, 255, 0): 4,  # yellow -> wheat
    (229, 201, 159): 1,  # tan -desert
}


def generate_hexagon_colors():
    hexagon_colors = []
    colors = list(COLOR_QUANTITIES.keys())  # Get list of colors
    for color, quantity in COLOR_QUANTITIES.items():
        hexagon_colors.extend([color] * quantity)  # Add each color to the list the specified number of times
    random.shuffle(hexagon_colors)  # Shuffle the list of colors
    return hexagon_colors


def generate_hexagon_numbers():
    return random.sample(NUMBERS, 18)


def draw_hexagon(surface, x, y, color):
    points = []
    for i in range(6):
        angle_deg = 60 * i + 30
        angle_rad = math.pi / 180 * angle_deg
        points.append((x + HEX_SIZE * math.cos(angle_rad),
                       y + HEX_SIZE * math.sin(angle_rad)))
    pygame.draw.polygon(surface, (0, 0, 0), points, 5)  # Draw black border with a line width of 4
    pygame.draw.polygon(surface, color, points)


def draw_text(surface, text, font, color, x, y, align="center"):
    lines = text.split('\n')  # Split text by newline character
    y_offset = 0  # Initialize y offset for multiline text
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect()
        if align == "center":
            text_rect.center = (x, y + y_offset)
        elif align == "left":
            text_rect.left = x  # Adjust the left edge of the rectangle
            text_rect.centery = y + y_offset  # Center the text vertically at the specified y-coordinate
        elif align == "right":
            text_rect.right = x  # Adjust the right edge of the rectangle
            text_rect.centery = y + y_offset  # Center the text vertically at the specified y-coordinate
        surface.blit(text_surface, text_rect)
        y_offset += text_rect.height  # Update y offset for the next line


def start_screen(screen):


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont(FONT_STYLE, 150)
        draw_text(screen, "Settlers of Catan", font, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 -70, align='center')
        font = pygame.font.SysFont(FONT_STYLE, 70)
        draw_text(screen, "\n\nPress Space to Start", font, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT// 2 -100, align='center')
        font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)
        draw_text(screen, "\n\n\n\nBekah Doody\nDrew Baine\nJason Miranda", font, (15, 15, 100), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, align='center')
        pygame.display.flip()


# Function to roll a single die
def roll_die():
    return random.randint(1, 6)


# Function to roll two dice and return the results
def roll_dice():
    return roll_die(), roll_die()

def draw_grid(SCREEN_WIDTH, HEX_WIDTH, screen, font, hexagon_colors, hexagon_numbers):

    # Calculate starting position to center the grid
    start_x = (SCREEN_WIDTH - HEX_WIDTH * 5) / 2
    start_y = (SCREEN_HEIGHT - HEX_HEIGHT * 5) / 2
    # Draw hexagonal grid
    color_index = 0
    number_index = 0
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
            x = start_x + 100 + col * HEX_WIDTH + row_offset * HEX_WIDTH / 2
            y = start_y + 60 + row * HEX_HEIGHT
            draw_hexagon(screen, x, y, hexagon_colors[color_index])
            if hexagon_colors[color_index] != (229, 201, 159):
                draw_text(screen, hexagon_numbers[number_index], font, FONT_COLOR, x, y, align="center")
                number_index += 1
            color_index += 1


# Main function
def main():
    hexagon_colors = generate_hexagon_colors()
    hexagon_numbers = generate_hexagon_numbers()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Catan Board')
    game = Game()
    game.current_player = game.players[0]

    game.generate_vertices()
    game.set_order()
    start_screen(screen)

    font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pass
                if event.key == pygame.K_i:
                    pass
                if event.key == pygame.K_s:
                    pass

                if event.key == pygame.K_c:
                    pass

                if event.key == pygame.K_e:

                    game.change_player()



        screen.fill(BACKGROUND_COLOR)
        draw_grid(SCREEN_WIDTH, HEX_WIDTH, screen, font, hexagon_colors, hexagon_numbers)
        game.draw_vertices(screen)

                # Draw text to the right of the board

        left_text = "Current Player: " + game.current_player.name + "\nPress: \nR to roll \nI to buy a Road\nS to buy a Settlement\nC to buy a City\nE to end turn "
        right_text = 'Resource Hex Codes\nGreen: Sheep\nYellow: Wheat\nGray: Ore\nBrown: Wood\nRed: Brick\nTan:Desert'
        draw_text(screen, right_text, font, FONT_COLOR, SCREEN_WIDTH - 10, 25, align='right')
        draw_text(screen, left_text, font, FONT_COLOR, 10, 25, align='left')




        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()