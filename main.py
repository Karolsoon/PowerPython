class Generator:

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


class Array_filler(Generator):

    super().__init__()

    def generate_numbers(self):
        bla = 1

    def generate_string(self):
        pass

    def generate_bullshit(self):
        pass
