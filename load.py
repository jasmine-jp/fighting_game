import pyxel

from common import *

class Load:
    def __init__(self):
        self.body = {
            'UP': [0, 0],
            'RIGHT': [bodysize, 0],
            'LEFT': [bodysize*2, 0],
            'DOWN': [bodysize*3, 0],
            'GUARD': [bodysize*4, 0],
            'ATTACKLEFT': [[bodysize*i, 0] for i in range(5, 8)],
            'ATTACKRIGHT': [[bodysize*i, 0] for i in range(8, 11)]
        }

        pyxel.load('./src/resource.pyxres')
    
    def createKeyMap(self, keyboards):
        o = np.array([0, 0])
        self.keyboards_bool = {
            'UP': pyxel.btn(keyboards['UP']),
            'RIGHT': pyxel.btn(keyboards['RIGHT']),
            'LEFT': pyxel.btn(keyboards['LEFT']),
            'GUARD': pyxel.btn(keyboards['GUARD']),
            'ATTACK': pyxel.btnp(keyboards['ATTACK'])
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