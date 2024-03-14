"This class holds Game and Vertex. Game holds all the information on "

from player import Player
from vertex_button import VertexButton
import pygame
import random
class Game:
    """
    Holds information on the game. Includes which players turn it is along with if a vertex has been clicked and what player has it.

    """
    def __init__(self):
        self.players = [Player("player1", ((255, 165, 0))), Player("player2", ((0, 0, 255)))]
        self.vertices = []
        self.current_player = None

    def generate_vertices(self) -> list:
        "Generates all vertices and fills self.vertices"
        temp = []
        #top
        temp.append(Vertex(480, 101))
        temp.append(Vertex(601, 101))
        temp.append(Vertex(726, 101))
        #2nd top
        temp.append(Vertex(787, 135))
        temp.append(Vertex(662, 135))
        temp.append(Vertex(544, 135))
        temp.append(Vertex(421, 135))
        #3rd row
        temp.append(Vertex(419, 205))
        temp.append(Vertex(544, 205))
        temp.append(Vertex(662, 205))
        temp.append(Vertex(784, 205))
        #4th row
        temp.append(Vertex(361, 241))
        temp.append(Vertex(480, 241))
        temp.append(Vertex(603, 241))
        temp.append(Vertex(725, 241))
        temp.append(Vertex(848, 241))
        #5th row
        temp.append(Vertex(361, 312))
        temp.append(Vertex(480, 312))
        temp.append(Vertex(603, 312))
        temp.append(Vertex(725, 312))
        temp.append(Vertex(848, 312))
        #6th row
        temp.append(Vertex(300, 346))
        temp.append(Vertex(420, 346))
        temp.append(Vertex(544, 346))
        temp.append(Vertex(662, 346))
        temp.append(Vertex(784, 346))
        temp.append(Vertex(908, 346))
        #7th row
        temp.append(Vertex(300, 416))
        temp.append(Vertex(420, 416))
        temp.append(Vertex(544, 416))
        temp.append(Vertex(662, 416))
        temp.append(Vertex(784, 416))
        temp.append(Vertex(908, 416))
        #8th row
        temp.append(Vertex(361, 452))
        temp.append(Vertex(480, 452))
        temp.append(Vertex(603, 452))
        temp.append(Vertex(725, 452))
        temp.append(Vertex(848, 452))
        #9th row
        temp.append(Vertex(361, 521))
        temp.append(Vertex(480, 521))
        temp.append(Vertex(603, 521))
        temp.append(Vertex(725, 521))
        temp.append(Vertex(848, 521))
        #10th row
        temp.append(Vertex(420, 556))
        temp.append(Vertex(544, 556))
        temp.append(Vertex(662, 556))
        temp.append(Vertex(784, 556))
        #11th row
        temp.append(Vertex(421, 627))
        temp.append(Vertex(544, 627))
        temp.append(Vertex(662, 627))
        temp.append(Vertex(784, 627))
        #12th row
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
            if not num == len(self.players)-1:
                self.players[num].before = self.players[num+1]
        self.players[len(self.players)-1].before = self.players[0]

    def change_player(self):

        self.current_player = self.current_player.before

    # Function to roll a single die
    def roll_die(self):
        return random.randint(1, 6)


    # Function to roll two dice and return the results
    def roll_dice(self):
        return self.roll_die(), self.roll_die()


class Vertex:
    def __init__(self, x: int, y: int,):
        self.settlement = False
        self.city = False
        self.Adjacent = []
        self.button = VertexButton(x, y, 10)
        self.color = (0, 0, 0)
        self.x = x
        self.y = y

    def buy_settlement(self, player: Player):
        self.settlement = True
        self.color = player.color


    def buy_city(self):
        self.settlement = False
        self.city = True


    def draw(self, surface):
        if self.settlement:
            pygame.draw.polygon(surface, self.color, [(self.x, self.y-20),(self.x+20, self.y+5),(self.x-20, self.y+5)])

        if self.city:
            pygame.draw.polygon(surface, self.color, [(self.x-10, self.y-10),(self.x+10, self.y-10),(self.x-10, self.y+10),(self.x+10, self.y+10)])




