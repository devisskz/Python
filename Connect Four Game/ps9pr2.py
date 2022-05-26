#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class
#
#Name: Batyr Issabekov

from ps9pr1 import Board

# write your class below

class Player:

    def __init__(self,checker):
        """initializes attributes to construct a player object"""
        self.checker = checker #attributes checker and num moves as states
        self.num_moves = 0

    def __repr__(self):
        """returns a string of player object"""
        return 'Player ' + str(self.checker)
        #returns player and current checker

    def opponent_checker(self):
        if self.checker == 'X':
            return 'O' #if current player is x, returns o
        else:
            return 'X' #if not x, then o

    def next_move(self,b):
        while True:  #decided to use a while true loop, in order to constantly
        #ask for an input
            column = int(input('Enter a column: ')) #input has to be integer
            if b.can_add_to(column) == True: #calls a method from board
                self.num_moves +=1 #if it is true, adds 1 to num moves and
                return column      #returns the input
            print('Try again!')  #otherwise, prints try again
