import turtle as tt
from random import choice, randint as r
from itertools import cycle
from typing import Optional

from tetrominoes import I, J, L, S, Z, O, T
from tetro_base import Tetromino, Cell

SHAPE_CLASSES = cycle((O, I, J, L, S, Z, T))


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
    highest row in stack is 19
    """
    def __init__(self, size=20, screen=None):
        super().__init__(size, screen)
        self.screen = self.pen.getscreen()
        self.stack = None  # Initially, the stack is None
        self.tetro = None  # Initially, there is no active tetro
        self.init_screen()

    def init_screen(self, **settings):
        s = self.size
        x1, y1, xu, yu = -5, 0, 15, 20
        self.screen.setworldcoordinates(x1*s, y1*s, xu*s, yu*s)
        self.screen.bgcolor("black")
        self.draw(0, s, "green")
        self.stack = Stack(self)  # Pass the World object (self) to Stack
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
        """Create a new active tetro"""
        self.tetro = next(SHAPE_CLASSES)(self.size, self.screen)
        x, y = 4 * self.size, 22 * self.size
        self.tetro.draw(x, y)
        self.screen.update()



class Stack(Tetromino):
    def __init__(self, world: World):
        super().__init__(world.size, world.screen)  # Initialize base Tetromino class
        self.state_matrix = None
        self.world = world
        self.init_state_matrix()

    def init_state_matrix(self):
        """Initializes stack state i.e. 20x10 table with 0's"""
        self.state_matrix = [[0 for _ in range(10)] for _ in range(20)]  # 20 rows, 10 columns


    def request_tetro(self):
        """Invoke spawn on world after a tetro is absorbed"""
        if any(cell > 19 for cell in self.state_matrix):  # Game over condition
            self.world.game_over()
        else:
            self.world.spawn()


if __name__ == '__main__':
    tt.ht()
    tt.tracer(100)
    w = World()
    scr = tt.getscreen()
    scr.onclick(lambda x, y: [w.tetro.clear(), w.spawn()])

    for line in w.stack.state_matrix:
        print(line)

    tt.done()
