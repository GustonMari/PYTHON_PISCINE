from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
            super().__init__(first_name, is_alive)
            self.family_name = "Baratheon"
            self.eyes = "brown"
            self.hairs = "dark"

    def die(self):
        """die method"""
        return super().die()

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"


class Lannister(Character):
    """Lannister class"""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        """die method"""
        return super().die()

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        """create_lannister method"""
        return Lannister(first_name, is_alive)
