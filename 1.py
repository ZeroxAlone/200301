# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:05:28 2020

@author: lisa_
"""
def OddParity(data):
    ones = 0
    for i in data[0:]:
        if i == "1":
            ones += 1
    if ones%2 == 0:
        print("Incorrect")
    else:
        print("Correct")

OddParity("10010010")
        