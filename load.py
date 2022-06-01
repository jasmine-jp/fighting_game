import pyxel

class Load:
    def __init__(self):
        self.bodynum = 0
        self.bodysize = 16
        self.body = [
            [[i*self.bodysize, 0] for i in range(4)],
            [[i*self.bodysize, self.bodysize] for i in range(3)]
        ]

        pyxel.load('./src/resource.pyxres')