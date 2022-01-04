#!/usr/bin/env python3

import abc
import collections

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

class IntelligentPlayer(Player, abc.ABC):
    @abc.abstractmethod
    def play(self):
        ...

class StraightPlayer(IntelligentPlayer):
    def play(self):
        valid_moves = self.grid.valid_moves
        valid_moves = sorted(
            valid_moves,
            key = lambda x: 3 * x[0] + x[1],
        )
        self.move(*valid_moves[0])

class ProbabilisticPlayer(IntelligentPlayer):
    def __init__(self):
        super().__init__()

        self.table: dict[str, float] = collections.defaultdict(lambda: 0.5)

    def play(self):
        valid_moves = self.grid.valid_moves

        valid_moves_key = sorted(
            valid_moves,
            key = lambda x: 3 * x[0] + x[1],
        )

        valid_moves_value = []
        for move_it in valid_moves_key:
            grid_it = Grid(self.grid)
            grid_it.move(self.turn, *move_it)
            valid_moves_value.append(self.table[repr(grid_it)])

        valid_moves_dict = dict(zip(
            valid_moves_key,
            valid_moves_value,
        ))

        move = max(
            valid_moves_dict,
            key = lambda k: valid_moves_dict[k],
        )

        self.move(*move)

