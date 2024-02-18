import abc


class ResourceCard(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
    #
    # @property
    # def type(self) -> str:
    #     return self.__type
    #
    # @type.setter
    # def name(self, type: Card):
    #     self.__type = type


class BrickCard(ResourceCard):
    def __str__(self):
        return "Brick Card"


class WoodCard(ResourceCard):
    def __str__(self):
        return "Wood Card"


class SheepCard(ResourceCard):
    def __str__(self):
        return "Sheep Card"


class WheatCard(ResourceCard):
    def __str__(self):
        return "Wheat Card"


class OreCard(ResourceCard):
    def __str__(self):
        return "Ore Card"
