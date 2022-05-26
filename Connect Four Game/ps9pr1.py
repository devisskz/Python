#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#
#Name: Batyr Issabekov

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """
    ### add your constructor here ###
    def __init__(self, height, width):
        """gets"""
        self.height = height  #initializes height to heigh and width to width
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)] #given

    def __repr__(self):
        """ Returns a string representation of a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###


        s+= '-' * ((self.width) * 2 +1)  #adds dash underneath the board

        s+= '\n'
        for col in range(self.width):
            if col >9:                 #if col is double digit,
                col = col %10         #mods the col to be single digit
            s+= ' '+str(col)         #adds a space and string of col under board
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)

        ### put the rest of the method here ###

        row = 0
        for i in range(self.height):         #in the range of height
            if self.slots[row][col] == ' ':  #if current place is empty
                row +=1 #add 1 to row, loops again for range of height
        self.slots[row-1][col] = checker #when loop ends, adds checker to row-1

    ### add your reset method here ###

    def reset(self):
        """resets all board objects to contain a space"""

        for row in range(self.height):
            for col in range(self.width):  #loops over all slots in board
                self.slots[row][col] = ' '  #sets them to space

    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self,col):
        """returns true if it is valid to place a checker in column col
        otherwise, returns false"""

        count = 0
        if col <0:
            return False   #if column is less than 0, it is false
        if col>= self.width:  #if column is larger than the table width, false
            return False

        for row in range(self.height):  #loops through the height of the board
            if self.slots[row][col] != ' ':  #if the slot is not empty
                count +=1  #adds 1 to coumt
            else:
                count +=0  #otherwise, doesn't change

        if count == self.height:  #if count is equal to the height of the board
            return False   #then it is full, returns False
        return True   #otherwise, there is space, so returns True

    def is_full(self):
        """returns True if the Board objec is completely full, otherwise False"""

        for col in range(self.width):
            if self.can_add_to(col) == True:   #if can add to method is true
                return False  #returns false, as the board is not full
        return True  #otherwise, the board is full, returns true

    def remove_checker(self,col):
        """removes top checker from column, if the column is empty, does not do
        anything"""
        row = 0
        for i in range(self.height):
            if self.slots[row][col] == ' ':
                if self.slots[row][col] != self.slots[row-1][col]:
                                #if the current slot is empty, and next slot
                                # (underneath) is not
                    row +=1 #adds one to row
                else:
                    row += 0  #othwerwise, doesnt do anything
        self.slots[row][col] = ' ' #set slot with current row to empty

    def is_horizontal_win(self, checker):
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True

    # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self,checker):
        """chekc for vertical win for specified checker"""
        for row in range(self.height-3):
            for col in range(self.width):
                #checks if next four rows contain specified checker
                if self.slots[row][col] == checker and \
                self.slots[row+1][col] == checker and \
                self.slots[row+2][col] == checker and \
                self.slots[row+3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self,checker):
        """checks for down diagonal win for specified checker"""
        for row in range(self.height-3):
            for col in range(self.width-3):
                #checks if next down diagonal slots contain specified checker
                if self.slots[row][col] == checker and \
                self.slots[row+1][col+1] == checker and \
                self.slots[row +2][col+2] == checker and \
                self.slots[row +3][col+3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self,checker):
        """checks for up diagonal win for specified checker"""
        for row in range(3,self.height):
            for col in range(self.width-3):
                #checks if next up and right diagonal slots contain specified
                #checker
                if self.slots[row][col] == checker and \
                self.slots[row-1][col+1] == checker and \
                self.slots[row-2][col+2] == checker and \
                self.slots[row-3][col+3] == checker:
                    return True
        return False



    def is_win_for(self,checker):
        """takes parameter X or O and returns True if there are four
        consecutive slots containing that checker on the board"""
        #tests for every case to see if it is win or lose
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
