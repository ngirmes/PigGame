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

"""Module for player base"""


class Player:
    """Class to hold player name, score, and turn order"""

    def __init__(self, name, order):
        """Declare name, order, and score"""
        self._name = name
        self._order = order
        self._score = 0

    @property
    def name(self):
        """Get name"""
        return self._name

    @property
    def order(self):
        """Get order"""
        return self._order

    @property
    def score(self):
        """Get score"""
        return self._score

    @score.setter
    def one_roll(self, revert_score):
        """Revert score if a one is rolled"""
        self._score = revert_score

    @score.setter
    def score(self, add_score):
        """Set a new score"""
        self._score += add_score

