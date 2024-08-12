from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Create a bastard King"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Change the color of eyes"""
        self.eyes = color

    def set_hairs(self, color):
        """Change color hair"""
        self.hairs = color

    def get_eyes(self) -> str:
        """Get the color of eyes"""
        return self.eyes

    def get_hairs(self) -> str:
        """Get the color of hair"""
        return self.hairs
