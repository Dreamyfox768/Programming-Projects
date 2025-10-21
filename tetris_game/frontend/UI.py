import turtle as tt
from random import choice, randint as r
from itertools import cycle
from typing import Optional

from tetrominoes import I, J, L, S, Z, O, T
from tetro_base import Tetromino, Cell

SHAPE_CLASSES = cycle((I, J, L, S, Z, O, T))


class World(Tetromino):
    """Represents the tetris world
    defined by a grid of 20x10 (visible) cells
    Components:
        - tetro: the currently active Tetromino
        - stack:  the stack of past Tetromino blocks
    Tetro moves:
        - down -> key Down: Drops active tetro by 1 cell
        - Left -> key Left: Shifts active tetro right by 1 cell
        - right -> key Right: Shifts active tetro left by 1 cell
        - rotate -> key Up: Rotates active tetro 90 clockwise
        - hard_drop -> key space: Drops active tetro till stop at stack or bottom

    A new tetro is spawned in cell 22 (i.e. out of visible grid)
    An active tetro is dropped by one cell each play cycle until
    it's at the bottom of the world or
    its bottom row of cells collides with the stack.
    An active tetro is absorbed by the Stack at this point and a new tetro
    is spawned.
    The game is over once the stack hits the world ceiling i.e.
    highest row in stack is 19"""

    def __init__(self, size=20, screen=None):
        super().__init__(size, screen)
        self.screen = self.pen.getscreen()
        self.stack = Stack(self)  # Pass the World object (self) to Stack
        self.tetro = None  # Initially, there is no active tetro
        self.init_screen()

    def init_screen(self, **settings):
        s = self.size
        x1, y1, xu, yu = -5, 0, 15, 20
        self.screen.setworldcoordinates(x1 * s, y1 * s, xu * s, yu * s)
        self.screen.bgcolor("#C6DEF1")
        self.draw(0, s, "#FAEDCB")
        self.spawn()

    def draw(self, x, y, color=""):
        """Draws the world, a 20x10 grid"""
        for row in range(20):
            for col in range(10):
                super().draw(x, y, color)
                x += self.size
            x, y = 0, y + self.size
        self.screen.update()

    def spawn(self):
        """create a new/active tetro"""
        self.tetro = next(SHAPE_CLASSES)(self.size, self.screen)
        x, y = 4 * self.size, 22 * self.size
        self.tetro.draw(x, y)
        self.screen.update()

    def get_tetro(self):
        """TODO"""
        ...

    def move(self, instr="down"):
        """If game over (check state of stack) invoke game_over
        Otherwise check if move is acceptable (i.e. invoke ok_move on stack)
         and invoke move on tetro if move is ok."""
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

        # Check if the move is valid
        if self.stack.ok_move(temp_cells, self.tetro):
            getattr(self.tetro, instr)()  # Call move method of Tetromino
        else:
            if instr == "down":
                # Absorb tetromino into stack if it can't move further
                self.stack.absorb(*self.tetro.cells, tetro=self.tetro)
                self.stack.request_tetro()

        self.tetro.draw_bounds()

    def hard_drop(self):
        """TODO: While ok drop current tetro by a cell """
        ...

    def play(self):
        """TODO"""
        ...

    def game_over(self):
        """Simplest game over graphic I could think of
        randomly reset cell colors to yellow or green and redraw"""
        self.pen.penup()
        self.pen.goto(5 * self.size, 10 * self.size)
        self.pen.color("white")
        self.pen.write("GAME OVER!", align="center", font=("Arial", 40, "bold"))

        self.screen.update()
        print("Game Over!")

    def update_score(self, lines):
        """TODO"""
        ...


class Stack(Tetromino):
    def __init__(self, world: World):
        super().__init__(world.size, world.screen)  # Initialize base Tetromino class
        self.state_matrix = None
        self.world = world
        self.cells = []
        self.init_state_matrix()

    def init_state_matrix(self):
        """Initializes stack state i.e.  20x10 table with 0's """
        self.state_matrix = [[0 for _ in range(10)] for _ in range(20)]  # 20 rows, 10 columns


    def ok_move(self, cells: list[Cell], tetro:Tetromino, move="down") -> bool:
        """Given a Tetromino and intended move returns a boolean
        indicating whether move is OK.
        NB:
            - Cannot move outside world boundaries
            - Cannot overlap with the stack
            - Once the base of a tetromino touches the stack is absorbed
        Hint (checking overlap with stack):
            Use check_overlap, and dunder methods
            that return cells for proposed move from tetro
              Ex. for a right move check_overlap(*[c >> 1 for c in tetro.cells])
            without drawing or affecting the state of the world"""
        for cell in cells:
            xl, yl, xh, yh = cell.get_bounds()
            if xl < 0 or xh > self.size * 10 or yl < 0:
                return False
            for my_cell in self.cells:
                mx, my, _, _ = my_cell.get_bounds()
                if xl == mx and yl == my:  # Compare coordinates instead of objects
                    return False
        return True

    def absorb(self, *cells, tetro:Tetromino=None):
        for cell in cells:
            xl, yl, _, _ = cell.get_bounds()
            row = int(yl // self.size)
            col = int(xl // self.size)
            if 0 <= row < 20 and 0 <= col < 10:
                self.state_matrix[row][col] = 1
                self.cells.append(cell)
        self.redraw()


    def request_tetro(self):
        """Invokes spawn on world after a tetro is absorbed
        Sets game_over property to zero if height is greater than 19"""
        self.world.spawn()

    def clear_line(self, line_num):
        """TODO"""

    def rearrange(self):
        """Rearrange stack after absorbing a tetro
            - Find row index of full lines i.e. all cells no zeros
            - Clear out full lines
            - Drop lines above each deleted line (starting from the top)
        """
        """TODO"""



if __name__ == '__main__':
    tt.ht()
    tt.tracer(100)
    w = World(1)

    screen = tt.getscreen()
    keys = "Left Right Down Up space".split()
    screen.onclick(lambda x, y: w.play())
    screen.onkey(lambda: w.move("left"), "Left")
    screen.onkey(lambda: w.move("right"), "Right")
    screen.onkey(lambda: w.move("down"), "Down")
    screen.onkey(lambda: w.move("rotate"), "Up")

    presses_moves = dict(zip(keys, [k.lower() for k in keys]))
    presses_moves["Up"] = "rotate"
    for kp, mv in presses_moves.items():
        screen.onkey(lambda move=mv: w.move(move), kp)
    screen.listen()
    tt.listen()
    tt.mainloop()
