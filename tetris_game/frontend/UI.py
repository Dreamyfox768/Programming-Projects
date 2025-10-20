import turtle as tt
from random import choice, randint as r
from itertools import cycle
from typing import Optional

from tetrominoes import I, J, L, S, Z, O, T
from tetro_base import Tetromino, Cell

SHAPE_CLASSES = cycle((O, I, J, L, S, Z, T))


class World(Tetromino):
    def __init__(self, size=20, screen=None):
        super().__init__(size, screen)
        self.screen = self.pen.getscreen()
        self.stack = None
        self.tetro = None
        self.init_screen()

    def init_screen(self, **settings):
        s = self.size
        x1, y1, xu, yu = -5, 0, 15, 20
        self.screen.setworldcoordinates(x1*s, y1*s, xu*s, yu*s)
        self.screen.bgcolor("black")
        self.draw(0, s, "gray")
        self.stack = Stack(self)
        self.spawn()

    def draw(self, x, y, color=""):
        for row in range(20):
            for col in range(10):
                super().draw(x, y, color)
                x += self.size
            x, y = 0, y + self.size
        self.screen.update()

    def spawn(self):
        self.tetro = next(SHAPE_CLASSES)(self.size, self.screen)
        x, y = 4 * self.size, 22 * self.size
        self.tetro.draw(x, y)
        self.screen.update()

    def move(self, instr="down"):
        # ✅ FIX: Check top row (row 19) for game over
        if any(self.stack.state_matrix[19]):
            self.game_over()
            return

        temp_cells = []
        for cell in self.tetro.cells:
            new_cell = Cell(self.size, cell.color, cell.pen, *cell.points)
            if instr == "down":
                new_cell.translate_y(-1)
            elif instr == "left":
                new_cell.translate_x(-1)
            elif instr == "right":
                new_cell.translate_x(1)
            elif instr == "rotate":
                new_cell = new_cell * self.tetro.rot_center
            temp_cells.append(new_cell)

        if self.stack.ok_move(temp_cells):
            getattr(self.tetro, instr)()
        else:
            if instr == "down":
                self.stack.absorb(*self.tetro.cells, tetro=self.tetro)
                self.stack.request_tetro()

        self.tetro.draw_bounds()

    def game_over(self):
        # Fill the grid with a single color (e.g., gray)
        x, y = 0, self.size
        for row in range(20):
            for col in range(10):
                color = "gray"  # Change this to whatever color you want for the game over grid
                super().draw(x, y, color)
                x += self.size
            x, y = 0, y + self.size

        # Display a larger "Game Over!" message in the center of the grid
        self.pen.penup()
        self.pen.goto(5 * self.size, 10 * self.size)  # Roughly center of the grid
        self.pen.color("white")  # You can change this to any color you prefer
        self.pen.write("GAME OVER!", align="center", font=("Arial", 40, "bold"))  # Larger font size

        self.screen.update()
        print("Game Over!")


class Stack(Tetromino):
    def __init__(self, world: World):
        super().__init__(world.size, world.screen)
        self.state_matrix = None
        self.world = world
        self.init_state_matrix()

    def init_state_matrix(self):
        self.state_matrix = [[0 for _ in range(10)] for _ in range(20)]

    def ok_move(self, cells: list[Cell], move="down") -> bool:
        for cell in cells:
            xl, yl, xh, yh = cell.get_bounds()
            if xl < 0 or xh > self.size * 10 or yl < 0:
                return False
            for my_cell in self.cells:
                if cell == my_cell:
                    return False
        return True

    def absorb(self, *cells, tetro: Tetromino = None):
        for cell in cells:
            xl, yl, _, _ = cell.get_bounds()
            row = int(yl // self.size)
            col = int(xl // self.size)
            if 0 <= row < 20 and 0 <= col < 10:
                self.state_matrix[row][col] = 1
                self.cells.append(cell)
        self.redraw()

    def request_tetro(self):
        self.world.spawn()


if __name__ == '__main__':
    tt.ht()
    tt.tracer(100)
    w = World()
    scr = tt.getscreen()

    scr.onclick(lambda x, y: [w.tetro.clear(), w.spawn()])
    scr.onkey(lambda: w.move("left"), "Left")
    scr.onkey(lambda: w.move("right"), "Right")
    scr.onkey(lambda: w.move("down"), "Down")
    scr.onkey(lambda: w.move("rotate"), "Up")
    scr.onkey(lambda: [w.move("down") for _ in range(10)], "space")
    scr.listen()

    for line in w.stack.state_matrix:
        print(line)

    tt.done()
