"""Code to explain details around Python classes and it's methods"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    x = Rectangle(10, 20)
    y = Rectangle(20, 40)
    print("Calculating X rectangle area = ", x.calculate_area())
    print("Calculating X rectangle perimeter = ", x.calculate_perimeter())
    print("Calculating Y rectangle area = ", y.calculate_area())
    print("Calculating Y rectangle perimeter = ", y.calculate_perimeter())
