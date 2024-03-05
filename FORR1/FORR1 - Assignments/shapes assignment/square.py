from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, sides):
        self.side1 = sides
        self.side2 = sides
        super().__init__(self.side1, self.side2)