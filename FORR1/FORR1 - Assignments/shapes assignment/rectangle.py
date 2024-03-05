from shape import Shape
class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.area = 0
        self.perimeter = 0
        self.side1 = side1
        self.side2 = side2
        super().__init__(self.area, self.perimeter)

    def get_area(self):
        self.area = self.side1 * self.side2
        return self.area

    def get_perimeter(self):
        self.perimeter = 2* self.side1 + 2 * self.side2
        return self.perimeter
    
    def get_perimiter(self):
        return self.get_perimeter
    
    def __str__(self):
        self.get_area()
        self.get_perimeter()
        output = f"{type(self).__name__} with area of {self.area:.2f} and perimeter of {self.perimeter:.2f}"
        return output