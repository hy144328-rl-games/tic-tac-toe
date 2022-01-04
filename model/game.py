#!/usr/bin/env python3

from . import Move
from .grid import Grid
from .player import Player

class Game:
    def __init__(self):
        self.grid = Grid()
        self.player_1 = Player()
        self.player_2 = Player()

        self.player_1.set_grid(self.grid, Move.ONE)
        self.player_2.set_grid(self.grid, Move.TWO)

    @property
    def is_finished(self) -> bool:
        return (
            all(self.grid[i, j] != Move.NONE for i in range(3) for j in range(3))
            or self.player_1.is_winner
            or self.player_2.is_winner
        )

