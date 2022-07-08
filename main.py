import pyxel

from player import Player
from common import window_x, window_y

pyxel.init(window_x, window_y)

player1 = Player(
    0, 10,
    {
        'UP': pyxel.KEY_E,
        'RIGHT': pyxel.KEY_F,
        'LEFT': pyxel.KEY_S,
        'GUARD': pyxel.KEY_X,
        'ATTACK': pyxel.KEY_D
    }
)

player2 = Player(
    window_x-16, window_x-5*10-10,
    {
        'UP': pyxel.KEY_I,
        'RIGHT': pyxel.KEY_L,
        'LEFT': pyxel.KEY_J,
        'GUARD': pyxel.KEY_M,
        'ATTACK': pyxel.KEY_K
    }
)

def update():
    player1.update(player2)
    player2.update(player1)

def draw():
    pyxel.cls(0)
    pyxel.blt(0, 0, 1, 0, 0, window_x, window_y)
    player1.draw()
    player2.draw()

pyxel.run(update, draw)