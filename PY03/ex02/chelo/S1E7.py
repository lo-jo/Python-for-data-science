from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self):
        """Returns a string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a more information-rich, or official,
        string representation of an object"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Your docstring for Method die"""
        self.is_alive = False

    def __str__(self):
        """Returns a string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a more information-rich, or official,
        string representation of an object"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Do incest"""
        return cls(first_name, is_alive)
