import pygame
import random
import math
from game import *
import time
import player
import resource_hexes
import buildings
import backgrounds

pygame.init()


class board:
    """
    This class stores data and functions related to the Catan board

    Attributes:
        SCREEN_WIDTH(int): width of the pop-up screen
        SCREEN_HEIGHT(int): height of the pop-up screen
        SCREEN: the pygame screen itself
        HEX_SIZE(int): size of resource hexagons
        HEX_WIDTH(int): width of the resource hexagons
        BACKGROUND_COLOR(int, int, int): the color of the screen background
        FONT_COLOR(int, int, int): color of the text
        FONT_SIZE(int): size of text
        FONT_STYLE(int): the font itself
        START_TEST(str): text on the start screen
        NUMBERS(list): list of the roll probabilities to be distributed
        grid_nums(list): list to be filled with the order of numbers of the board
        grid_colors(list): list to be filled with the order of colors of the board
        COLOR_QUANTITIES(dict): how many hexes of each color to be distributed
    """

    def __init__(self):
        """
        Constructor of the board class
        """
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
        self.grid_nums = []
        self.grid_colors = []
        self.background_image = pygame.image.load("backgrounds/start_screen.png")
        self.COLOR_QUANTITIES = {
            (255, 0, 0): 3,  # red -> bricks
            (0, 255, 0): 4,  # green -> sheep
            (139, 69, 19): 4,  # brown -> wood
            (176, 196, 222): 3,  # blue-gray -> mountains
            (255, 255, 0): 4,  # yellow -> wheat
            (229, 201, 159): 1,  # tan -desert
        }
        self.COLOR_DICT = {
            (255, 0, 0): "bricks",  # red -> bricks
            (0, 255, 0): "sheep",  # green -> sheep
            (139, 69, 19): "wood",  # brown -> wood
            (176, 196, 222): "ore",  # blue-gray -> mountains
            (255, 255, 0): "wheat",  # yellow -> wheat
            (229, 201, 159): "desert",
        }
        self.hill = None
        self.mountain = None
        self.pasture = None
        self.forest = None
        self.desert = None
        self.field = None

    def generate_hexagon_colors(self):
        """
        Generates a shuffled list of hexagon colors
        :return: hexagon_colors
        """
        hexagon_colors = []
        colors = list(self.COLOR_QUANTITIES.keys())  # Get list of colors
        for color, quantity in self.COLOR_QUANTITIES.items():
            hexagon_colors.extend([color] * quantity)  # Add each color to the list the specified number of times
        random.shuffle(hexagon_colors)  # Shuffle the list of colors
        return hexagon_colors

    def generate_hexagon_numbers(self):
        """
        Generates a shuffled list of the roll probabilities
        :return: shuffled roll probabilities
        """
        return random.sample(self.NUMBERS, 18)

    def draw_hexagon(self, surface, x, y, color):
        """
        Draws the hexagons on the board
        :param x: x coord to be placed at
        :param y: y coord to be placed at
        :param color: color of hexagon
        """
        points = []
        for i in range(6):
            angle_deg = 60 * i + 30
            angle_rad = math.pi / 180 * angle_deg
            points.append((x + self.HEX_SIZE * math.cos(angle_rad),
                           y + self.HEX_SIZE * math.sin(angle_rad)))
        # pygame.draw.polygon(surface, (230, 200, 170), points, 15)
        pygame.draw.polygon(surface, (210, 180, 140), points, 10)  # Draw tan border
        pygame.draw.polygon(surface, color, points)

    def draw_text(self, surface, text, font, color, x, y, align="center"):
        """
        Draws text on the board
        :param text: text to be printed
        :param font: text font
        :param color: text color
        :param x: x coord of text placement
        :param y: y coord of text placement
        :param align: left/right/center alignment of text
        :return:
        """
        lines = text.split('\n')  # Split text by newline character
        y_offset = 0  # Initialize y offset for multiline text
        for line in lines:
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect()
            if align == "center":
                text_rect.center = (x, y + y_offset)
            elif align == "left":
                text_rect.left = x  # Adjust the left edge of the rectangle
                text_rect.centery = y + y_offset  # Center the text vertically at specified y-coordinate
            elif align == "right":
                text_rect.right = x  # Adjust the right edge of rectangle
                text_rect.centery = y + y_offset  # Center the text vertically at specified y-coordinate
            surface.blit(text_surface, text_rect)
            y_offset += text_rect.height  # Update y offset for next line

    def start_screen(self, screen):
        """
        Creates the start screen
        """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            self.background_image = pygame.transform.scale(self.background_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
            screen.blit(self.background_image, (0,0))

            # screen.fill(self.BACKGROUND_COLOR)
            # font = pygame.font.SysFont(self.FONT_STYLE, 150)
            # self.draw_text(screen, "Settlers of Catan", font, (255, 255, 255), self.SCREEN_WIDTH // 2,
            #                self.SCREEN_HEIGHT // 2 - 70,
            #                align='center')
            # font = pygame.font.SysFont(self.FONT_STYLE, 70)
            # self.draw_text(screen, "\n\nPress Space to Start", font, (255, 255, 255), self.SCREEN_WIDTH // 2,
            #                self.SCREEN_HEIGHT // 2 - 100, align='center')
            # font = pygame.font.SysFont(self.FONT_STYLE, self.FONT_SIZE)
            # self.draw_text(screen, "\n\n\n\nBekah Doody\nDrew Baine\nJason Miranda", font, (15, 15, 100),
            #                self.SCREEN_WIDTH // 2,
            #                self.SCREEN_HEIGHT // 2, align='center')
            pygame.display.flip()

    def display_options(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN):
        """
        Creates the options menu
        :param SCREEN_WIDTH: width of screen
        :param SCREEN_HEIGHT: height of screen
        :param SCREEN: the screen itself
        """
        popup_width = 400
        popup_height = 300
        font = pygame.font.Font(None, 36)
        popup_x = (SCREEN_WIDTH - popup_width) // 2
        popup_y = (SCREEN_HEIGHT - popup_height) // 2

        pygame.draw.rect(SCREEN, (250, 250, 250), (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(SCREEN, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 2)

        commands = ['R to roll dice',
                    'E to end turn',
                    'I to view inventory',
                    'X to quit'
                    ]

        for i, command in enumerate(commands):
            text = font.render(command, True, (0, 0, 0))
            SCREEN.blit(text, (popup_x + 20, popup_y + 20 + i * 40))

        pygame.display.flip()

    def display_inventory(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN, wood, brick, sheep, wheat, ore):
        """
        Creates the options menu
        :param SCREEN_WIDTH: width of screen
        :param SCREEN_HEIGHT: height of screen
        :param SCREEN: the screen itself
        """
        popup_width = 400
        popup_height = 300
        font = pygame.font.Font(None, 36)
        popup_x = (SCREEN_WIDTH - popup_width) // 2
        popup_y = (SCREEN_HEIGHT - popup_height) // 2

        pygame.draw.rect(SCREEN, (250, 250, 250), (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(SCREEN, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 2)

        commands = ["Wood: " + str(wood),
                    "Bricks: " + str(brick),
                    "Sheep: " + str(sheep),
                    "Wheat: " + str(wheat),
                    "Ore: " + str(ore)]

        for i, command in enumerate(commands):
            text = font.render(command, True, (0, 0, 0))
            SCREEN.blit(text, (popup_x + 20, popup_y + 20 + i * 40))

        pygame.display.flip()

    def load_images(self):
        self.hill = pygame.image.load("resource_hexes/hill-removebg-preview.png")
        self.pasture = pygame.image.load("resource_hexes/pasture-removebg-preview.png")
        self.mountain = pygame.image.load("resource_hexes/mountain-removebg-preview.png")
        self.forest = pygame.image.load("resource_hexes/forest-removebg-preview.png")
        self.desert = pygame.image.load("resource_hexes/desert-removebg-preview.png")
        self.field = pygame.image.load("resource_hexes/field-removebg-preview.png")

        self.hill = pygame.transform.scale(self.hill, (self.HEX_WIDTH + 18, self.HEX_HEIGHT + 42))
        self.pasture = pygame.transform.scale(self.pasture, (self.HEX_WIDTH + 18, self.HEX_HEIGHT + 42))
        self.mountain = pygame.transform.scale(self.mountain, (self.HEX_WIDTH + 18, self.HEX_HEIGHT + 42))
        self.forest = pygame.transform.scale(self.forest, (self.HEX_WIDTH + 18, self.HEX_HEIGHT + 42))
        self.desert = pygame.transform.scale(self.desert, (self.HEX_WIDTH + 18, self.HEX_HEIGHT + 42))
        self.field = pygame.transform.scale(self.field, (self.HEX_WIDTH + 18, self.HEX_HEIGHT + 42))

    def draw_grid(self, SCREEN_WIDTH, HEX_WIDTH, screen, font, hexagon_colors, hexagon_numbers):
        """
        Draws the grid of hexagons to create the classic Catan board
        :param SCREEN_WIDTH: width of screen
        :param HEX_WIDTH: width of hexagoons
        :param screen: the screen itself
        :param font: text font for roll probabilities
        :param hexagon_colors: the randomized list of hexagon colors
        :param hexagon_numbers: the randomized list of hexagon numbers
        """

        # Calculate starting position to center the grid
        # self.background_image = pygame.transform.scale(self.background_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        # screen.blit(self.background_image, (0,0))
        start_x = (SCREEN_WIDTH - HEX_WIDTH * 5) / 2
        start_y = (self.SCREEN_HEIGHT - self.HEX_HEIGHT * 5) / 2

        self.load_images()

        resource_images = {
            (255, 0, 0): self.hill,
            (0, 255, 0): self.pasture,
            (139, 69, 19): self.forest,
            (176, 196, 222): self.mountain,
            (255, 255, 0): self.field,
            (229, 201, 159): self.desert,
        }

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
                    resource_image = resource_images[hexagon_colors[color_index]]
                    screen.blit(resource_image,
                                (x - resource_image.get_width() / 2, y - resource_image.get_height() / 2))
                    self.draw_text(screen, hexagon_numbers[number_index], font, self.FONT_COLOR, x, y, align="center")
                    self.grid_nums.append(hexagon_numbers[number_index])
                    self.grid_colors.append(hexagon_colors[color_index])
                    number_index += 1
                else:
                    desert_image = resource_images[(229, 201, 159)]
                    screen.blit(desert_image,
                                (x - desert_image.get_width() / 2, y - desert_image.get_height() / 2))
                color_index += 1
                #     self.draw_text(screen, hexagon_numbers[number_index], font, self.FONT_COLOR, x, y, align="center")
                #     self.grid_nums.append(hexagon_numbers[number_index])
                #     self.grid_colors.append(hexagon_colors[color_index])
                #     number_index += 1
                # color_index += 1


class animation:
    def __init__(self):
        self.images = []
        self.time = time.time()
        self.temp = 0
        self.run = False
        self.roll = None

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

class Dice:

    def __init__(self, x, y, scale =1):
        self.topleft = (x,y)
        self.num = -1
        self.scale = scale
        imagelocation = "dices/dice1.png"
        image = pygame.image.load(imagelocation).convert_alpha()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self, surface, num):
        if not num == self.num:
            imagelocation = "dices/dice"+str(num)+".png"
            image = pygame.image.load(imagelocation).convert_alpha()
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = self.topleft
        surface.blit(self.image,  (self.rect.x, self.rect.y))


# Main function
def main():
    """
    Main function
    """

    # Creates two players
    player1 = Player("player1", ((255, 0, 0)))
    player2 = Player("player2", ((0, 0, 255)))
    current_player = player1

    players = (player1, player2)

    # initializes board
    b = board()
    hexagon_colors = b.generate_hexagon_colors()
    hexagon_numbers = b.generate_hexagon_numbers()
    screen = pygame.display.set_mode((b.SCREEN_WIDTH, b.SCREEN_HEIGHT))
    pygame.display.set_caption('Catan Board')

    # initializes game
    game = Game(player1, player2)
    game.current_player = game.players[0]

    # dice roll animation
    dice_roll = animation()
    for num in range(1, 6):
        frame = "dices/frame" + str(num) + ".png"
        dice_frame = pygame.image.load(frame).convert_alpha()
        scale = .5
        dice_roll.images.append(Frame(50, 500, dice_frame, .1))

    dice1 = Dice(69, 567, .3)
    dice2 = Dice(218, 567, .3)

    # creates the vertices
    game.generate_vertices()
    game.generate_roads()
    game.set_order()
    b.start_screen(screen)

    # running logic
    font = pygame.font.SysFont(b.FONT_STYLE, b.FONT_SIZE)
    running = True
    show_options = False
    show_inventory = False
    rolling = True
    lastroll1 = 1
    lastroll2 = 1
    pos = pygame.mouse.get_pos()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    show_options = True
                if event.key == pygame.K_r:
                    dice_roll.run = True

                    rolla = game.roll_dice()
                    lastroll1 = rolla[0]
                    lastroll2 = rolla[1]
                    roll = rolla[0] + rolla[1]
                    print(roll)

                    # Distribute resources based on the rolled number
                    for num in range(0, len(hexagon_numbers)):
                        a = hexagon_numbers[num]
                        if int(a) == (roll):
                            hex_color = hexagon_colors[num]
                            resources = game.get_resource_type(hex_color)
                            current_player.collect_resource(resources)
                            # print("Wood", current_player.wood)
                            # print("Wheat", current_player.wheat)
                            # print("Sheep", current_player.sheep)
                            # print("Brick", .brick)
                            # print("Ore", player1.ore)
                            # player2.collect_resource(resources)
                            # print("Wood", player2.wood)
                            # print("Wheat", player2.wheat)
                            # print("Sheep", player2.sheep)
                            # print("Brick", player2.brick)
                            # print("Ore", player2.ore)
                            pygame.display.flip()

                if event.key == pygame.K_i:
                    if event.key == pygame.K_i:
                        show_inventory = True
                if event.key == pygame.K_s:
                    pass

                if event.key == pygame.K_x:
                    pygame.quit()

                if event.key == pygame.K_e:
                    game.change_player()
                    current_player.next_turn()
                    if current_player == player1:
                        current_player = player2
                    else:
                        current_player = player1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    show_options = False
                if event.key == pygame.K_i:
                    show_inventory = False

        screen.fill(b.BACKGROUND_COLOR)
        b.draw_grid(b.SCREEN_WIDTH, b.HEX_WIDTH, screen, font, hexagon_colors, hexagon_numbers)
        game.draw_roads(screen)
        game.draw_vertices(screen)
        dice_roll.run = dice_roll.run_through(screen)

        dice_roll.run_through(screen)

        # Draw text to the right and left of the board
        player4 = game.current_player
        left_text = "Current Player: " + game.current_player.name + "\nHold O to see Options"
        right_text = 'Victory Points: ' + str(int(current_player.settlements))
        if current_player.settlements > 4:
            win_image = pygame.image.load("backgrounds/" + current_player.name + "_win.png")
            win_image = pygame.transform.scale(win_image, (b.SCREEN_WIDTH, b.SCREEN_HEIGHT))
            screen.blit(win_image, (0, 0))
        b.draw_text(screen, right_text, font, b.FONT_COLOR, b.SCREEN_WIDTH - 10, 25, align='right')
        b.draw_text(screen, left_text, font, b.FONT_COLOR, 10, 25, align='left')

        if show_options:
            b.display_options(b.SCREEN_WIDTH, b.SCREEN_HEIGHT, b.SCREEN)
        if show_inventory:
            b.display_inventory(b.SCREEN_WIDTH, b.SCREEN_HEIGHT, b.SCREEN, current_player.wood,
                                current_player.brick, current_player.sheep, current_player.wheat,
                                current_player.ore)

        if not pygame.mouse.get_pos() == pos:
            pos=pygame.mouse.get_pos()
            print(pos)
        if not dice_roll.run:
            dice1.draw(screen, lastroll1)
            dice2.draw(screen, lastroll2)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
