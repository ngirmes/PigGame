#!/usr/bin/env python3
# Nicholas Girmes
# CPSC 386-04
# 2022-02-08
# n.girmes@csu.fullerton.edu
# @ngirmes
#
# Lab 00-01
#
# Program simluates the game, 'Pig'!
#

"""Executes game.run"""

from piggame import game

if __name__ == "__main__":
    g = game.PigGame()
    g.run()
