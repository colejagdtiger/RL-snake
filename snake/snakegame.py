import pygame as pg
import food
import snakeplayer as player
import snakeconfig as config
import numpy as np
import time

def getStartPositions():
    x = round(config.screen_width / 2)
    y = round(config.screen_height / 2)
        
    player_x = x
    player_y = y
        
    food_x = min(x + config.tile_size * 4, config.screen_width - config.tile_size)
    food_y = y
        
    return [player_x, player_y, food_x, food_y]   

class SnakeGame(object):
    
    def __init__(self):
        self.running = True
        self.player = player.Player()
        self.food = food.Food(config.tile_size * -1, config.tile_size * -1)
        self.screen = None
        x_size = int(config.screen_width / config.tile_size)
        y_size = int(config.screen_height / config.tile_size)
        
        self.empty = np.full((x_size, y_size), True, dtype=bool)
        
    
    def initializeGame(self):
        pg.init()
        
        self.newGame()
        self.screen = pg.display.set_mode((config.screen_width, config.screen_height))


    def updateEmpty(self, index, val):
        i = int(self.player.segments[index].x / config.tile_size)
        j = int(self.player.segments[index].y / config.tile_size)
        try:
            self.empty[i, j] = val
        except:
            self.running = False
        
    
    def newGame(self):
        player_x, player_y, food_x, food_y = getStartPositions()
        
        self.player.initializePlayer(player_x, player_y)
        self.food.changePosition(food_x, food_y)
        
        for ind in range(self.player.length):
            self.updateEmpty(ind, False)
            
        self.running = True
      
    
    def update(self):
        self.updateEmpty(self.player.length - 1, True)
        self.player.step()
        self.updateEmpty(0, False)

        if (self.checkFood()):
            self.player.addSegment()
            self.moveFood()
        if (self.checkCollision()):
            self.running = False
            
        self.display()
    
    
    def execute(self):
        count = 0
        while self.running:
            time.sleep(0.05)
            pg.event.pump()
            pressed = pg.key.get_pressed()
            if (pressed[pg.K_w]):
                self.player.moveUp()
            elif (pressed[pg.K_s]):
                self.player.moveDown()
            elif (pressed[pg.K_d]):
                self.player.moveRight()
            elif (pressed[pg.K_a]):
                self.player.moveLeft()
            elif (pressed[pg.K_ESCAPE]):
                self.running = False
            
            count += 1
            if (count == 6):
                self.update()
                count = 0
            
        pg.quit()
    
    
    def display(self):
        self.screen.fill((0, 0, 0))
        self.food.display(self.screen)
        self.player.display(self.screen)
        pg.display.flip()
        
    
    def checkFood(self):
        food_x = self.food.x
        food_y = self.food.y
        player_x = self.player.segments[0].x
        player_y = self.player.segments[0].y
        if (player_x == food_x and player_y == food_y):
            return True
        return False
    
    
    def checkCollision(self):
        x = self.player.segments[0].x
        y = self.player.segments[0].y
        
        for segment in self.player.segments[1:]:
            if (segment.x == x and segment.y == y):
                return True
            
        if (x + config.tile_size > config.screen_width or x < 0
            or y + config.tile_size > config.screen_height or y < 0):
            return True

        return False
    
    
    def moveFood(self):
        try:
            spaces = np.where(self.empty)
            ind = np.random.randint(len(spaces[0]))
            
            x = spaces[0][ind] * config.tile_size
            y = spaces[1][ind] * config.tile_size
                    
            self.food.changePosition(x, y)
        except:
            """if there is no place for food to be placed, then an exception
            will occur and we will exit the game"""
            self.running = False
        
        