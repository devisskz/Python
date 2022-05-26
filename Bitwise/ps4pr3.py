#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:55:07 2020

Name: Batyr Issabekov

Problem Set 4, Problem 3: Recursive operations on binary numbers.
"""

def bitwise_and(b1, b2):
    """inputs two strings, binary, uses recursion
    to compute the bitwise AND of the two numbers"""
    if b1 == '' and b2 == '':
        return '' #base case
    elif b1 == '':
        return (len(b2)-len(b1))*'0' #base case 2
    elif b2 == '':
        return (len(b1)-len(b2))*'0' #base case 3
    else:
        bit_rest = bitwise_and(b1[:-1], b2[:-1]) #recursive call
        if b1[-1] == '1' and b2[-1] == '1': #if the two numbers are one
            return bit_rest + '1'  #returns one
        else:
            return bit_rest + '0' #otherwise returns '0'
        
def add_bitwise(b1,b2):
    """adds two binary numbers using recursion and returns the result"""
    if b1 == '':
        return b2 #base case 1 
    elif b2 == '':
        return b1 #base case  2 ( if one strins is empty)
    else:
        add_rest = add_bitwise(b1[:-1], b2[:-1]) #recursive call
        if b1[-1] == '1' and b2[-1] == '0': #if 1 and 0, +1 to the string
            return add_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '1': #if 0 and 1, + 1 to the string
            return add_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '0': #if both 0, +0 to the string
            return add_rest + '0'
        else: #if 1 and 1
            return add_bitwise(add_rest, '1') + '0' #calls add_bitwise second 
                                #time, add_rest as b1, 1 as b2 ( adds 0 
                                                #         because 1+1 = 10 )