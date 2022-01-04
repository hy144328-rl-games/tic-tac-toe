#!/usr/bin/env python3

import pytest

import model
from model import grid as model_grid
from model import player as model_player
from model import game as model_game

class TestGame:
    @pytest.fixture
    def game(self) -> model_game.Game:
        game = model_game.Game()

        grid = model_grid.Grid()
        game.set_grid(grid)

        player_1 = model_player.Player()
        game.set_player_1(player_1)

        player_2 = model_player.Player()
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

