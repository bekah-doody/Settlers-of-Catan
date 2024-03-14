"""This file holds the player class"""

class Player:
    """

    """
    def __init__(self, name, color):
        self.__color = color
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
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def before(self):
        return self.__before

    @before.setter
    def before(self, value):
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

    #Getters and Setters for Buildings
    @property
    def roads(self) -> int:
        return self.__roads

    @roads.setter
    def roads(self, num: int):
        self.__roads = num

    def add_road(self):
        self.__roads+=1

    @property
    def settlements(self) -> int:
        return self.__settlements

    @settlements.setter
    def settlements(self, num: int):
        self.__settlements = num

    def add_settlement(self):
        self.__settlements += 1

    @property
    def cities(self) -> int:
        return self.__cities

    @cities.setter
    def cities(self, num: int):
        self.__cities = num

    def add_city(self):
        self.__cities += 1
        self.__settlements -= 1


    #Getters and Setters for resource cards

    @property
    def wood(self) -> int:
        return self.__wood

    @wood.setter
    def wood(self, num: int):
        self.__wood = num

    def collect_wood(self, num: int):
        self.__wood += num
        self.__cards += num

    @property
    def brick(self) -> int:
        return self.__brick

    @brick.setter
    def brick(self, num: int):
        self.__brick = num

    def collect_brick(self, num: int):
        self.__brick += num
        self.__cards += num

    @property
    def sheep(self) -> int:
        return self.__sheep

    @sheep.setter
    def sheep(self, num: int):
        self.__sheep = num

    def collect_sheep(self, num: int):
        self.__sheep += num
        self.__cards += num

    @property
    def wheat(self) -> int:
        return self.__wheat

    @wheat.setter
    def wheat(self, num: int):
        self.__wheat = num

    def collect_wheat(self, num: int):
        self.__wheat += num
        self.__cards += num

    @property
    def ore(self) -> int:
        return self.__ore

    @ore.setter
    def ore(self, num: int):
        self.__ore = num

    def collect_ore(self, num: int):
        self.__ore += num
        self.__cards += num

    @property
    def turn(self) -> int:
        return self.__turn

    @turn.setter
    def turn(self, num: int):
        self.__turn = num

    def next_turn(self):
        self.__turn += 1

