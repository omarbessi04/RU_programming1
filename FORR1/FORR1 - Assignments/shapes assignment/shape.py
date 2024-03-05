class Shape():

    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def __str__(self):
        output = f"{type(self).__name__} with area of {self.area:.2f} and perimeter of {self.perimeter:.2f}"
        return output