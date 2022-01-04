#!/usr/bin/env python3

import pytest

import model
from model import grid as model_grid
from model import player as model_player
from model import game as model_game

from .test_game import TestIntelligentGame

class TestProbabilisticGame1(TestIntelligentGame):
    @pytest.fixture
    def player_1(self) -> model_player.StraightPlayer:
        return model_player.ProbabilisticPlayer()

class TestProbabilisticGame2(TestIntelligentGame):
    @pytest.fixture
    def player_2(self) -> model_player.StraightPlayer:
        return model_player.ProbabilisticPlayer()

class TestProbabilisticGame12(TestProbabilisticGame1):
    @pytest.fixture
    def player_2(self) -> model_player.StraightPlayer:
        return model_player.ProbabilisticPlayer()

