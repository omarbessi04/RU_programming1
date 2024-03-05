import string
class ComplexNumber:
    def __init__(self, a = 0, b = 0,):
        self.a = a
        self.b = b

    def __repr__(self):
        output = f"ComplexNumber({self.a}, {self.b})"
        return output

    def __str__(self):
        if self.a == 0:
            if self.b == 0:
                return "0"
            else:
                return f"{self.b}i"
            
        if self.b == 0:
            return f"{self.a}"
        
        if self.a < 0:
            x = f"-{str(self.a).strip(string.punctuation)}"
        else:
            x = self.a

        if self.b < 0:
            y = f"- {str(self.b).strip(string.punctuation)}"
        else:
            y = f"+ {self.b}"

        return f"{x} {y}i"
    
    def __eq__(self, comparison):
        if self.a == comparison.a:
            if self.b == comparison.b:
                return True
            
        return False
    
    def __neg__(self):
        if self.a < 0:
            new_a = self.a - (self.a*2)
        else:
            new_a = -self.a

        if self.b < 0:
            new_b = self.b - (self.b*2)
        else:
            new_b = -self.b

        return ComplexNumber(new_a, new_b)
    
    def __add__(self, addition):
        first = self.a + addition.a
        second = self.b + addition.b

        output = ComplexNumber(first, second)
        return output

    def __sub__(self, subtraction):
        first = self.a - subtraction.a
        second = self.b - subtraction.b

        output = ComplexNumber(first, second)
        return output

    def __mul__(self, multiple):

        first = (self.a*multiple.a - self.b*multiple.b)
        second = (self.a*multiple.b + self.b*multiple.a)
        output = ComplexNumber(first, second)
        return output
    
    def __truediv__(self, division):
        return self*division.inverse()

    def conjugate(self):
        if self.b < 0:
            new_b = self.b - (self.b*2)
        else:
            new_b = -self.b

        return ComplexNumber(self.a, new_b)

    def re(self):
        return self.a
    
    def im(self):
        return self.b
    
    def inverse(self):
        if self.a + self.b == 0:
            return 0
        first = self.a/(self.a**2 + self.b**2)
        second = -self.b/(self.a**2 + self.b**2)
        output = ComplexNumber(first, second)
        return output