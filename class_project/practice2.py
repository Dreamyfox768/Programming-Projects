import turtle as tt
from random import randint as r
from itertools import cycle

class Tetromino:
    shapes = " I O J L S Z T".split()

    def __init__(self, size=20):
        self.size = size

    def draw(self, x, y, color="green"):
        tt.pu()
        tt.goto(x, y)
        tt.fillcolor(color)

        tt.pd()
        tt.begin_fill()
        for _ in range(4):
            tt.fd(self.size)
            tt.right(90)
        tt.end_fill()
        tt.update()


class O(Tetromino):
    def draw(self, x, y, color="green"):
        for i in range(2):
            for j in range(2):
                super().draw(x, y, color="yellow")
                x += self.size
            y -= self.size
            x -= self.size * 2


class Z(Tetromino):
    def draw(self, x, y, color="green"):
        for i in range(2):
            for j in range(2):
                super().draw(x, y, color="red")
                x += self.size
            y -= self.size
            x -= self.size


class I(Tetromino):
    def draw(self, x, y, color="green"):
        for i in range(1):
            for j in range(4):
                super().draw(x, y, color="#ADD8E6")
                x += self.size
            y += self.size
            x -= self.size


class S(Tetromino):
    def draw(self, x, y, color="green"):
        for i in range(2):
            for j in range(2):
                super().draw(x, y, color="green")
                x -= self.size
            y -= self.size
            x += self.size


class T(Tetromino):
    def draw(self, x, y, color="green"):
        super().draw(x, y, color="#F535AA")
        super().draw(x + self.size, y, color="#F535AA")
        super().draw(x + 2 * self.size, y, color="#F535AA")
        super().draw(x + self.size, y - self.size, color="#F535AA")


class L(Tetromino):
    def draw(self, x, y, color="green"):
        super().draw(x, y, color="orange")
        super().draw(x, y - self.size, color="orange")
        super().draw(x, y - 2 * self.size, color="orange")
        super().draw(x + self.size, y - 2 * self.size, color="orange")


class J(Tetromino):
    def draw(self, x, y, color="green"):
        super().draw(x, y, color="#00008B")
        super().draw(x, y - self.size, color="#00008B")
        super().draw(x, y - 2 * self.size, color="#00008B")
        super().draw(x - self.size, y - 2 * self.size, color="#00008B")


def main(x, y):
    tetro = next(shapes)()
    tetro.draw(x, y, f"#{r(0, 255):02x}{r(0, 255):02x}{r(0, 255):02x}")


if __name__ == '__main__':
    tt.tracer(100)

    shapes = cycle([O, Z, I, S, T, L, J])  # No need for `global` here
    screen = tt.getscreen()
    screen.onclick(main)

    tt.mainloop()
