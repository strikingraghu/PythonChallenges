"""Code to explain details around Python classes and it's methods"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be a positive integer')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be a positive integer')
        self._height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return "Rectangle Object: Width {0} & Height {1}".format(self.width, self.height)


if __name__ == "__main__":
    x = Rectangle(10, 20)
    y = Rectangle(20, 40)
    print("Calculating X rectangle area = ", x.calculate_area())
    print("Calculating X rectangle perimeter = ", x.calculate_perimeter())
    print("Calculating Y rectangle area = ", y.calculate_area())
    print("Calculating Y rectangle perimeter = ", y.calculate_perimeter())
    print(x)
    print(y)
