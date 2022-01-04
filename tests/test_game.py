#!/usr/bin/env python3

import pytest

import model
from model import grid as model_grid
from model import player as model_player
from model import game as model_game

class TestGame:
    @pytest.fixture
    def game(self) -> model_game.Game:
        return model_game.Game()

    @pytest.fixture
    def grid(self, game: model_game.Game) -> model_grid.Grid:
        return game.grid

    @pytest.fixture
    def player_1(self, game: model_game.Game) -> model_player.Player:
        return game.player_1

    @pytest.fixture
    def player_2(self, game: model_game.Game) -> model_player.Player:
        return game.player_2

    def test_is_finished(
        self,
        game: model_game.Game,
        grid: model_grid.Grid,
        player_1: model_player.Player,
        player_2: model_player.Player,
    ):
        player_1.move(1, 1)
        assert game.is_finished is False

        player_1.move(0, 0)
        player_1.move(2, 2)
        assert game.is_finished is True

