from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Base class constructor"""
        pass

    @abstractmethod
    def die(self):
        """Base class method die"""
        pass


class Stark(Character):
    def __init__(self, name, is_alive=True):
        """CONSTRUCTOR"""
        self.name = name
        self.is_alive = is_alive

    def die(self):
        """passes is_alive from True to False"""
        self.is_alive = False
