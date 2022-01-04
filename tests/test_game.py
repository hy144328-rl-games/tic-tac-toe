#!/usr/bin/env python3

import pytest

import model
from model import grid as model_grid
from model import player as model_player
from model import game as model_game

class TestGame:
    @pytest.fixture
    def grid(self) -> model_grid.Grid:
        return model_grid.Grid()

    @pytest.fixture
    def player_1(self) -> model_player.Player:
        return model_player.Player()

    @pytest.fixture
    def player_2(self) -> model_player.Player:
        return model_player.Player()

    @pytest.fixture
    def game(
        self,
        grid: model_grid.Grid,
        player_1: model_player.Player,
        player_2: model_player.Player,
    ) -> model_game.Game:
        game = model_game.Game()

        game.set_grid(grid)
        game.set_player_1(player_1)
        game.set_player_2(player_2)

        return game

    def test_is_finished(
        self,
        game: model_game.Game,
    ):
        game.player_1.move(1, 1)
        assert game.is_finished is False

        game.player_1.move(0, 0)
        game.player_1.move(2, 2)
        assert game.is_finished is True

