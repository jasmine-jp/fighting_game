import pyxel
from player import Player

window_x, window_y = 160, 120
pyxel.init(window_x, window_y)

player = Player(
    (window_x, window_y),
    [0, 0],
    [window_x-20, 0],
    [
        pyxel.KEY_E,
        pyxel.KEY_X,
        pyxel.KEY_S,
        pyxel.KEY_F
    ],
    [
        pyxel.KEY_I,
        pyxel.KEY_M,
        pyxel.KEY_J,
        pyxel.KEY_L
    ]
)

pyxel.run(player.update, player.draw)