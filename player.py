import pyxel
import numpy as np

from load import Load

class Player:
    def __init__(self, max_pos, first_pos, keys):
        load = Load()
        self.pos = np.array(first_pos)
        self.max_x, self.max_y = max_pos
        self.keys = keys
        self.bodynum = load.bodynum
        self.body = load.body
    
    def update(self):
        conds = list(map(lambda x: pyxel.btnp(x), self.keys[:2])) + \
            list(map(lambda x: pyxel.btn(x), self.keys[2:]))
        pos_elements = [
            np.array([0, -1]),
            np.array([0, 1]),
            np.array([1, 0]),
            np.array([-1, 0])
        ]

        for i, (cond, pos_element) in enumerate(zip(conds, pos_elements)):
            if cond:
                if i == 2 and self.pos[0] == 0:
                    continue
                elif i == 3 and self.pos[0] == self.max_x:
                    continue
                else:
                    self.pos += pos_element
    
    def draw(self):
        u, v = self.body[0][1]
        pyxel.blt(self.pos[0], self.pos[1], self.bodynum, u, v, 16, 16, 0)