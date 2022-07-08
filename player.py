import pyxel

from load import Load
from common import *

class Player:
    def __init__(self, first_pos, hp_bar_pos, keyboards):
        self.load = Load(first_pos)
        self.pos = np.array([first_pos, window_y-bodysize])
        self.keyboards = keyboards
        self.hp = 5
        self.hp_bar_pos = hp_bar_pos
        self.hitbox = np.array([bodysize, -bodysize])+self.pos
        self.upperleft = np.array([self.pos[0], self.hitbox[1]])
        self.lowerright = np.array([self.hitbox[0], self.pos[1]])
    
    def update(self, opponent):
        self.pos += self.load.createKeyMap(self.keyboards)
        self.attack(opponent)
        self.pos = self.pos.clip([0, window_y-bodysize*4], [window_x-bodysize, window_y-bodysize])
    
    def draw(self):
        u, v = self.load.decideBody(self.pos)
        pyxel.blt(self.pos[0], self.pos[1], 0, u, v, bodysize, bodysize, 0)
        pyxel.rect(self.hp_bar_pos, 10, self.hp*10, 10, 11)
    
    def attack(self, opponent):
        self.hitbox = np.array([bodysize, -bodysize])+self.pos
        self.upperleft = np.array([self.pos[0], self.hitbox[1]])
        self.lowerright = np.array([self.hitbox[0], self.pos[1]])
        if np.all(opponent.upperleft <= self.lowerright) and np.all(self.upperleft <= opponent.lowerright):
            if self.load.keyboards_bool['ATTACK'] and not opponent.load.keyboards_bool['GUARD']:
                opponent.hp -= 1