"This class holds Game and Vertex. Game holds all the information on "

from player import Player
from vertex_button import VertexButton
import pygame
import random


class Game:
    """
    Holds information on the game. Includes which players turn it is along with if a vertex has been clicked and
    what player has it.

    """

    def __init__(self):
        self.players = [Player("player1", ((255, 0, 0))), Player("player2", ((0, 0, 255)))]
        self.vertices = []
        self.current_player = None

    def get_adjacent_hexagons(self, vertex):
        """
        Get the hexagons adjacent to a given vertex.
        """
        adjacent_hexagons = []
        vertex_index = self.board.grid_nums.index(vertex)  # Find the index of the given vertex in grid_nums
        adjacent_indices = self.get_adjacent_indices(vertex_index)
        for index in adjacent_indices:
            color = self.board.grid_colors[index]
            hexagon = {"color": color, "number": self.board.grid_nums[index]}
            adjacent_hexagons.append(hexagon)
        return adjacent_hexagons

    def get_adjacent_indices(self, vertex_index):
        """
        Get the indices of adjacent vertices.
        """
        adjacent_indices = []
        # Define the pattern of adjacent indices based on the layout of the board
        # Adjust this pattern based on your specific board layout
        pattern = {
            0: [1, 2, 6, 5, 4, 3],
            1: [0, 2, 7, 12, 11, 5],
            2: [0, 1, 3, 8, 13, 6],
            3: [0, 2, 13, 18, 17, 4],
            4: [0, 3, 17, 16, 15, 14],
            5: [0, 4, 14, 10, 9, 1],
            6: [0, 2, 13, 18, 17, 4],
            7: [1, 8, 19, 24, 12, 11],
            8: [2, 7, 9, 20, 25, 13],
            9: [5, 8, 21, 26, 10, 1],
            10: [5, 9, 26, 27, 22, 14],
            11: [1, 7, 12, 24, 23, 15],
            12: [1, 11, 23, 28, 19, 2],
            13: [2, 8, 25, 29, 18, 6],
            14: [4, 10, 27, 30, 16, 5],
            15: [4, 11, 23, 32, 31, 14],
            16: [4, 14, 31, 33, 34, 17],
            17: [3, 6, 13, 18, 29, 16],
            18: [3, 6, 17, 29, 35, 36],
            19: [7, 12, 28, 37, 24, 0],
            20: [8, 25, 38, 39, 21, 2],
            21: [9, 20, 39, 40, 26, 5],
            22: [10, 26, 40, 41, 27, 0],
            23: [11, 15, 32, 42, 37, 0],
            24: [7, 12, 19, 37, 43, 44],
            25: [8, 13, 29, 38, 45, 46],
            26: [9, 21, 40, 47, 39, 0],
            27: [10, 22, 41, 48, 49, 14],
            28: [12, 19, 37, 44, 50, 51],
            29: [13, 18, 35, 36, 52, 45],
            30: [14, 16, 33, 53, 54, 55],
            31: [15, 23, 42, 56, 57, 58],
            32: [15, 31, 57, 59, 60, 61],
            33: [16, 30, 54, 62, 63, 34],
            34: [16, 33, 63, 64, 65, 66],
            35: [18, 29, 36, 52, 67, 68],
            36: [18, 35, 68, 69, 70, 71],
            37: [19, 23, 28, 44, 51, 0],
            38: [20, 25, 46, 72, 73, 74],
            39: [20, 21, 26, 47, 75, 76],
            40: [21, 26, 27, 48, 77, 78],
            41: [27, 48, 79, 80, 81, 0],
            42: [23, 31, 56, 82, 83, 0],
            43: [24, 44, 50, 84, 0, 0],
            44: [24, 28, 37, 51, 0, 0],
            45: [25, 29, 52, 85, 0, 0],
            46: [25, 38, 72, 86, 0, 0],
            47: [26, 39, 75, 87, 0, 0],
            48: [27, 40, 41, 79, 88, 0],
            49: [27, 49, 88, 0, 0, 0],
            50: [28, 37, 43, 0, 0, 0],
            51: [28, 37, 44, 0, 0, 0],
            52: [29, 35, 45, 0, 0, 0],
            53: [30, 33, 54, 0, 0, 0],
            54: [30, 33, 53, 0, 0, 0],
            55: [30, 0, 0, 0, 0, 0],
            56: [31, 42, 0, 0, 0, 0],
            57: [31, 32, 58, 0, 0, 0],
            58: [31, 57, 0, 0, 0, 0],
            59: [32, 0, 0, 0, 0, 0],
            60: [32, 0, 0, 0, 0, 0],
            61: [32, 0, 0, 0, 0, 0],
            62: [33, 0, 0, 0, 0, 0],
            63: [33, 0, 0, 0, 0, 0],
            64: [34, 0, 0, 0, 0, 0],
            65: [34, 0, 0, 0, 0, 0],
            66: [34, 0, 0, 0, 0, 0],
            67: [35, 0, 0, 0, 0, 0],
            68: [35, 36, 0, 0, 0, 0],
            69: [36, 0, 0, 0, 0, 0],
            70: [36, 0, 0, 0, 0, 0],
            71: [36, 0, 0, 0, 0, 0],
            72: [38, 46, 0, 0, 0, 0],
            73: [38, 0, 0, 0, 0, 0],
            74: [38, 0, 0, 0, 0, 0],
            75: [39, 47, 0, 0, 0, 0],
            76: [39, 0, 0, 0, 0, 0],
            77: [40, 0, 0, 0, 0, 0],
            78: [40, 0, 0, 0, 0, 0],
            79: [41, 48, 0, 0, 0, 0],
            80: [41, 0, 0, 0, 0, 0],
            81: [41, 0, 0, 0, 0, 0],
            82: [42, 0, 0, 0, 0, 0],
            83: [42, 0, 0, 0, 0, 0],
            84: [43, 0, 0, 0, 0, 0],
            85: [45, 0, 0, 0, 0, 0],
            86: [46, 0, 0, 0, 0, 0],
            87: [47, 0, 0, 0, 0, 0],
            88: [48, 49, 0, 0, 0, 0],
        }
        return pattern[vertex_index]

    def distribute_resources(self, roll):
        """
        Distributes resources to players based on the dice roll

        Parameters:
            roll(int) = the number the dice roll
        """

    def get_resource_type(self, color):
        resource_mapping = {
            (0, 255, 0): "sheep",  # Green
            (255, 255, 0): "wheat",  # Yellow
            (176, 196, 222): "ore",  # Gray
            (139, 69, 19): "wood",  # Brown
            (255, 0, 0): "brick"  # Red
        }
        return resource_mapping.get(color)

    def generate_vertices(self) -> list:
        "Generates all vertices and fills self.vertices"
        temp = []
        # top
        temp.append(Vertex(480, 101))
        temp.append(Vertex(601, 101))
        temp.append(Vertex(726, 101))
        # 2nd top
        temp.append(Vertex(787, 135))
        temp.append(Vertex(662, 135))
        temp.append(Vertex(544, 135))
        temp.append(Vertex(421, 135))
        # 3rd row
        temp.append(Vertex(419, 205))
        temp.append(Vertex(544, 205))
        temp.append(Vertex(662, 205))
        temp.append(Vertex(784, 205))
        # 4th row
        temp.append(Vertex(361, 241))
        temp.append(Vertex(480, 241))
        temp.append(Vertex(603, 241))
        temp.append(Vertex(725, 241))
        temp.append(Vertex(848, 241))
        # 5th row
        temp.append(Vertex(361, 312))
        temp.append(Vertex(480, 312))
        temp.append(Vertex(603, 312))
        temp.append(Vertex(725, 312))
        temp.append(Vertex(848, 312))
        # 6th row
        temp.append(Vertex(300, 346))
        temp.append(Vertex(420, 346))
        temp.append(Vertex(544, 346))
        temp.append(Vertex(662, 346))
        temp.append(Vertex(784, 346))
        temp.append(Vertex(908, 346))
        # 7th row
        temp.append(Vertex(300, 416))
        temp.append(Vertex(420, 416))
        temp.append(Vertex(544, 416))
        temp.append(Vertex(662, 416))
        temp.append(Vertex(784, 416))
        temp.append(Vertex(908, 416))
        # 8th row
        temp.append(Vertex(361, 452))
        temp.append(Vertex(480, 452))
        temp.append(Vertex(603, 452))
        temp.append(Vertex(725, 452))
        temp.append(Vertex(848, 452))
        # 9th row
        temp.append(Vertex(361, 521))
        temp.append(Vertex(480, 521))
        temp.append(Vertex(603, 521))
        temp.append(Vertex(725, 521))
        temp.append(Vertex(848, 521))
        # 10th row
        temp.append(Vertex(420, 556))
        temp.append(Vertex(544, 556))
        temp.append(Vertex(662, 556))
        temp.append(Vertex(784, 556))
        # 11th row
        temp.append(Vertex(421, 627))
        temp.append(Vertex(544, 627))
        temp.append(Vertex(662, 627))
        temp.append(Vertex(784, 627))
        # 12th row
        temp.append(Vertex(482, 663))
        temp.append(Vertex(603, 663))
        temp.append(Vertex(725, 663))
        self.vertices = temp

    def draw_vertices(self, surface):
        for num in range(len(self.vertices)):
            if self.vertices[num].button.draw(surface):
                self.vertices[num].buy_settlement(self.current_player)
            self.vertices[num].button.draw(surface)
            self.vertices[num].draw(surface)

    def set_order(self):
        for num in range(len(self.players)):
            if not num == len(self.players) - 1:
                self.players[num].before = self.players[num + 1]
        self.players[len(self.players) - 1].before = self.players[0]

    def change_player(self):

        self.current_player = self.current_player.before

    # Function to roll a single die
    def roll_die(self):
        return random.randint(1, 6)

    # Function to roll two dice and return the results
    def roll_dice(self):
        return self.roll_die(), self.roll_die()


class Vertex:
    def __init__(self, x: int, y: int, ):
        self.settlement = False
        self.city = False
        self.Adjacent = []
        self.button = VertexButton(x, y, 10)
        self.color = (0, 0, 0)
        self.x = x
        self.y = y

    def buy_settlement(self, player: Player):
        wood_cost = 1
        brick_cost = 1
        wheat_cost = 1
        sheep_cost = 1
        if player.place_settlement(player, wood_cost, brick_cost, wheat_cost, sheep_cost):
            self.settlement = True
            self.color = player.color

    def buy_city(self):
        self.settlement = False
        self.city = True

    def draw(self, surface):
        if self.settlement:
            pygame.draw.polygon(surface, self.color,
                                [(self.x, self.y - 20), (self.x + 20, self.y + 5), (self.x - 20, self.y + 5)])

        if self.city:
            pygame.draw.polygon(surface, self.color,
                                [(self.x - 10, self.y - 10), (self.x + 10, self.y - 10), (self.x - 10, self.y + 10),
                                 (self.x + 10, self.y + 10)])
