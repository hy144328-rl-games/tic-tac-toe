#!/usr/bin/env python3

import enum
import numpy as np

class Move(enum.Enum):
    ONE = 1
    TWO = 2
    NONE = 0

class Grid:
    def __init__(self):
        self.state: np.ndarray = np.full((3, 3), Move.NONE)

    def set_player_1(self, player: Player):
        player.turn: Move = Move.ONE

    def set_player_2(self, player: Player):
        player.turn: Move = Move.TWO

    def move(self, turn: Move, row: int, col: int):
        if self.state[row, col] != Move.NONE:
            raise ValueError

        self.state[row, col] = turn

class Player:
    def set_grid(self, grid: Grid):
        self.grid: Grid = grid

    def move(self, row: int, col: int):
        self.grid.move(self.turn, row, col)

if __name__ == "__main__":
    grid = Grid()
    print(grid.state)

