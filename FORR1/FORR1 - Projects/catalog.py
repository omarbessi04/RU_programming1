class Catalog:
    """Catalog that can be filled with items"""
    def __init__(self, name: str) -> None:
        """Initialize a catalog with a given name"""
        self.name = name
        self.list_of_items = []

    def set_name(self, new_name: str) -> None:
        """Change/set name of the catalog"""
        self.name = new_name

    def add(self, new_item: str) -> None:
        """Add a new item to the catalog"""
        self.list_of_items.append(new_item)

    def remove(self, bad_film: str) -> None:
        """Remove an item from the catalog"""
        self.list_of_items.remove(bad_film)

    def clear(self) -> None:
        """Empties the catalog"""
        self.list_of_items = []

    def __str__(self) -> str:
        """String representation of catalog"""
        output = f"Catalog {self.name}:"
        # if the catalog is empty then only the \
        # name of the catalog is printed
        for film in self.list_of_items:
            output += "\n\t" + str(film)
        
        return output
