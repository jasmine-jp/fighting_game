import pyxel

from player import Player
from common import window_x

class Command:
    def __init__(self):
        self.phase = 'waiting'
        self.player1 = Player(
            16*3, 10,
            {
                'UP': pyxel.KEY_E,
                'RIGHT': pyxel.KEY_F,
                'LEFT': pyxel.KEY_S,
                'GUARD': pyxel.KEY_X,
                'ATTACK': pyxel.KEY_D
            }
        )
        self.player2 = Player(
            window_x-16*4, window_x-5*10-10,
            {
                'UP': pyxel.KEY_I,
                'RIGHT': pyxel.KEY_L,
                'LEFT': pyxel.KEY_J,
                'GUARD': pyxel.KEY_M,
                'ATTACK': pyxel.KEY_K
            }
        )

    def gamestart(self):
        pyxel.text(82, 55, 'ROBODAN\'s FIGHTING GAME', 0)
        pyxel.text(84, 70, 'please press space key', 0)
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.phase = 'start'
    
    def gameover(self):
        self.phase = 'end'
        pyxel.text(110, 55, 'GAME OVER', 0)
        pyxel.text(84, 70, 'please press space key', 0)
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.__init__()
            self.phase = 'start'
