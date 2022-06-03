import pyxel

from player import Player
from common import Common

common = Common()
pyxel.init(common.window_x, common.window_y)

player1 = Player(
    0, 10,
    [
        pyxel.KEY_E,
        pyxel.KEY_F,
        pyxel.KEY_S,
        pyxel.KEY_X,
        pyxel.KEY_D
    ]
)

player2 = Player(
    common.window_x-16, common.window_x-5*10-10,
    [
        pyxel.KEY_I,
        pyxel.KEY_L,
        pyxel.KEY_J,
        pyxel.KEY_M,
        pyxel.KEY_K
    ]
)

def update():
    player1.update(player2)
    player2.update(player1)

def draw():
    pyxel.cls(0)
    player1.draw()
    player2.draw()

pyxel.run(update, draw)