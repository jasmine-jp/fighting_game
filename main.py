import pyxel
from player import Player

from common import Common

common = Common()
pyxel.init(common.window_x, common.window_y)

player1 = Player(
    [0, common.window_y-20],
    [
        pyxel.KEY_E,
        pyxel.KEY_X,
        pyxel.KEY_F,
        pyxel.KEY_S
    ]
)

player2 = Player(
    [common.window_x-20, common.window_y-20],
    [
        pyxel.KEY_I,
        pyxel.KEY_M,
        pyxel.KEY_L,
        pyxel.KEY_J
    ]
)

def update():
    player1.update()
    player2.update()

def draw():
    pyxel.cls(0)
    player1.draw()
    player2.draw()

pyxel.run(update, draw)