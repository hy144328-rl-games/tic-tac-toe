#!/usr/bin/env python3

import enum
import numpy as np

class Move(enum.Enum):
    ONE = 1
    TWO = 2
    NONE = 0

class State:
    def __init__(self):
        self.m: np.ndarray = np.full((3, 3), Move.NONE)

if __name__ == "__main__":
    state = State()
    print(state.m)

