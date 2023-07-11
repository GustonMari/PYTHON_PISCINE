class calculator:

    # ! the dot product or also known as the scalar product
    # ! is an algebraic operation that takes two equal-length sequences
    # ! of numbers and returns a single number
    # ? list(zip('abcdefg', range(3), range(4)))
    # ? ==> [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product between two vectors"""
        if len(V1) != len(V2):
            print("Error")
            return
        res = 0
        res = sum([x * y for x, y in zip(V1, V2)])
        print("Dot product is:", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """addition between two vectors"""
        if len(V1) != len(V2):
            print("Error")
            return
        res = [x + y for x, y in zip(V1, V2)]
        print("Add Vector is :", res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """soustract between two vectors"""
        if len(V1) != len(V2):
            print("Error")
            return
        res = [x - y for x, y in zip(V1, V2)]
        print("Sous Vector is:", res)
