import pyxel

from load import Load
from common import *

class Player:
    def __init__(self, first_pos, hp_bar_pos, keyboards):
        self.load = Load()
        self.pos = np.array([first_pos, window_y-bodysize])
        self.max_x, self.max_y = np.array([window_x, window_y])-bodysize
        self.keyboards = keyboards
        self.hp = 5
        self.direct = 'RIGHT' if self.pos[0] < window_x/2 else 'LEFT'
        self.hp_bar_pos = hp_bar_pos
        self.hitbox = np.array([bodysize, -bodysize])+self.pos
        self.upperleft = np.array([self.pos[0], self.hitbox[1]])
        self.lowerright = np.array([self.hitbox[0], self.pos[1]])
    
    def update(self, opponent):
        self.pos += self.load.createKeyMap(self.keyboards)
        self.pos = self.pos.clip([0, window_y-bodysize*2], [window_x-bodysize, window_y-bodysize])
        self.attack(opponent)
    
    def draw(self):
        u, v = self.decideDirect()
        pyxel.blt(self.pos[0], self.pos[1], 0, u, v, bodysize, bodysize, 0)
        pyxel.rect(self.hp_bar_pos, 10, self.hp*10, 10, 11)
    
    def attack(self, opponent):
        self.hitbox = np.array([bodysize, -bodysize])+self.pos
        self.upperleft = np.array([self.pos[0], self.hitbox[1]])
        self.lowerright = np.array([self.hitbox[0], self.pos[1]])
        if np.all(opponent.upperleft <= self.lowerright) and np.all(self.upperleft <= opponent.lowerright):
            if self.load.keyboards_bool['ATTACK']:
                if not opponent.load.keyboards_bool['GUARD']:
                    opponent.hp -= 1
    
    def decideDirect(self):
        s = 'RIGHT' if self.direct == 'LEFT' else 'LEFT'
        if self.load.keyboards_bool[s]:
            self.direct = s

        if self.load.keyboards_bool['GUARD']:
            u, v = self.load.body['GUARD']
        elif self.load.keyboards_bool['ATTACK']:
            u, v = self.load.body['ATTACK'+self.direct][0]
        else:
            if self.load.keyboards_bool['UP']:
                u, v = self.load.body['UP']
            elif self.pos[1] != window_y-bodysize:
                u, v = self.load.body['DOWN']
            else:
                u, v = self.load.body[self.direct]
        return u, v