class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)

    def get_picture(self):
        line = ""
        if self.width > 50 or self.height > 50:
            return ("Too big for picture.")
        else:
            for i in range(self.height):
                line = line + "*" * self.width + "\n"
        return (line)

    def get_amount_inside(self, shape):
        return(int(self.get_area() / shape.get_area()))


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        rep = 'Square(side=' + str(self.width) + ')'
        return rep
        # return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
