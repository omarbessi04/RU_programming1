class Item:
    """Create an item with a name and category"""
    def __init__(self, name: str, category: str) -> None:
        """Initialize an Item with a name and category"""
        self.name = name
        self.category = category

    def set_name(self, new_name: str) -> None:
        """Change/Set name of item"""
        self.name = new_name

    def set_category(self, new_category: str) -> None:
        "Change/Set name of category"
        self.category = new_category

    def __str__(self) -> str:
        """String representation of Item"""
        return f"Name: {self.name}, Category: {self.category}"
