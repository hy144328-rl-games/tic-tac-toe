#!/usr/bin/env python3

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
        self.player_2.set_grid(self.grid, Move.ONE)

    @property
    def is_finished(self) -> bool:
        return (
            all(self.grid[i, j] != Move.NONE for i in range(3) for j in range(3))
            or self.player_1.is_winner
            or self.player_2.is_winner
        )

