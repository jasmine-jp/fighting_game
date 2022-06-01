import pyxel

class Load:
    def __init__(self):
        self.bodynum = 0
        self.body = [
            [[i*16, 0] for i in range(4)],
            [[i*16, 16] for i in range(3)]
        ]
        pyxel.load('./src/resource.pyxres')