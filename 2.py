# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:16:58 2020

@author: lisa_
"""

DataList = ["00010011",
            "10110000",
            "11011001",
            "10011101",
            "10110011",
            "10100000",
            "10110000",
            "10101011"]

RowList = []
ColumnList = []
Temp = ["" for i in range(8)]

def OddParity(data):
    ones = 0
    for i in data[0:]:
        if i == "1":
            ones += 1
    if ones%2 == 0:
        return False
    else:
        return True

def Adder(x,c):
    Temp[c] += x
    
def main(DL, RL, CL):
    counti = 0
    countk = 0
    for i in DL:
        if OddParity(i) == False:
            RL.append(counti)
        counti += 1
        countj = 0
        for j in i:
            Adder(j,countj)
            countj += 1
    for k in Temp:
        if OddParity(k) == False:
            CL.append(countk)
        countk += 1
    for n in range(len(RL)):
        if DL[RL[n]][CL[n]] == "1":
            DL[RL[n]] = DL[RL[n]][:CL[n]]+"0"+DL[RL[n]][CL[n]+1:]
        else:
            DL[RL[n]] = DL[RL[n]][:CL[n]]+"1"+DL[RL[n]][CL[n]+1:]
    
    print(DL)
    
main(DataList, RowList, ColumnList)
        
            