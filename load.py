import pyxel

class Load:
    def __init__(self):
        self.bodynum = 0
        self.bodysize = 16
        self.body = [
            [[i*self.bodysize, 0] for i in range(7)]
        ]

        pyxel.load('./src/resource.pyxres')