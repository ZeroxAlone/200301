# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:03:01 2020

@author: lisa_
"""



def ISBN_13(Data):
    Total = 0
    for i in range(len(Data)-1):
        if i % 2 == 0:
            Weight = 1
        if i % 2 == 1:
            Weight = 3
        Total += int(Data[i])*Weight
    if 10-Total%10 == int(Data[-1]):
        print("Correct")
    else:
        print("Incorrect")

ISBN_13("9787301141724")