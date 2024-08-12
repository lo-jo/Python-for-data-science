from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Class in python"""
    # @abc.abstractmethod
    # A decorator indicating abstract methods.
    # Using this decorator requires that the class’s metaclass
    # is ABCMeta or is derived from it.
    # A class that has a metaclass derived from ABCMeta cannot be
    # instantiated unless all of its
    # abstract methods and properties are overridden.
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Constructor of class Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract function of class Character"""
        pass


class Stark(Character):
    """Child Class"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of class Stark"""
        super().__init__(first_name, is_alive=True)

    def die(self):
        """Passes is_alive from True to False"""
        self.is_alive = False
