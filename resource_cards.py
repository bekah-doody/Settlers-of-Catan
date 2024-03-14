import abc


class ResourceCard(abc.ABC):
    """
    The abstract class for the resources cards
    """

    def __init__(self):
        #Constructor
        pass

    @abc.abstractmethod
    def __str__(self):
        #str method
        pass


class BrickCard(ResourceCard):
    """
    BrickCard class that is a child of ResourceCard
    """
    def __str__(self):
        """
        returns name of resource card
        """
        return "Brick Card"


class WoodCard(ResourceCard):
    """
    WoodCard class that is a child of ResourceCard
    """
    def __str__(self):
        """
        returns name of resource card
        """
        return "Wood Card"


class SheepCard(ResourceCard):
    """
    SheepCard class that is a child of ResourceCard
    """
    def __str__(self):
        """
        returns name of resource card
        """
        return "Sheep Card"


class WheatCard(ResourceCard):
    """
    WheatCard class that is a child of ResourceCard
    """
    def __str__(self):
        """
        returns name of resource card
        """
        return "Wheat Card"


class OreCard(ResourceCard):
    """
    OreCard class that is a child of ResourceCard
    """
    def __str__(self):
        """
        returns name of resource card
        """
        return "Ore Card"
