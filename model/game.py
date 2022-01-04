#!/usr/bin/env python3

import abc
import itertools

from . import Move
from .grid import Grid
from .player import Player

class Game:
    def set_grid(self, grid: Grid):
        self.grid: Grid = Grid()

    def set_player_1(self, player: Player):
        self.player_1: Player = player
        self.player_1.set_grid(self.grid, Move.ONE)

    def set_player_2(self, player: Player):
        self.player_2: Player = player
        self.player_2.set_grid(self.grid, Move.TWO)

    @property
    def is_finished(self) -> bool:
        return (
            all(self.grid[i, j] != Move.NONE for i in range(3) for j in range(3))
            or self.player_1.is_winner
            or self.player_2.is_winner
        )

    def reset(self):
        self.grid.reset()
        self.player_1.reset()
        self.player_2.reset()

class IntelligentGame(Game, abc.ABC):
    def simulate(self):
        turns = itertools.cycle([self.player_1, self.player_2])

        for player_it in turns:
            player_it.play()

            if self.is_finished:
                break

