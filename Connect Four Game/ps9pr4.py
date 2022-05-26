#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four
#

import random
from ps9pr3 import *

class AIPlayer(Player): #inherits from player
    """looks ahead to assess each possible move that it could take and
    assign a schore to each possible move"""
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs AIplayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """returns a string representing AIPlayer object"""
        AIPlayer = "Player "+str(self.checker) + " ("+str(self.tiebreak) \
        +", " +str(self.lookahead)+")"
        return AIPlayer

    def max_score_column(self,scores):
        """takes a list scores and returns index of the column with max score"""
        max_score = max(scores) #uses max function to determine the max of score
        list = [] #new list
        for i in range(len(scores)): #index based loop
            if scores[i] == max_score: #if number in scores is the same as max
                list += [i] #add that number ot new list
        if self.tiebreak == "LEFT": # if tiebreak is left
            return list[0] #chooses the left most score
        elif self.tiebreak == "RIGHT": #if tiebreak is right
            return list[-1] #chooses right most score
        else:
            return random.choice(list) #otherwise, chooses at random

    def scores_for(self,b):
        """determines the calles aiplayes scores for the columns in b"""
        scores = [50] * b.width  #creates a list of length of width of board
        for i in range(b.width):  #loops over columns
            if b.can_add_to(i) == False:  #if cant add to column
                scores[i] = -1   #sets -1 to that column index
            elif b.is_win_for(self.checker) == True: #if certain win for self
                scores[i] = 100 #sets 100
            elif b.is_win_for(self.opponent_checker()) == True: #if win for opponent
                scores[i] = 0 #sets 0
            elif self.lookahead == 0: #if lookahead is 0, sets to 50, as stated
                scores[i] = 50
            else:
                b.add_checker(self.checker,i) #adds checekr to current column
                opponent = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1)
                #creates opponent with same everything, but lookahead is one less.
                opponent_scores = opponent.scores_for(b) #recursive call
                if max(opponent_scores) == 100: #if opponent score is 100
                    scores[i] = 0 #sets index of score to 0
                elif max(opponent_scores) == 0: #if opponent score is 0
                    scores[i] = 100 #sets to 100
                else:
                    scores[i] = 50 #otherwise, sets to 50
                b.remove_checker(i) #removes checker that was places in column ^
        return scores

    def next_move(self,b):
        """overrides the next move that is inherited from player"""
        self.num_moves +=1
        judgment = self.max_score_column(self.scores_for(b))
        #determines the column number that has to be returned
        return judgment
