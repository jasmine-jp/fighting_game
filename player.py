import pyxel
import numpy as np

from load import Load
from common import Common

class Player:
    def __init__(self, first_pos, keys):
        self.load = Load()
        self.common = Common()
        self.pos = np.array(first_pos)
        self.max_x, self.max_y = np.array([self.common.window_x, self.common.window_y])-self.load.bodysize
        self.keys = keys
        self.max_jumpheight = self.load.bodysize*2
    
    def update(self):
        self.movekey = list(map(lambda x: pyxel.btn(x), self.keys[:3]))
        self.commandkey = list(map(lambda x: pyxel.btn(x), self.keys[3:]))+[True]
        pos_elements = [
            self.common.jump(self.pos[1] > self.max_y-self.max_jumpheight),
            self.common.rightmove(self.pos[0] != self.max_x),
            self.common.leftmove(self.pos[0] != 0),
            self.common.fall(self.pos[1] < self.max_y),
            self.common.guard(),
            self.common.attack()
        ]
        self.diff = sum(map(lambda c, p: p if c else np.array([0, 0]), self.movekey+[True], pos_elements))
        self.pos += self.diff
        
    
    def draw(self):
        row, num = 0, (self.movekey+self.commandkey).index(True)
        u, v = self.load.body[row][num]
        bodynum, bodysize = self.load.bodynum, self.load.bodysize
        pyxel.blt(self.pos[0], self.pos[1], bodynum, u, v, bodysize, bodysize, 0)