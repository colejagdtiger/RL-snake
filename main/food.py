import tile
import snakeconfig as config

class Food(tile.Tile):
    
    def __init__(self, x, y):
        colour = (50, 220, 70)
        super().__init__(x, y, colour)
        
    def changePosition(self, x, y):
        self.x = x
        self.y = y