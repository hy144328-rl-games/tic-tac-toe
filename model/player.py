#!/usr/bin/env python3

import abc
import collections
import random

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

    @property
    def is_loser(self) -> bool:
        return self.grid.in_line(self.other_turn)

    def reset(self):
        ...

class IntelligentPlayer(Player, abc.ABC):
    @property
    def valid_moves(self) -> list[tuple[int, int]]:
        valid_moves = self.grid.valid_moves
        valid_moves = sorted(
            valid_moves,
            key = lambda x: 3 * x[0] + x[1],
        )
        return valid_moves

    @abc.abstractmethod
    def pick_move(
        self,
        moves: list[tuple[int, int]],
    ) -> tuple[int, int]:
        ...

    def play(self):
        valid_moves = self.valid_moves
        move = self.pick_move(valid_moves)
        self.move(*move)

class StraightPlayer(IntelligentPlayer):
    def pick_move(
        self,
        moves: list[tuple[int, int]],
    ) -> tuple[int, int]:
        return moves[0]

class RewardTable:
    def __init__(self):
        self.table: dict[str, float] = collections.defaultdict(lambda: 0.5)

    def get(
        self,
        grid: Grid,
        move: tuple[int, int] = None,
        turn: Move = None,
    ) -> float:
        if move is not None and turn is not None:
            grid = Grid(grid)
            grid.move(turn, *move)

        return self.table[repr(grid)]

    def set(
        self,
        grid: Grid,
        val: float,
        move: tuple[int, int] = None,
        turn: Move = None,
    ) -> float:
        if move is not None and turn is not None:
            grid = Grid(grid)
            grid.move(turn, *move)

        self.table[repr(grid)] = val

class ProbabilisticPlayer(IntelligentPlayer):
    def __init__(self):
        super().__init__()
        self.table: RewardTable = RewardTable()

    def pick_move(
        self,
        moves: list[tuple[int, int]],
    ) -> tuple[int, int]:
        return max(
            moves,
            key = lambda move: self.table.get(
                self.grid,
                move,
                self.turn,
            ),
        )

class Learning:
    def __init__(self, train: bool=False):
        self.train: bool = train

class TemporalDifferencePlayer(ProbabilisticPlayer, Learning):
    def __init__(self, train: bool=False):
        ProbabilisticPlayer.__init__(self)
        Learning.__init__(self, train)

    def pick_move(
        self,
        moves: list[tuple[int, int]],
    ) -> tuple[int, int]:
        max_move = super().pick_move(moves)
        if not self.train:
            return max_move

        weights = [
            self.table.get(
                self.grid,
                move,
                self.turn,
            )
            for move in moves
        ]
        random_move = random.choices(moves, weights)[0]

        return random_move

