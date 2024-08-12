from S1E7 import Baratheon, Lannister

# Method Resolution Order (MRO) is the order in which Python looks for
# a method in a hierarchy of classes.


class King(Baratheon, Lannister):
    """Create a bastard King"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, value_eyes):
        self.eyes = value_eyes

    def set_hairs(self, value_hairs):
        self.hairs = value_hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
