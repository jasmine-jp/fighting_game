import pyxel
import numpy as np

from load import Load
from common import Common

class Player:
    def __init__(self, first_pos, hp_bar_pos, keys):
        self.load = Load()
        self.common = Common()
        self.pos = np.array([first_pos, self.common.window_y-self.load.bodysize])
        self.max_x, self.max_y = np.array([self.common.window_x, self.common.window_y])-self.load.bodysize
        self.keys = keys
        self.max_jumpheight = self.load.bodysize*2
        self.hp = 5
        self.hp_bar_pos = hp_bar_pos
        self.hitbox = np.array([self.load.bodysize, -self.load.bodysize])+self.pos
        self.upperleft = np.array([self.pos[0], self.hitbox[1]])
        self.lowerright = np.array([self.hitbox[0], self.pos[1]])
    
    def update(self, opponent):
        self.movekey = list(map(lambda x: pyxel.btn(x), self.keys[:3]))+[self.pos[1] < self.max_y]
        self.commandkey = [pyxel.btn(self.keys[3]), pyxel.btnp(self.keys[4]), True]
        pos_elements = [
            self.common.jump(self.pos[1] > self.max_y-self.max_jumpheight),
            self.common.rightmove(self.pos[0] != self.max_x),
            self.common.leftmove(self.pos[0] != 0),
            self.common.fall(),
            self.common.guard(),
            self.common.attack()
        ]
        self.diff = sum(map(lambda c, p: p if c else np.array([0, 0]), self.movekey, pos_elements))
        self.pos += self.diff
        self.attack(opponent)
    
    def draw(self):
        row, num = 0, (self.movekey+self.commandkey).index(True)
        u, v = self.load.body[row][num]
        bodynum, bodysize = self.load.bodynum, self.load.bodysize
        pyxel.blt(self.pos[0], self.pos[1], bodynum, u, v, bodysize, bodysize, 0)
        pyxel.rect(self.hp_bar_pos, 10, self.hp*10, 10, 11)
    
    def attack(self, opponent):
        self.hitbox = np.array([self.load.bodysize, -self.load.bodysize])+self.pos
        self.upperleft = np.array([self.pos[0], self.hitbox[1]])
        self.lowerright = np.array([self.hitbox[0], self.pos[1]])
        if np.all(opponent.upperleft <= self.lowerright) and np.all(self.upperleft <= opponent.lowerright):
            if self.commandkey[1]:
                if not opponent.commandkey[0]:
                    opponent.hp -= 1