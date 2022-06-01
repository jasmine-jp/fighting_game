import pyxel
import numpy as np

class Player:
    def __init__(self, max_pos, first_pos, keys):
        self.pos = np.array(first_pos)
        self.max_x, self.max_y = max_pos
        self.keys = keys
    
    def update(self):
        conds = map(lambda x: pyxel.btnp(x), self.keys)
        pos_elements = [
            np.array([0, -1]),
            np.array([0, 1]),
            np.array([-1, 0]),
            np.array([1, 0])
        ]

        for cond, pos_element in zip(conds, pos_elements):
            if cond:
                self.pos += pos_element
    
    def draw(self):
        pyxel.rect(self.pos[0], self.pos[1], 20, 20, 11)