from abc import ABC, abstractmethod


class Character(ABC):
    """Base class Character
    which can take a first_name as first parameter,
    is_alive as second non mandatory parameter set to True by default"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """CONSTRUCTOR"""
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Base class method die"""
        pass
    # #your code here


class Stark(Character):
    """Child class, inherits from character"""
    def __init__(self, name, is_alive=True):
        """Constructor for child class"""
        super(Stark, self).__init__(name, is_alive=True)

    def die(self):
        """passes is_alive from True to False"""
        self.is_alive = False
