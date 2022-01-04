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

if __name__ == "__main__":
    grid = Grid()
    print(grid.state)

