from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """Constructor"""
        super().__init__(first_name, is_alive=True)

    def set_eyes(self, eyes):
        """Sets eye color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Sets hair color"""
        self.hairs = hairs

    def get_eyes(self):
        """Gets eye color"""
        return self.eyes
    
    def get_hairs(self):
        """Gets hair color"""
        return self.hairs