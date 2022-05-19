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

"""Module to execute gameplay"""
import time
import sys
from .die import Die
from .player import Player


def slow_print(output):
    """Slow speed for sleep print"""
    for char in output:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)


def fprint(output):
    """Fast speed for sleep print"""
    for char in output:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)


class PigGame:
    """Class for running game"""

    def __init__(self):
        """Method for welcoming user and printing rules"""
        self._players = []
        self._welcome = "Welcome to pig game!\n"
        self._rules = (
            "\nRules:\n1. Players will take turns rolling a die\n"
            "2. On your turn, each roll will add to your total score\n"
            "3. A player's turn ends when they either decide to stop rolling, "
            "or they roll a 1\n"
            "4. If a 1 is rolled, points accumulated during your turn "
            "are revoked, and your turn ends immediately\n"
            "5. If played single player, an AI will be used to"
            "simulate an opponent\n"
        )

    def run(self):
        """Method for running game"""
        die = Die()
        fprint(self._welcome)
        fprint("Would you like to see the rules? (y/n): ")
        see_rules = input()
        while see_rules not in ("y", "n"):
            fprint("Invalid Input - " "Please enter either 'y' or 'n': ")
            see_rules = input()

        if see_rules == "y":
            fprint(self._rules)

        fprint("\nHow many players? [1-4]: ")
        num_players = int(input())
        while num_players not in range(1, 5):
            fprint("Invalid Input - Please enter an integer 1-4: ")
            num_players = int(input())

        """Begin Single Player Block"""
        if num_players == 1:
            ai_num_players = 2
            fprint(f"\nEnter your name: ")
            name = input()
            order = die.roll()
            self._players.append(Player(name, order))
            fprint(f"{name} is rolling for turn priority! ")
            fprint("Highest roll wins!\n")
            slow_print(f".............{order}!\n")
            name = "Tobor"
            order = die.roll()
            self._players.append(Player(name, order))
            fprint(f"\n{name} is rolling for turn priority! ")
            fprint("Highest roll wins!\n")
            slow_print(f".............{order}!\n")

            fprint("\nThe turn order is:\n")
            for i in range(ai_num_players):
                fprint(f"{i+1}. {self._players[i].name}\n")
            self._players.sort(key=lambda p: p.order, reverse=True)
            time.sleep(0.5)

            index = 0
            winning_score = 0
            accumulated_points = 0
            num_rolls = 1
            first_roll = 1
            """First roll block"""
            while True:
                if winning_score == 30:
                    break
                begin_score = self._players[index].score
                fprint(
                    f"\n{self._players[index].name}"
                    "'s turn!"
                    "\nStarting score: "
                    f"{self._players[index].score}\n"
                )
                roll = die.roll()
                fprint("First roll:\n")
                slow_print(f".........{roll}!\n")
                if roll == 1:
                    fprint(f"\n{self._players[self].name} lost their turn! ")
                    fprint(f"Your score is still: {begin_score}\n")
                    index = (index + 1) % len(self._players)
                    continue
                elif first_roll == 1:
                    self._players[index].score = roll
                    accumulated_points += roll
                    first_roll += 1
                    fprint("\nCurrent score: ")
                    fprint(f"{self._players[index].score}\n")
                    fprint("Accumulated Points: ")
                    fprint(f"{accumulated_points}\n")
                    fprint(f"{self._players[index].name} has rolled "
                    f"{num_rolls} time this turn!\n")
                    if self._players[index].score >= 30:
                        fprint(f"\n{self._players[index].name} " "wins!\n")
                        winning_score = 30
                elif self._players[index].name == "Tobor" and first_roll != 1:
                    fprint("Tobor is rolling again!\n")
                    roll = die.roll()
                    slow_print(f".............{roll}!\n")
                    if roll == 1:
                        fprint("\nTobor lost their points for this turn! ")
                        fprint(f"Tobor's score is now: {begin_score}\n")
                        self._players[index].one_roll = begin_score
                        index = (index + 1) % len(self._players)
                        accumulated_points = 0
                        num_rolls = 1
                        first_roll -= 1
                    else: 
                        self._players[index].score = roll
                        accumulated_points += roll
                        num_rolls += 1
                        fprint("Current score: ")
                        fprint(f"{self._players[index].score}\n")
                        fprint("Accumulated Points: ")
                        fprint(f"{accumulated_points}\n")
                        fprint(f"Tobor has rolled {num_rolls} times this turn!\n")
                        if self._players[index].score >= 30:
                            fprint(f"\n{self._players[index].name} " "wins!\n")
                            winning_score = 30
                            break
                elif first_roll != 1:
                    accumulated_points = 0
                    num_rolls = 1
                    index = (index + 1) % len(self._players)
        """End Single Player Block"""

        """Begin 2-4 Players Block"""
        """Obtain user info"""
        if num_players > 1:
            for i in range(num_players):
                fprint(f"\nEnter player {i+1}'s name: ")
                name = input()
                order = die.roll()
                fprint(f"{name} is rolling for turn priority! ")
                fprint("Highest roll wins!\n")
                slow_print(f".............{order}!\n")
                self._players.append(Player(name, order))
            self._players.sort(key=lambda p: p.order, reverse=True)
            time.sleep(0.5)

            """Print turn order"""
            fprint("\nThe turn order is:\n")
            for i in range(num_players):
                fprint(f"{i+1}. {self._players[i].name}\n")
            time.sleep(0.5)

            """Gameplay block"""
            index = 0
            winning_score = 0
            accumulated_points = 0
            num_rolls = 1
            while True:
                if winning_score == 30:
                    break
                begin_score = self._players[index].score
                fprint(
                    f"\n{self._players[index].name}"
                    "'s turn!"
                    "\nStarting score: "
                    f"{self._players[index].score}\n"
                )
                roll = die.roll()
                fprint("First roll:\n")
                slow_print(f".........{roll}!\n")
                if roll == 1:
                    fprint("\nYou've lost your turn! ")
                    fprint(f"Your score is still: {begin_score}\n")
                    index = (index + 1) % len(self._players)
                    continue
                else:
                    self._players[index].score = roll
                    accumulated_points += roll
                    fprint("Current score: ")
                    fprint(f"{self._players[index].score}\n")
                    fprint("Accumulated Points: ")
                    fprint(f"{accumulated_points}\n")
                    fprint(f"You have rolled {num_rolls} time this turn!\n")
                    if self._players[index].score >= 30:
                        fprint(f"\n{self._players[index].name} " "wins!\n")
                        winning_score = 30
                        break

                while True:
                    fprint("\nRoll again? (y/n): ")
                    player_roll = input()
                    if player_roll == "y":
                        roll = die.roll()
                        slow_print(f".............{roll}!\n")
                        if roll == 1:
                            fprint("\nYou've lost your points for this turn! ")
                            fprint(f"Your score is now: {begin_score}\n")
                            self._players[index].one_roll = begin_score
                            index = (index + 1) % len(self._players)
                            accumulated_points = 0
                            num_rolls = 1
                            break

                        else:
                            self._players[index].score = roll
                            accumulated_points += roll
                            num_rolls += 1
                            fprint("Current score: ")
                            fprint(f"{self._players[index].score}\n")
                            fprint("Accumulated points: ")
                            fprint(f"{accumulated_points}\n")
                            fprint(f"You have rolled {num_rolls} times this turn!\n")

                            if self._players[index].score >= 30:
                                fprint(f"\n{self._players[index].name} " "wins!\n")
                                winning_score = 30
                                break
                    elif player_roll == "n":
                        index = (index + 1) % len(self._players)
                        accumulated_points = 0
                        num_rolls = 1
                        break

                    else:
                        fprint("Invalid Input - Please enter a 'y' or 'n'")
            """End 2-4 Players Block"""