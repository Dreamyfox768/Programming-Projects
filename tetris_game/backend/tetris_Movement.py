'''
The shapes of tetris
'''

import turtle as tt
from random import randint
from math import sin , cos , pi


class Tetromino:
    shapes = " I O J L S Z T".split()

    def __init__(self, size=20, screen=None):
        self.size = size
        self.cells = []
        self.pen = tt.RawTurtle(screen or tt.getscreen())

    def draw(self, x, y, color="green"):
        p = self.pen
        p.pu()
        p.goto(x, y)
        p.fillcolor(color)

        p.pd()
        p.begin_fill()
        points = []
        for _ in range(4):
            p.forward(self.size)
            p.right(90)
            x, y = p.pos()
            x, y = round(x), round(y)
            points.append((x, y))
        cell = Cell(self.size, color, self.pen, *points)
        self.cells.append(cell)
        p.end_fill()
        p.getscreen().update()

    def redraw(self):
        self.pen.clear()
        for cell in self.cells:
            cell.draw()
        self.update_screen()

    def left(self, factor=1):
        self.right(-factor)
        self.redraw()

    def right(self, factor=1):
        for cell in self.cells:
            cell.translate_x(factor)
        self.redraw()

    def up(self, factor=1):
        for cell in self.cells:
            cell.translate_y(factor)
        self.redraw()
        ...

    def down(self, factor=1):
        self.up(-factor)
        self.redraw()

    def update_screen(self):
        self.pen.getscreen().update()


class Cell:
    def __init__(self, size, color, pen, *points):
        assert len(points) == 4, f"Number of points must be exactly 4:\n{points}"
        assert points[0] != points[1] != points[2] != points[3], "Points must be unique"
        self.points = points
        self.pen = pen
        self.size = size
        self.color = color

    def draw(self):
        p = self.pen
        p.pu()

        p.goto(self.points[0])
        p.fillcolor(self.color)

        p.pd()
        p.begin_fill()
        for point in self.points:
            p.goto(point)
        p.goto(self.points[0])
        p.end_fill()

    def translate_x(self, factor):
        s = self.size
        self.points = [(x+factor*s, y) for x, y in self.points]

    def translate_y(self, factor):
        s = self.size
        self.points = [(x, y + factor * s) for x, y in self.points]




def draw(x, y):
    global tetro
    r, g, b = [randint(0, 255) for _ in range(3)]
    colr = f"#{r:02x}{g:02x}{b:02x}"
    tetro.draw(x, y, colr)

if __name__ == '__main__':
    tt.tracer(100)
    tetro = Tetromino()
    scr = tt.getscreen()
    scr.onclick(draw)

    scr.onkey(tetro.right, "Right")
    scr.onkey(tetro.left, "Left")
    scr.onkey(tetro.up, "Up")
    scr.onkey(tetro.down, "Down")

    scr.listen()

    tt.mainloop()





