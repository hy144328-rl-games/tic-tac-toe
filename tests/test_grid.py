#!/usr/bin/env python3

import pytest

import model
from model import grid as model_grid
from model import player as model_player
from model import game as model_game

class TestGrid:
    @pytest.fixture
    def grid(self) -> model_grid.Grid:
        return model_grid.Grid()

    def test_move(self, grid: model_grid.Grid):
        grid.move(model.Move.ONE, 1, 1)
        assert repr(grid) == (
            4 * model.Move.NONE.value
            + model.Move.ONE.value
            + 4 * model.Move.NONE.value
        )

    def test_in_line(self, grid: model_grid.Grid):
        grid.move(model.Move.ONE, 1, 1)
        assert grid.in_line(model.Move.ONE) is False

        grid.move(model.Move.ONE, 0, 0)
        grid.move(model.Move.ONE, 2, 2)
        assert grid.in_line(model.Move.ONE) is True

