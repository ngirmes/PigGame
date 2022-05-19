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

"""Module for rolling a die"""

from random import randrange


class Die:
    """A class for rolling the die on a players turn"""

    def __init__(self):
        """Empty init method"""

    @classmethod
    def roll(cls):
        """Rolls a d6"""
        return randrange(1, 7)

    @classmethod
    def dnd_die(cls):
        """Rolls a d20"""
        return randrange(1, 21)
