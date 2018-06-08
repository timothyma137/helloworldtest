#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:38:25 2018

@author: TimothyMa
"""

# Paste your code into this box 

previouslongestlength=1

index=0
for char in range(len(s)-1):
    longestlength=1
    while s[char]<=s[char+1]:
        longestlength +=1
        if longestlength>previouslongestlength:
            index=char-longestlength+2
            previouslongestlength=longestlength


        char +=1
        
        if char+1== len(s):
            break
        
print("Longest substring in alphabetical order is:", s[index:index+previouslongestlength])