from itertools import count
import pyxel

from common import *

class Load:
    def __init__(self, first_pos):
        self.direct = 'RIGHT' if first_pos < window_x/2 else 'LEFT'
        self.body = {
            'UP': [0, 0],
            'RIGHT': [bodysize, 0],
            'LEFT': [bodysize*2, 0],
            'DOWN': [bodysize*3, 0],
            'GUARD': [bodysize*4, 0],
            'ATTACKLEFT': [[bodysize*i, 0] for i in range(5, 8)],
            'ATTACKRIGHT': [[bodysize*i, 0] for i in range(8, 11)]
        }
        self.count = -1
        pyxel.load('./src/resource.pyxres')
    
    def createKeyMap(self, keyboards):
        o = np.array([0, 0])
        self.keyboards_bool = {
            'UP': pyxel.btn(keyboards['UP']),
            'RIGHT': pyxel.btn(keyboards['RIGHT']),
            'LEFT': pyxel.btn(keyboards['LEFT']),
            'GUARD': pyxel.btn(keyboards['GUARD']),
            'ATTACK': pyxel.btnp(keyboards['ATTACK']) and not pyxel.btn(keyboards['GUARD'])
        }
        move = {
            'UP': jump(),
            'RIGHT': rightmove(),
            'LEFT': leftmove()
        }
        for key in move.keys():
            if self.keyboards_bool[key]:
                o += move[key]
        o += fall()
        return o
    
    def decideBody(self, pos):
        s = 'RIGHT' if self.direct == 'LEFT' else 'LEFT'
        if self.keyboards_bool[s]:
            self.direct = s

        if self.keyboards_bool['GUARD']:
            return self.body['GUARD']
        elif self.keyboards_bool['ATTACK']:
            self.count = 0
        
        if -1 < self.count < len(self.body['ATTACKLEFT']):
            u, v = self.body['ATTACK'+self.direct][self.count]
            self.count += 1
            if self.count == 3:
                self.count = -1
        else:
            if self.keyboards_bool['UP']:
                u, v = self.body['UP']
            elif pos[1] != window_y-bodysize:
                u, v = self.body['DOWN']
            else:
                u, v = self.body[self.direct]
        return u, v