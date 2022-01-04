#!/usr/bin/env python3

import numpy as np

from . import Move

class Grid:
    no_pad = 1
    col_sep = "|"
    row_sep = "\n" + (5 + 6 * no_pad) * "-" + "\n"

    def __init__(self, grid: "Grid"=None):
        if grid:
            self.state: np.ndarray = grid.state.copy()
        else:
            self.state: np.ndarray = np.full((3, 3), Move.NONE)

    def set_player_1(self, player: "Player"):
        player.turn: Move = Move.ONE

    def set_player_2(self, player: "Player"):
        player.turn: Move = Move.TWO

    def move(self, turn: Move, row: int, col: int):
        if self.state[row, col] != Move.NONE:
            raise ValueError

        self.state[row, col] = turn

    def in_line(self, turn: Move) -> bool:
        # Rows.
        for i in range(3):
            if all(self.state[i, j] == turn for j in range(3)):
                return True

        # Columns.
        for j in range(3):
            if all(self.state[i, j] == turn for i in range(3)):
                return True

        # Diagonals.
        if all(self.state[i, i] == turn for i in range(3)):
            return True
        if all(self.state[i, 2 - i] == turn for i in range(3)):
            return True

        return False

    @property
    def valid_moves(self) -> set[tuple[int, int]]:
        return set(
            (i, j)
            for i in range(3)
            for j in range(3)
            if self.state[i, j] == Move.NONE
        )

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

