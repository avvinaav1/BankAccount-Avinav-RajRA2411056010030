class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


def demonstrate_violation():
    rectangle = Square()
    rectangle.set_width(10)
    rectangle.set_height(20)

    # A Rectangle caller expects independent dimensions and therefore expects 200.
    # Square keeps both dimensions equal, so the observed result is 400.
    return rectangle.area()


if __name__ == "__main__":
    print(demonstrate_violation())
