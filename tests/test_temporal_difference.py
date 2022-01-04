#!/usr/bin/env python3

import pytest

import model
from model import grid as model_grid
from model import player as model_player
from model import game as model_game

from .test_game import TestIntelligentGame

class TestProbabilisticGame1(TestIntelligentGame):
    @pytest.fixture
    def player_1(self) -> model_player.IntelligentPlayer:
        return model_player.ProbabilisticPlayer()

class TestProbabilisticGame2(TestIntelligentGame):
    @pytest.fixture
    def player_2(self) -> model_player.IntelligentPlayer:
        return model_player.ProbabilisticPlayer()

class TestProbabilisticGame12(TestProbabilisticGame1):
    @pytest.fixture
    def player_2(self) -> model_player.IntelligentPlayer:
        return model_player.ProbabilisticPlayer()

class TestTemporalDifferenceGame1(TestIntelligentGame):
    @pytest.fixture
    def player_1(self) -> model_player.IntelligentPlayer:
        return model_player.TemporalDifferencePlayer()

class TestTemporalDifferenceGame2(TestIntelligentGame):
    @pytest.fixture
    def player_2(self) -> model_player.IntelligentPlayer:
        return model_player.TemporalDifferencePlayer()

class TestTemporalDifferenceGame12(TestTemporalDifferenceGame1):
    @pytest.fixture
    def player_2(self) -> model_player.IntelligentPlayer:
        return model_player.TemporalDifferencePlayer()

class TestTemporalDifferenceGameTrain1(TestIntelligentGame):
    @pytest.fixture
    def player_1(self) -> model_player.IntelligentPlayer:
        return model_player.TemporalDifferencePlayer(True)

    def test_simulate(
        self,
        game: model_game.Game,
    ):
        for _ in range(10):
            game.reset()
            game.simulate()
            print(game.grid)

        assert False

