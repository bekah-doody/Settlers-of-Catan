# This file contains classes for base game development cards

from abc import *


class DevelopmentCard(ABC):
    # Abstract class for Development Cards
    def __init__(self):
        # function to initialize object
        pass
    @abstractmethod
    def __str__(self):
        # Abstract method which is for the title/ description of the card
        pass
    @abstractmethod
    def CheckMaterials(self, ore, wheat, wool):
        # this function is supposed to be used to check if a player has enough material
        # in their inventory to get the development card
        pass


class KnightCard(DevelopmentCard):
    def __str__(self):
        print("Knight Card")
        print("You can move the robber! \n"
              " and you can steal 1 resource from the owner of a settlement\n"
              " or adjacent to the robber's new hex.")

    def CheckMaterials(self, ore, wheat, wool):
        pass


class RoadBuilding(DevelopmentCard):
    def __str__(self):
        print("Road Building Card")
        print("Place 2 new roads as if you had just built them!")

    def CheckMaterials(self, ore, wheat, wool):
        pass


class YearOfPlenty(DevelopmentCard):
    def __str__(self):
        print("Year of Plenty Card")
        print("Take any 2 resources from the bank!\n"
              "Add them to your hand.\n"
              "They can be 2 of the same or different resources")

    def CheckMaterials(self, ore, wheat, wool):
        pass


class Monopoly(DevelopmentCard):
    def __str__(self):
        print("Monopoly Card")
        print("When you play this card, announce 1 type of resource card.\n"
              "All players must give you all of their resource cards of that type")

    def CheckMaterials(self, ore, wheat, wool):
        pass


class VictoryPointCard(DevelopmentCard):
    def __str__(self):
        print("Victory Point Card")
        print("1 free Victory Point! :D")

    def CheckMaterials(self, ore, wheat, wool):
        pass


