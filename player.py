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