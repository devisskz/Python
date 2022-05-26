#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:18:44 2020

@author: b.isz
"""

#Name: Batyr Issabekov
#PS3, Problem 4: More algorithm design

def index(elem,seq):
    """takes elem and seq as inputs and uses recursion to return index of
    first occurence of elem in seq, the seq can be list or string"""
    if seq == '':
        return -1 #base case 1
    elif seq == []:
        return -1 #base case 2
    else:
        index_rest = index(elem,seq[1:]) #recursive call
        if elem == seq[0]:
            return 0 #return 0 if first index of seq is elem
        else:
            return 1 + index_rest

def index_last(elem, seq):
    """ takes elem and seq, uses recursion to return last occurence of elem"""
    if seq == '':
        return -1 #base case
    elif seq == []:
        return -1 #base case 2
    else:
        index_rest = index(elem, seq[:-1]) #recursive call from behind
        if elem == seq[-1]: #if last element is elem
            return len(seq) - 1 #returns length of sequence, -1 to account for
                                #index starting with 0
        else:
            return index_rest #otherwise, recursive call
        
#helper function

def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values
    """
    if values == '':
        return ''
    elif values[0] == elem:             #from lecture, modified for string
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest

def jscore(s1,s2):
    """takes strings s1 and s2, returns Jotto score comparing them"""
    if s1 == '' or s2 == '': #base case
        return 0
    else:
        j_rest = jscore(s1[1:],rem_first(s1[0],s2)) #recursive call utilizes 
                                        #the rem_frst function
                            
        if s1[0] in s2: #as given from notes/hints
            return 1 + j_rest #returns count of letters
        else:
            return j_rest #otherwise, recursive call