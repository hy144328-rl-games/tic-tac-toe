#!/usr/bin/env python3

import enum
import numpy as np

class Move(enum.Enum):
    ONE = "x"
    TWO = "o"
    NONE = " "

class Grid:
    no_pad = 1
    col_sep = "|"
    row_sep = "\n" + (5 + 6 * no_pad) * "-" + "\n"

    def __init__(self):
        self.state: np.ndarray = np.full((3, 3), Move.NONE)

    def set_player_1(self, player: "Player"):
        player.turn: Move = Move.ONE

    def set_player_2(self, player: "Player"):
        player.turn: Move = Move.TWO

    def move(self, turn: Move, row: int, col: int):
        if self.state[row, col] != Move.NONE:
            raise ValueError

        self.state[row, col] = turn

    def __repr__(self) -> str:
        return "".join([self.state[i, j].value for i in range(3) for j in range(3)])

    def __str__(self) -> str:
        return "\n" + self.row_sep.join(
            [
                self.col_sep.join(
                    [
                        self.no_pad * " " + self.state[i, j].value + self.no_pad * " "
                        for j in range(3)
                    ]
                )
                for i in range(3)
            ]
        ) + "\n"

    def __getitem__(self, idx: tuple[int, int]) -> Move:
        return self.state[idx[0], idx[1]]

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

class Game:
    def __init__(self):
        self.grid = Grid()
        self.player_1 = Player()
        self.player_2 = Player()

        self.player_1.set_grid(self.grid, Move.ONE)
        self.player_2.set_grid(self.grid, Move.TWO)

    def won_(self, move: Move) -> bool:
        # Rows.
        for i in range(3):
            if all(self.grid[i, j] == move for j in range(3)):
                return True

        # Columns.
        for j in range(3):
            if all(self.grid[i, j] == move for i in range(3)):
                return True

        # Diagonals.
        if all(self.grid[i, i] == move for i in range(3)):
            return True
        if all(self.grid[i, 2 - i] == move for i in range(3)):
            return True

        return False

    @property
    def won_1(self) -> bool:
        return self.won_(Move.ONE)

    @property
    def won_2(self) -> bool:
        return self.won_(Move.TWO)

    @property
    def won(self) -> bool:
        return self.won_1 or self.won_2

if __name__ == "__main__":
    game = Game()
    print(game.grid)
    print(game.won)

    for i in range(3):
        game.player_1.move(i, i)
    print(game.grid)
    print(game.won)

