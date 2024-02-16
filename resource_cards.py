from enum import Enum


class Card(Enum):
    WOOD = 0
    BRICK = 1
    WOOL = 2
    WHEAT = 3
    ORE = 4

class Resource_Cards:

    def __init__(self, type: Card):
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def name(self, type: Card):
        self.__type = type
