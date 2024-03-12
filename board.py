import pygame
import random
import math
from game import *
import time

pygame.init()

class board:
    def __init__(self):
        self.SCREEN_WIDTH = 1250
        self.SCREEN_HEIGHT = 750
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.HEX_SIZE = 70
        self.HEX_WIDTH = math.sqrt(3) * self.HEX_SIZE
        self.HEX_HEIGHT = 1.5 * self.HEX_SIZE
        self.BACKGROUND_COLOR = (0, 157, 196)
        self.FONT_COLOR = (0, 0, 0)
        self.FONT_SIZE = 36
        self.FONT_STYLE = 'Arial'
        self.START_TEXT = "\n\nPress Space to Start\n\nBekah Doody \nDrew Baine \nJason Miranda"
        self.NUMBERS = ['2', '3', '3', '4', '4', '5', '5', '6', '6', '8', '8', '9', '9', '10', '10', '11', '11', '12']
        self.COLOR_QUANTITIES = {
            (255, 0, 0): 3,  # red -> bricks
            (0, 255, 0): 4,  # green -> sheep
            (139, 69, 19): 4,  # brown -> wood
            (176, 196, 222): 3,  # blue-gray -> mountains
            (255, 255, 0): 4,  # yellow -> wheat
            (229, 201, 159): 1,  # tan -desert
        }

    def generate_hexagon_colors(self):
        hexagon_colors = []
        colors = list(self.COLOR_QUANTITIES.keys())  # Get list of colors
        for color, quantity in self.COLOR_QUANTITIES.items():
            hexagon_colors.extend([color] * quantity)  # Add each color to the list the specified number of times
        random.shuffle(hexagon_colors)  # Shuffle the list of colors
        return hexagon_colors

    def generate_hexagon_numbers(self):
        return random.sample(self.NUMBERS, 18)

    def draw_hexagon(self, surface, x, y, color):
        points = []
        for i in range(6):
            angle_deg = 60 * i + 30
            angle_rad = math.pi / 180 * angle_deg
            points.append((x + self.HEX_SIZE * math.cos(angle_rad),
                           y + self.HEX_SIZE * math.sin(angle_rad)))
        pygame.draw.polygon(surface, (0, 0, 0), points, 5)  # Draw black border with a line width of 4
        pygame.draw.polygon(surface, color, points)

    def draw_text(self, surface, text, font, color, x, y, align="center"):
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

    def start_screen(self, screen):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            screen.fill(self.BACKGROUND_COLOR)
            font = pygame.font.SysFont(self.FONT_STYLE, 150)
            self.draw_text(screen, "Settlers of Catan", font, (255, 255, 255), self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 - 70,
                      align='center')
            font = pygame.font.SysFont(self.FONT_STYLE, 70)
            self.draw_text(screen, "\n\nPress Space to Start", font, (255, 255, 255), self.SCREEN_WIDTH // 2,
                      self.SCREEN_HEIGHT // 2 - 100, align='center')
            font = pygame.font.SysFont(self.FONT_STYLE, self.FONT_SIZE)
            self.draw_text(screen, "\n\n\n\nBekah Doody\nDrew Baine\nJason Miranda", font, (15, 15, 100), self.SCREEN_WIDTH // 2,
                      self.SCREEN_HEIGHT // 2, align='center')
            pygame.display.flip()

    def display_options(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN):
        popup_width = 400
        popup_height = 300
        font = pygame.font.Font(None, 36)
        popup_x = (SCREEN_WIDTH - popup_width) // 2
        popup_y = (SCREEN_HEIGHT - popup_height) // 2

        pygame.draw.rect(SCREEN,(250,250,250), (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(SCREEN, (0,0,0), (popup_x, popup_y, popup_width, popup_height), 2)

        commands = ['R to roll_die',
                    'I to buy a Road',
                    'S to buy a Settlement',
                    'C to buy a City',
                    'E to end turn',
                    'N to view inventory',
                    'B to Buy',]

        for i, command in enumerate(commands):
            text = font.render(command, True, (0,0,0))
            SCREEN.blit(text, (popup_x + 20, popup_y + 20 + i * 40))

        pygame.display.flip()


    # Function to roll a single die
    def roll_die(self):
        return random.randint(1, 6)


    # Function to roll two dice and return the results
    def roll_dice(self):
        return self.roll_die(), self.roll_die()

    def draw_grid(self,SCREEN_WIDTH, HEX_WIDTH, screen, font, hexagon_colors, hexagon_numbers):

        # Calculate starting position to center the grid
        start_x = (SCREEN_WIDTH - HEX_WIDTH * 5) / 2
        start_y = (self.SCREEN_HEIGHT - self.HEX_HEIGHT * 5) / 2
        # Draw hexagonal grid
        color_index = 0
        number_index = 0
        num_hexes_in_row = 0
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
                x = start_x + 100 + col * self.HEX_WIDTH + row_offset * self.HEX_WIDTH / 2
                y = start_y + 60 + row * self.HEX_HEIGHT
                self.draw_hexagon(screen, x, y, hexagon_colors[color_index])
                if hexagon_colors[color_index] != (229, 201, 159):
                    self.draw_text(screen, hexagon_numbers[number_index], font, self.FONT_COLOR, x, y, align="center")
                    number_index += 1
                color_index += 1


class animation:
    def __init__(self):
        self.images = []
        self.time = time.time()
        self.temp = 0
        self.run = False

    def randomize(self, screen):
        if not self.images:
            return
        if self.time == 0:
            self.time = 100
            temp = self.temp
            while temp == self.temp:
                temp = random.randint(0, len(self.images) - 1)
            self.temp = temp
        self.images[self.temp].draw(screen)
        self.time -= 1

    def run_through(self, screen) -> bool:
        if not self.images:
            return False
        if self.run:
            self.images[self.temp].draw(screen)
            temp = time.time()


            if temp - self.time > .25:
                self.time = time.time()
                if self.temp == len(self.images) - 1:
                    self.temp = 0
                    return False
                else:
                    self.temp += 1
            return True


class Frame:
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))


# Main function
def main():
    b = board()
    hexagon_colors = b.generate_hexagon_colors()
    hexagon_numbers = b.generate_hexagon_numbers()
    screen = pygame.display.set_mode((b.SCREEN_WIDTH, b.SCREEN_HEIGHT))
    pygame.display.set_caption('Catan Board')
    game = Game()
    game.current_player = game.players[0]
    dice_roll = animation()
    for num in range(1,6):
        frame = "dices/frame"+str(num) +".png"
        dice_frame = pygame.image.load(frame).convert_alpha()
        scale = .5
        dice_roll.images.append(Frame(50, 500, dice_frame, .1))

    game.generate_vertices()
    game.set_order()
    b.start_screen(screen)

    font = pygame.font.SysFont(b.FONT_STYLE, b.FONT_SIZE)
    running = True
    show_options = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    show_options = True
                if event.key == pygame.K_r:
                    dice_roll.run = True
                if event.key == pygame.K_i:
                    pass
                if event.key == pygame.K_s:
                    pass

                if event.key == pygame.K_c:
                    pass

                if event.key == pygame.K_e:
                    game.change_player()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    show_options = False



        screen.fill(b.BACKGROUND_COLOR)
        b.draw_grid(b.SCREEN_WIDTH, b.HEX_WIDTH, screen, font, hexagon_colors, hexagon_numbers)
        game.draw_vertices(screen)
        dice_roll.run = dice_roll.run_through(screen)
        dice_roll.run_through(screen)

        # Draw text to the right of the board

        left_text = "Current Player: " + game.current_player.name + "\nHold O to see Options"
        right_text = 'Resource Hex Codes\nGreen: Sheep\nYellow: Wheat\nGray: Ore\nBrown: Wood\nRed: Brick\nTan:Desert'
        b.draw_text(screen, right_text, font, b.FONT_COLOR, b.SCREEN_WIDTH - 10, 25, align='right')
        b.draw_text(screen, left_text, font, b.FONT_COLOR, 10, 25, align='left')


        if show_options:
            b.display_options(b.SCREEN_WIDTH,b.SCREEN_HEIGHT,b.SCREEN)



        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
