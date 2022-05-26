#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:06:47 2020

@author: b.isz
"""

#Problem 2: Algorithm Design

#Name: Batyr Issabekov

def abs_list_lc(values):
    """takes as input a list of numbers called values, and that 
    uses a list comprehension to create and return a list containing the
    absolute values of the numbers in values"""
    return [abs(w) for w in values] #absolute value for each elem in values

def abs_list_rec(values):
    """takes as input a list of numbers called values, and that uses recursion 
    to create and return a list containing the absolute 
    values of the numbers in values"""
    if values == []:
        return []
    else:
        abs_rest = abs_list_rec(values[1:]) #recursive call
        return [abs(values[0])] + abs_rest 
    #returns absolute value as list + recursive call
    
    
def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])     #given
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_vowels(words):
    if len(words) == 0:
        return ''
    else:
        most_rest = most_vowels(words[1:]) #recursive call
        if num_vowels(words[0])>num_vowels(most_rest): 
            #if words[0] more vowels than rest, return it
            return words[0]
        else:
            return most_rest #otherwise, return rest

def num_multiples(m, values):
    """takes an integer m and a list of integers values and returns the number 
    of integers in values that are multiples of m"""  
    if values == []:
        return 0
    else:
        num_rest = num_multiples(m,values[1:]) # recursive call
        if values[0]%m == 0: # if elem 1 in list is multiple
            return 1+num_rest #add 1 to num_rest
        else:
            return num_rest #otherwise, return existing num rest

def price_string(cents):
    """positive integer cents representing a price given in cents, and that
    constructs and returns a string in which the price is expressed as a 
    combination of dollars and cents."""
    d = cents//100   # compute whole number of dollars
    c = cents%100   # compute remaining cents

    price = ''            # initial value of the price string

    ## add code below to build up the price string
    
    if d>0: # if at least one dollar
        if d == 1: # if exactly one, then
            price = price + str(d) + ' dollar' #prints dollar
        else:
            price = price + str(d) + ' dollars' #if more, prints dollars
    if c>0: #if at least one cent
        if price != '': #if price is not empty
            price = price+ ', ' #then adds comma
        if c == 1: # if cents is exactly one
            price = price+ str(c)+' cent' #prints cent
        else:
            price = price + str(c)+' cents' # #otherwise, cents
    return price

      