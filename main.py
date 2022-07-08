import pyxel

from command import Command
from common import window_x, window_y

pyxel.init(window_x, window_y)

command = Command()

def update():
    if command.phase == 'start':
        command.player1.update(command.player2)
        command.player2.update(command.player1)

def draw():
    pyxel.cls(0)
    pyxel.blt(0, 0, 1, 0, 0, window_x, window_y)
    if command.phase == 'waiting':
        command.gamestart()
    elif command.phase == 'start':
        command.player1.draw()
        command.player2.draw()
    if command.player1.hp <= 0 or command.player2.hp <= 0 or command.phase == 'end':
        command.gameover()

pyxel.run(update, draw)