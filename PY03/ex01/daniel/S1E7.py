from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Returns a string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a more information-rich, or official,
        string representation of an object"""
        return self.__str__()

    def die(self):
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Returns a string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a more information-rich, or official,
        string representation of an object"""
        return self.__str__()

    def die(self):
        self.is_alive = False

    # In Python, the @classmethod decorator
    # is used to declare a method in the class
    # as a class method that can be called using ClassName.MethodName().
    # The class method can also be called using an object of the class.
    # What I can do with a @classmethod ?
    # Declares a class method.
    # The first parameter must be cls
    # which can be used to access class attributes.
    # The class method can only access the class attributes
    # but not the instance attributes.
    # The class method can be called using ClassName.MethodName()
    # and also using object.
    # It can return an object of the class.

    # The class method can also be used as
    # a factory method to get an object of the class, as shown below.
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        return cls(first_name, is_alive)
