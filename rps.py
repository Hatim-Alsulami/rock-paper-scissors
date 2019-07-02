#!/usr/bin/env python3

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.

import random
import time

moves = ['rock', 'paper', 'scissors']

# print message to the user after 2 seconds
def print_pause(text): 
    time.sleep(2)
    print(text)


# parent class player
class Player:
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


# this class select random move
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# this class request the human player to select a move
# and check if the input is valid
class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Rock, paper, scissors?\n").lower()
            if human_move not in moves:
                continue
            else:
                print(f"Your move is {human_move}")
                break
        return human_move


# this class refelct the previous move of human player
class ReflectPlayer(Player):
    def move(self):
        return self.their_move


# this class cycle over the list of move
class CyclePlayer(Player):
    def move(self):
        index = moves.index(self.my_move)
        if index == 2:
            return moves[0]
        else:
            return moves[index + 1]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

# play the game, check the moves and print them.
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Your move: {move1} Opponent's move: {move2}")
        self.keep_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

# keep record of the score
    def keep_score(self, move1, move2):
        if beats(move1, move2):
            self.p1_score += 1
            print_pause(f"{move1} beats {move2}. You win this round")
        elif beats(move2, move1):
            self.p2_score += 1
            print_pause(f"{move2} beats {move1}. Opponent wins this round")
        else:
            print_pause("No winner!!")
        print_pause(f"Your score {self.p1_score}")
        print_pause(f"Opponent's score {self.p2_score}")

# Present the result of the game
    def game_result(self):
        if self.p1_score > self.p2_score:
            print_pause("You win the match")
        elif self.p1_score < self.p2_score:
            print_pause("Opponent wins the match")
        else:
            print_pause("It is a TIE!!")

# play a game of a single round
    def single_game(self):
        print("Round 1 of 1")
        self.play_round()
        self.game_result()
        print("Game over!")

    def round_game(self):
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        self.game_result()
        print("Game over!")

# this function will start the game
# ask the user for type of game
# check the validity of the input
    def play_game(self):
        print("Game start!")
        while True:
            game_type = input("Enter 1 for single round or "
                              "2 fora game of three rounds:\n")
            game_type_int = int(game_type)
            if game_type_int == 1:
                self.single_game()
                break
            elif game_type_int == 2:
                self.round_game()
                break
            else:
                continue


if __name__ == '__main__':
    #let the computer choose which strategy to play with
    strategy = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    game_mode = random.choice(strategy)
    game = Game(HumanPlayer(), game_mode)
    game.play_game()
