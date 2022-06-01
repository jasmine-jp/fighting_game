import pyxel
import numpy as np

from load import Load
from common import Common

class Player:
    def __init__(self, first_pos, keys):
        self.load = Load()
        self.common = Common()
        self.pos = np.array(first_pos)
        self.max_x, self.max_y = np.array([self.common.window_x, self.common.window_y])-20
        self.keys = keys
    
    def update(self):
        conds = list(map(lambda x: pyxel.btnp(x), self.keys[:2])) + \
            list(map(lambda x: pyxel.btn(x), self.keys[2:]))
        pos_elements = [
            np.array([0, -1]),
            self.common.jump(),
            self.common.rightmove(self.pos[0] != self.max_x),
            self.common.leftmove(self.pos[0] != 0)
        ]
        self.pos += sum(map(lambda c, p: p if c else np.array([0, 0]), conds, pos_elements))
        
    
    def draw(self):
        u, v = self.load.body[0][1]
        bodynum, bodysize = self.load.bodynum, self.load.bodysize
        pyxel.blt(self.pos[0], self.pos[1], bodynum, u, v, bodysize, bodysize, 0)