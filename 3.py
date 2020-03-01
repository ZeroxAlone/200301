# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:52:40 2020

@author: lisa_
"""


def CheckSum(x):
    total = 0
    for i in range(len(x)-1):
        total += int(x[i])*(i+1)
    if 11-total%11 == int(x[-1]):
        print("Correct")
    else:
        print("Incorrect")

CheckSum("12343")