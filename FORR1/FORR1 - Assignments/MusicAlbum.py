class MusicAlbum:
    def __init__(
            self, 
            band = "unknown band", 
            title = "unknown", 
            year = "unknown year") -> None:
        self.band = band
        self.title = title
        self.year = year

    def set_album( 
            self,           
            band = "unknown band", 
            title = "unknown", 
            year = "unknown year") -> None:
        self.band = band
        self.title = title
        self.year = year

    def __str__(self):
        return f"Album {self.title} by {self.band}, released in {self.year}."