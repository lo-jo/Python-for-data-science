from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon Family"""
    def __init__(self, first_name, is_alive=True):
        """CONSTRUCTOR"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "dark"
    
    def die(self):
        """passes is_alive from True to False"""
        self.is_alive = False

    def __str__(self):
        return f"({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__ (self):
        vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector : {vector}"
        

class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        """CONSTRUCTOR"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "Blue"
        self.hairs = "Light"

    def die(self):
        """passes is_alive from True to False"""
        self.is_alive = False

    def __str__(self):
        return f"({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__ (self):
        vector = (self.family_name, self.eyes, self.hairs)
        return f"{vector}"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """ METHOD CHAINING"""
        # character = cls(first_name, is_alive)
        return cls(first_name, is_alive)