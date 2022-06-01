import pyxel
import numpy as np

class Player:
    def __init__(self, max_pos, first_pos1, first_pos2, keys1, keys2):
        self.pos1 = np.array(first_pos1)
        self.pos2 = np.array(first_pos2)
        self.max_x, self.max_y = max_pos
        self.keys1 = keys1
        self.keys2 = keys2
    
    def update(self):
        conds1 = map(lambda x: pyxel.btnp(x), self.keys1)
        conds2 = map(lambda x: pyxel.btnp(x), self.keys2)
        pos_elements = [
            np.array([0, -1]),
            np.array([0, 1]),
            np.array([-1, 0]),
            np.array([1, 0])
        ]

        for cond, pos_element in zip(conds1, pos_elements):
            if cond:
                self.pos1 += pos_element
        for cond, pos_element in zip(conds2, pos_elements):
            if cond:
                self.pos2 += pos_element
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.pos1[0], self.pos1[1], 20, 20, 11)
        pyxel.rect(self.pos2[0], self.pos2[1], 20, 20, 11)