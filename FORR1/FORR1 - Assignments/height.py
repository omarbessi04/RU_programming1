class Height:
    """Height class containing height in feet/inches"""

    def __init__(self, feet, inches) -> None:
        """Initialize the Height class"""

        self.imperial = True
        self.feet = int(feet)
        self.inches = int(inches)
        self.height_cm = 0

        while self.inches >= 12:
            self.inches -= 12
            self.feet += 1

    def cm(self) -> int:
        """Convert imperial height to centimeters"""

        self.height_cm = 0
        self.height_cm += self.feet * 30.48
        self.height_cm += self.inches * 2.54

        self.height_cm = round(self.height_cm)
        self.imperial = False

        return self.height_cm
    
    def __gt__(self, other) -> bool:
        """Check whether height is greater than other height"""

        if self.feet > other.feet:
            return True
        
        if self.feet == other.feet:
            if self.inches > other.inches:
                return True

        return False

    def __add__(self, other) -> 'Height':
        """Add two heights together"""

        feet = self.feet + other.feet
        inches = self.inches + other.inches

        if inches >= 12:
            inches -= 12
            feet += 1

        new_height = Height(feet, inches)
        return new_height

    def __str__(self) -> str:
        """String representation of height"""
        
        if self.imperial:
            output = f"{self.feet} ft, {self.inches} in"
        else:
            output = f"{self.height_cm} "

        return output
    