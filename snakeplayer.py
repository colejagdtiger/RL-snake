import segment as seg
import snakeconfig as config

class Player(object):
    
    def __init__(self):
        self.dir_x = 1
        self.dir_y = 0
        self.length = 4
        self.segments = list()
    

    def initializePlayer(self, start_x, start_y):
        self.length = 4
        self.segments.clear()
        start_x = config.screen_width / 2
        start_y = config.screen_height / 2
        for i in range(self.length):
            self.segments.append(seg.Segment(start_x - config.tile_size * i, start_y))
    
    
    def step(self):
        for i in range(self.length - 1, 0, -1):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y
            
        self.segments[0].x += self.dir_x * config.tile_size
        self.segments[0].y += self.dir_y * config.tile_size
            
    
    def moveUp(self):
        self.dir_x = 0
        self.dir_y = -1
    
    def moveDown(self):
        self.dir_x = 0
        self.dir_y = 1
        
    def moveRight(self):
        self.dir_x = 1
        self.dir_y = 0
    
    def moveLeft(self):
        self.dir_x = -1
        self.dir_y = 0
    
    def display(self, screen):
        for sg in self.segments:
            sg.display(screen)
        
    def addSegment(self):
        x = self.segments[self.length - 1].x
        y = self.segments[self.length - 1].y
        self.segments.append(seg.Segment(x, y))
        self.length += 1

