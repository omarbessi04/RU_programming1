import math
class Vector:
    def __init__(self, x_dim = 0, y_dim = 0, z_dim = 0) -> None:
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.z_dim = z_dim
        self.dimension_list = [self.x_dim, self.y_dim, self.z_dim]

    def __abs__(self):
        output = math.sqrt(self.x_dim**2 + self.y_dim**2 + self.z_dim**2)
        output
        return output
    
    def __add__(self, addition):
        first = self.dimension_list[0] + addition.dimension_list[0]
        second = self.dimension_list[1] + addition.dimension_list[1]
        third = self.dimension_list[2] + addition.dimension_list[2]
        new_vec = Vector(first, second, third)
        return new_vec
    
    def __sub__(self, subtraction):
        first = self.dimension_list[0] - subtraction.dimension_list[0]
        second = self.dimension_list[1] - subtraction.dimension_list[1]
        third = self.dimension_list[2] - subtraction.dimension_list[2]
        new_vec = Vector(first, second, third)
        return new_vec

    def __eq__(self, could_be_equal):
        CON = 0.0000001
        almost_zero = could_be_equal - self
        if -CON <= abs(almost_zero) <= CON:
            return True
        else:
            return False
        
    def __mul__(self, multiple):
        lst = []
        for num in self.dimension_list:
            lst.append(num*multiple)

        new_vec = Vector(lst[0], lst[1], lst[2])
        return new_vec
    
    def __repr__(self):
        output = f"Vector({self.dimension_list[0]}, {self.dimension_list[1]}, {self.dimension_list[2]})"
        return output

    def __rmul__(self, variable):
        new_vec = self * variable
        return new_vec
    
    def __gt__(self, greater):
        if abs(self) > abs(greater):
            return True
        else:
            return False
        
    def __ge__(self, greater_or_eq):
        if abs(self) >= abs(greater_or_eq):
            return True
        else:
            return False
        
    def __lt__(self, lesser):
        if abs(self) < abs(lesser):
            return True
        else:
            return False

    def __lt__(self, lesser_or_eq):
        if abs(self) < abs(lesser_or_eq):
            return True
        else:
            return False
        
    def dot(self, new):
        sum = 0
        for i in range(3):
            sum += self.dimension_list[i] * new.dimension_list[i]

        return sum

    def cross(self, new):
        lst = [0, 0, 0]
        lst[0] = (self.dimension_list[1] * new.dimension_list[2]) - (self.dimension_list[2] * new.dimension_list[1])
        lst[1] = (self.dimension_list[2] * new.dimension_list[0]) - (self.dimension_list[0] * new.dimension_list[2])
        lst[2] = (self.dimension_list[0] * new.dimension_list[1]) - (self.dimension_list[1] * new.dimension_list[0])

        n = Vector(lst[0], lst[1], lst[2])
        return n
    
    def __str__(self):
        return f"[[ {self.dimension_list[0]} {self.dimension_list[1]} {self.dimension_list[2]} ]]"
