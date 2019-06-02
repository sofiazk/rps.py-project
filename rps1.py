#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player():
    def __init__(self):
        pass

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return(random.choice(moves))
        return(throw)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        where = input("Rock, paper, or scissors? >")
        where = where.lower()
        while where not in moves and where != 'x':
            where = input('Invalid move\n')
        if where == 'x':
            exit()
        return where

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            return random.choice(moves)
        return self.learn_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class Cycles(Player):
    def __init__(self):
        Player.__init__(self)
        self.step = 0

    def move(self):
        throw = None
        if self.step == 0:
            throw = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            throw = moves[1]
            self.step = self.step + 1
        else:
            throw = moves[2]
            self.step = self.step + 1
        return throw


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("Its a tie!")
        if beats(move1, move2) is True:
            print("You won!")
            self.p1.score += 1
        elif beats(move2, move1) is True:
            print("You lost!")
            self.p2.score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Rock, paper, scissors, go!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('Player 1 wins!')
        elif self.p1.score < self.p2.score:
            print('Player 2 wins!')
        else:
            print('It is a tie!')
        print('The final score was: ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
