#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:48:02 2018

@author: TimothyMa
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp==0:
        return 1
    elif exp==1:
        return base
    else:
        return base*iterPower(base,exp-1)