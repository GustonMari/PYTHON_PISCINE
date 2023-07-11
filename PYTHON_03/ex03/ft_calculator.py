class calculator:

    def __init__(self, vector) -> None:
        """init method"""
        self.vector = vector
        # print(self.vector)

    def __add__(self, number) -> None:
        """add method"""
        # for i in range(len(self.vector)):
        #     self.vector[i] += number
        self.vector = [x + number for x in self.vector]
        print(self.vector)

    def __mul__(self, number) -> None:
        """multiply method"""
        self.vector = [x * number for x in self.vector]
        print(self.vector)

    def __sub__(self, number) -> None:
        """substract method"""
        self.vector = [x - number for x in self.vector]
        print(self.vector)

    def __truediv__(self, number) -> None:
        """division method"""
        if number == 0:
            print("Division by 0 is impossible")
            return
        self.vector = [x / number for x in self.vector]
        print(self.vector)
