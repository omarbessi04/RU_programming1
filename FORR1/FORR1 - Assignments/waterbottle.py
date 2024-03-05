class WaterBottle:
    def __init__(self, max_capacity = 2) -> None:
        self.max_capacity = max_capacity
        self.current_contents = 0

    def fill(self) -> None:
        self.current_contents = float(self.max_capacity)
        
    def drink(self, amount: float) -> float:
        if amount < 0:
            return 0
        if amount > self.current_contents:
            previous_amount = self.current_contents
            self.current_contents = 0
            return previous_amount
        else:
            self.current_contents = self.current_contents - amount
            return amount
   
    def __str__(self) -> str:
        output = self.current_contents
        return f"The bottle currently holds {output:.1f}L of water."