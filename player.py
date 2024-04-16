"""This file holds the player class"""
import pygame
import buildings

class Player:
    """
    This class stores data associated with the Player object

    Attributes:
        color(int, int, int): player color
        wood(int): number of wood cards the player holds
        brick(int): number of brick cards the plauer holds
        sheep(int): number of sheep cards the player holds
        wheat(int): number of wheat cards the player holds
        ore(int): number of ore cards the player holds
        settlements(int): number of settlements the player has
        cities(int): numbre of cities the player has
        roads(int): number of roads the player has
        after(player): the player with the next turn
        before(player): the player with the previous turn
        name(string): the player name
        turn(int): number of turns the player has taken
        cards(int): number of cards the player holds
    """

    def __init__(self, name, color):
        """
        Constructor for the Player class
        """
        self.__color = color
        self.image = None
        if color == (255, 265, 0):
            self.image = pygame.image.load("buildings/red_settlement.png")
        if color == (0, 0, 255):
            self.image = pygame.image.load("buildings/blue_settlement.png")
        self.__wood = 0
        self.__brick = 0
        self.__sheep = 0
        self.__wheat = 0
        self.__ore = 0
        self.__settlements = 0
        self.__cities = 0
        self.__roads = 0
        self.__after = None
        self.__before = None
        self.__development_cards = []
        self.name = name
        self.__turn = 0
        self.__cards = 0

    def __str__(self):
        return self.name


    def collect_resource(self, resource_type: str):
        if resource_type == "wood":
            self.collect_wood(1)
        elif resource_type == "brick":
            self.collect_brick(1)
        elif resource_type == "sheep":
            self.collect_sheep(1)
        elif resource_type == "wheat":
            self.collect_wheat(1)
        elif resource_type == "ore":
            self.collect_ore(1)

    def decrease_resource(self, resource_type: str):
        if resource_type == "wood":
            self.collect_wood(1)
        elif resource_type == "brick":
            self.collect_brick(1)
        elif resource_type == "sheep":
            self.collect_sheep(1)
        elif resource_type == "wheat":
            self.collect_wheat(1)
        elif resource_type == "ore":
            self.collect_ore(1)

    @property
    def color(self):
        """
        Getter for the color attribute

        :return: color
        """
        return self.__color

    @color.setter
    def color(self, value):
        """
        Setter for the color attribute
        :param value: new color
        """
        self.__color = value

    @property
    def before(self):
        """
        Getter for the before attribute
        :return: before
        """
        return self.__before

    @before.setter
    def before(self, value):
        """
        Setter for the before attribute
        :param value: new player
        """
        self.__before = value

    @property
    def name(self) -> str:
        """returns name"""
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """sets name. if value is null, name is set to 'no name'."""
        if value == "":
            self.__name = "Player"
        self.__name = value

    # Getters and Setters for Buildings
    @property
    def roads(self) -> int:
        """
        Getter for the roads attribute
        :return: roads
        """
        return self.__roads

    @roads.setter
    def roads(self, num: int):
        """
        Setter for the roads atribute
        :param num: new number of roads
        """
        self.__roads = num

    def add_road(self):
        """
        Adds one road to the number of roads the player has
        """
        self.__roads += 1

    @property
    def settlements(self) -> int:
        """
        Getter for the settlements attribute
        :return: settlements
        """
        return self.__settlements

    @settlements.setter
    def settlements(self, num: int):
        """
        Setter for the settlements attribute
        :param num: new number of settlements
        """
        self.__settlements = num

    def add_settlement(self):
        """
        Adds one settlement
        """
        self.__settlements += 1

    def place_settlement(self, player):
        if player.turn == 0 and self.__settlements < 2:
            self.settlements += .5
            return True
        if int(self.wood) >= 1 and int(self.brick) >= 1 and int(self.wheat) >= 1 and int(
                self.sheep) >= 1:
            self.__wood -= 1
            self.__brick -= 1
            self.__wheat -= 1
            self.__sheep -= 1
            self.settlements += 1
            print(player.turn)
            return True
        else:
            return False

    @property
    def cities(self) -> int:
        """
        Getter for cities attribute
        :return: cities
        """
        return self.__cities

    @cities.setter
    def cities(self, num: int):
        """
        Setter for cities attribute
        :param num: new number of cities
        """
        self.__cities = num

    def add_city(self):
        """
        Adds one city and removes one settlement in exchange
        """
        self.__cities += 1
        self.__settlements -= 1

    # Getters and Setters for resource cards

    @property
    def wood(self) -> str:
        """
        Getter for the wood attribute
        :return: wood
        """
        return str(self.__wood)

    @wood.setter
    def wood(self, num: int):
        """
        Setter for the wood attribute
        :param num: new number of wood cards
        """
        self.__wood = num

    def collect_wood(self, num: int):
        """
        Collects any number of wood cards
        :param num: number of wood cards
        """
        self.__wood += num
        self.__cards += num

    @property
    def brick(self) -> int:
        """
        Getter for brick attribute
        :return: brick
        """
        return self.__brick

    @brick.setter
    def brick(self, num: int):
        """
        Setter for brick attribute
        :param num: new number of bricks
        """
        self.__brick = num

    def collect_brick(self, num: int):
        """
        Collects any number of brick cards
        :param num: number of brick cards to collect
        """
        self.__brick += num
        self.__cards += num

    @property
    def sheep(self) -> int:
        """
        Getter for sheep attribute
        :return: sheep
        """
        return self.__sheep

    @sheep.setter
    def sheep(self, num: int):
        """
        Setter for sheep attribute
        :param num: new number of sheep
        """
        self.__sheep = num

    def collect_sheep(self, num: int):
        """
        Collects any number of sheep
        :param num: number of sheep to be collected
        :return:
        """
        self.__sheep += num
        self.__cards += num

    @property
    def wheat(self) -> int:
        """
        getter for wheat attribute
        :return: wheat
        """
        return self.__wheat

    @wheat.setter
    def wheat(self, num: int):
        """
        Setter for wheat attribute
        :param num: new number of wheat cards
        """
        self.__wheat = num

    def collect_wheat(self, num: int):
        """
        Collects any number of wheat cards
        :param num: number of wheat cards to collect
        """
        self.__wheat += num
        self.__cards += num

    @property
    def ore(self) -> int:
        """
        Getter for ore attribute
        :return: ore
        """
        return self.__ore

    @ore.setter
    def ore(self, num: int):
        """
        Setter for ore attribute
        :param num: new number of ore cards
        """
        self.__ore = num

    def collect_ore(self, num: int):
        """
        Collects any number of ore cards
        :param num: number of ore cards to collect
        """
        self.__ore += num
        self.__cards += num

    @property
    def turn(self) -> int:
        """
        Getter for turn attribute
        :return: turn
        """
        return self.__turn

    @turn.setter
    def turn(self, num: int):
        """
        Setter for turn attribute
        :param num: new turn number
        """
        self.__turn = num

    def next_turn(self):
        """
        Increments the turn attribute
        """
        self.turn += 1
