#!/usr/bin/env python3

import pytest

import model
from model import grid as model_grid
from model import player as model_player
from model import game as model_game

class TestPlayer:
    @pytest.fixture
    def grid(self) -> model_grid.Grid:
        return model_grid.Grid()

    def player_(
        self,
        grid: model_grid.Grid,
        turn: model.Move,
    ) -> model_player.Player:
        player = model_player.Player()
        player.set_grid(grid, turn)
        return player

    @pytest.fixture
    def player_1(self, grid: model_grid.Grid) -> model_player.Player:
        return self.player_(grid, model.Move.ONE)

    @pytest.fixture
    def player_2(self, grid: model_grid.Grid) -> model_player.Player:
        return self.player_(grid, model.Move.TWO)

    def test_move(
        self,
        grid: model_grid.Grid,
        player_1: model_player.Player,
        player_2: model_player.Player,
    ):
        player_1.move(1, 1)
        assert repr(grid) == (
            4 * model.Move.NONE.value
            + model.Move.ONE.value
            + 4 * model.Move.NONE.value
        )

        player_2.move(0, 0)
        assert repr(grid) == (
            model.Move.TWO.value
            + 3 * model.Move.NONE.value
            + model.Move.ONE.value
            + 4 * model.Move.NONE.value
        )

    def test_is_winner(
        self,
        grid: model_grid.Grid,
        player_1: model_player.Player,
        player_2: model_player.Player,
    ):
        player_1.move(1, 1)
        assert player_1.is_winner is False
        assert player_2.is_winner is False

        player_1.move(0, 0)
        player_1.move(2, 2)
        assert player_1.is_winner is True
        assert player_2.is_winner is False

class TestStraightPlayer(TestPlayer):
    def straight_player_(
        self,
        grid: model_grid.Grid,
        turn: model.Move,
    ) -> model_player.StraightPlayer:
        player = model_player.StraightPlayer()
        player.set_grid(grid, turn)
        return player

    @pytest.fixture
    def straight_player_1(self, grid: model_grid.Grid) -> model_player.StraightPlayer:
        return self.straight_player_(grid, model.Move.ONE)

    @pytest.fixture
    def straight_player_2(self, grid: model_grid.Grid) -> model_player.StraightPlayer:
        return self.straight_player_(grid, model.Move.TWO)

    def test_play(
        self,
        grid: model_grid.Grid,
        straight_player_1: model_player.StraightPlayer,
    ):
        straight_player_1.play()
        assert repr(grid) == (
            model.Move.ONE.value
            + 8 * model.Move.NONE.value
        )

