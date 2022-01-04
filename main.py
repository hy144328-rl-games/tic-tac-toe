#!/usr/bin/env python3

from model.game import Game

game = Game()
print(game.grid)
print(game.is_finished)

for i in range(3):
    game.player_1.move(i, i)
print(game.grid)
print(game.is_finished)

