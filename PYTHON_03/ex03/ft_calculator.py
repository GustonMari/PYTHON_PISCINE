class calculator:

    def __init__(self, vector) -> None:
        self.vector = vector
        # print(self.vector)

    def __add__(self, number) -> None:
        for i in range(len(self.vector)):
            self.vector[i] += number
        print(self.vector)

    def __add__(self, number) -> None:
        
        # for i in range(len(self.vector)):
        #     self.vector[i] += number
        self.vector = [x + number for x in self.vector]
        print(self.vector)

    def __mul__(self, number) -> None:
        self.vector = [x * number for x in self.vector]
        print(self.vector)

    def __sub__(self, number) -> None:
        self.vector = [x - number for x in self.vector]
        print(self.vector)

    def __truediv__(self, number) -> None:
        self.vector = [x / number for x in self.vector]
        print(self.vector)
