#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# 2-D Lists
#
# Computer Science 111
#Name: Batyr Issabekov
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# IMPORTANT: This file is for your solutions to Problem 2.
# Your solutions to problem 3 should go in ps7pr3.py instead.

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []

    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])

    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line


def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

def inner_grid(height,width,digit):
    """creates and returns a 2d list where inner cells have a value of digit"""

    grid = create_grid(height,width) #creates grid

    for r in range(height):
        for c in range(width):
            if r == 0 or r== height-1:  #if r is 0 (first) or height-1 (end)
                grid[r][c] = 0          #assigns to 0
            elif c == 0 or c == width-1: #if c is 0 (first) or width-1 (end)
                grid[r][c] = 0          #assigns it to 0
            else:
                grid[r][c] = digit      #otherwise, assigned to digit

    return grid

def copy(grid):
    '''creates and returns a deep copy of grid, in a separate 2d list'''
    grid1 = create_grid(len(grid), len(grid[0])) #creates a grid for grid1(same)

    for r in range(len(grid)):     #for row in grid
        for c in range(len(grid[0])):   #for col in grid
            grid1[r][c]=grid[r][c]       #writes the same values, but
                                        #onto a new list, grid1

    return grid1 #returns a new list (grid)


def increment(grid):
    '''takes an existing list and increments each digit by 1'''

    for r in range(len(grid)):   #for each row in grid
        for c in range(len(grid[0])):  #for each col in grid
            grid[r][c] +=1     #adds 1 to each elem in list
