"""This file holds the player class"""

class Player:
    """

    """
    def __init__(self, name):
        self.__wood = 0
        self.__brick = 0
        self.__wool = 0
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
        self.__cards

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

    @roads.setter
    def settlements(self, num: int):
        self.__settlements = num

    def add_settlement(self):
        self.__settlements += 1

    @property
    def cities(self) -> int:
        return self.__cities

    @cities.setter
    def cities(self, num: int):
        self.__cities == num

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
        self.__wood += 1
        self.__cards += 1

    @property
    def brick(self) -> int:
        return self.__brick

    @brick.setter
    def brick(self, num: int):
        self.__brick = num

    def collect_brick(self, num: int):
        self.__brick += 1
        self.__cards += 1

    @property
    def wool(self) -> int:
        return self.__wool

    @wool.setter
    def wool(self, num: int):
        self.__wool = num

    def collect_wool(self, num: int):
        self.__wool += 1
        self.__cards += 1

    @property
    def wheat(self) -> int:
        return self.__wheat

    @wheat.setter
    def wheat(self, num: int):
        self.__wheat = num

    def collect_wheat(self, num: int):
        self.__wheat += 1
        self.__cards += 1

    @property
    def ore(self) -> int:
        return self.__ore

    @ore.setter
    def ore(self, num: int):
        self.__ore = num

    def collect_ore(self, num: int):
        self.__ore += 1
        self.__cards += 1

    @property
    def turn(self) -> int:
        return self.__turn

    @turn.setter
    def turn(self, num: int):
        self.__turn = num

    def next_turn(self):
        self.__turn += 1

