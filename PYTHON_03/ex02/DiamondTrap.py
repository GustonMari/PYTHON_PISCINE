from S1E7 import Baratheon, Lannister

# ! this is the better way to do the exercise the second technique is not a good practice
# ! https://cutt.ly/cwiZ4krG
# class King(Baratheon, Lannister):
#     """King class"""

#     def ____init__(self, first_name, is_alive=True):
#         super().__init__(first_name, is_alive)

#     @property
#     def eyes(self):
#         """get_eyes method"""
#         return self._eyes

#     @property
#     def hairs(self):
#         """get_hairs method"""
#         return self._hairs

#     @eyes.setter
#     def eyes(self, eyes):
#         """set_eyes method"""
#         self._eyes = eyes

#     @hairs.setter
#     def hairs(self, hairs):
#         """set_hairs method"""
#         self._hairs = hairs



# !this way is the way with property() function technique
# !the technique above is the decorator technique
# ? its better to use the decorator technique !!!!
class King(Baratheon, Lannister):
    """King class"""

    def ____init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """set_eyes method"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """set_hairs method"""
        self.hairs = hairs

    def get_eyes(self):
        """get_eyes method"""
        return self.eyes

    def get_hairs(self):
        """get_hairs method"""
        return self.hairs
