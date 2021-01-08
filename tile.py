import pygame as pg
import snakeconfig as config

class Tile(pg.Rect):
    
    def __init__(self, x, y, colour):
        super().__init__(x, y, config.tile_size, config.tile_size)
        self.colour = colour
        
    def display(self, screen):
        pg.draw.rect(screen, self.colour, self)
    