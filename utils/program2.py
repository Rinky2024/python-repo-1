class Shape:
    def area(self):
        print("Output of Shape's area(): 0")


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        result = self.length * self.length
        print(f"Output of Square's area(): {result}")


# Unit tests for Program 2
def test_program2():
    square = Square(4)
    shape = Shape()

    assert square.area() == 16
    assert shape.area() == 0

    # Additional tests can be added based on the specific requirements
