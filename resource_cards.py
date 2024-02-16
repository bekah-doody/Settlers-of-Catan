
class Resource_Cards:

    def __init__(self, type: str):
        self.__type = type
        self.__name = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, type):
        self.__name = type
