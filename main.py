class arrayGenerator:

    def __init__(self, x=0, y=0, array_x_on_y=None):
        if array_x_on_y is None:
            array_x_on_y = [0, 0]
        self.x = x
        self.y = y
        self.array_x_on_y = array_x_on_y

    def generateArray(self, x, y):
        self.array_x_on_y = [y
                             for y in x
                             for x in x]

    def generateSnitches(self):
        pass


class arrayFiller(arrayGenerator):

    def fillArrayWithNumbers(self, x, y):
        super().__init__()
        array_x_on_y = [[y for y in range(y)] for x in range(x)]
        return  array_x_on_y

    def fillArrayWithString(self):
        pass

    def fillArrayWithBullshit(self):
        pass

