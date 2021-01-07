import tile

class Segment(tile.Tile):
    
    def __init__(self, x, y):
        colour = (50, 70, 220)
        super().__init__(x, y, colour)