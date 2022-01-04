#!/usr/bin/env python3

from . import Move
from .grid import Grid

class Player:
    def __init__(self):
        self.turn = None

    def set_grid(self, grid: Grid, turn: Move = Move.NONE):
        self.grid: Grid = grid

        if turn == Move.ONE:
            self.grid.set_player_1(self)
        elif turn == Move.TWO:
            self.grid.set_player_2(self)

    def move(self, row: int, col: int):
        self.grid.move(self.turn, row, col)

    @property
    def is_winner(self) -> bool:
        return self.grid.in_line(self.turn)

