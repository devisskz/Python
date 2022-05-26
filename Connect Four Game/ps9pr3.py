#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game
#

from ps9pr1 import Board
from ps9pr2 import Player
import random

def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)

    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p,b):
    """takes two parameters p and b, and processes a single move"""
    print(str(p) + "'s turn")   #couldn't get __repr__ to work, so prints the p
    next_move = p.next_move(b)  #assigned next_move to approptiate variable
    b.add_checker(p.checker,next_move) #calls add checker to update board
    print() #empty line
    print(b) #prints the board
    if b.is_win_for(p.checker) == True:  #if it is win for player
        print(str(p) + " wins in " + str(p.num_moves) + " moves.")
        print("Congratulations!") #eturns win
        return True
    elif b.is_full(): #if the board is full
        print("It's a tie!")  #it is a tie
        return True
    else:  #otherwise, returns false
        return False

class RandomPlayer(Player): #specifies that inherits from player
    """class of unintelligent computer player that chooses at random"""
    def next_move(self,b):
        """overrides the next_move that is inherited from plauer"""
        self.num_moves +=1  #counts number of moves everytime called
        while True:  #while loop
            i = random.choice(range(b.width)) #randomly chooses number from
                                            # width of the board
            if b.can_add_to(i) == True:     #if that number can add to the board
                return i        #returns that number
