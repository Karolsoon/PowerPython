class arrayGenerator:

    def __init__(self, x=0, y=0, array_x_on_y=None):
        if array_x_on_y is None:
            array_x_on_y = [0, 0]
        self.x = x
        self.y = y
        self.array_x_on_y = array_x_on_y

    def generate_array(self, x, y):
        self.array_x_on_y = [y
                             for y in x
                             for x in x]

    def snitches(self):
        pass


class arrayFiller(arrayGenerator):

    super().__init__()

    def generate_numbers(self):
        pass

    def generate_string(self):
        pass

    def generate_bullshit(self):
        pass

