# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:35:50 2021

@author: Brandon
"""

class Node(object):
    def __init__(self, val, index):
        self.val = val
        self.possval = [1,2,3,4,5,6,7,8,9]
        self.set = False
        self.index = index
    
    def updateValue(self):
        if(len(self.possval) == 1):
            self.val = self.possval[0]
            self.set = True
            self.possval = [self.val]
        
    def setState(self):
        if(self.val != 0):
            self.set = True
            self.possval = [self.val]

#######################################################
### Moved check for Naked Doubles into updateConstraints.
#    def checkForNakedDoubles(self, Nodelist):
#        if(len(self.possval) == 2):
#            col = self.index[0]
#            row = self.index[1]
#            ## Check column for doubles
#            for i in range(0, 9):
#                if(Nodelist[((i * 9)+row)].possval == self.possval and Nodelist[((i * 9))+row].index != self.index):
#                    for j in range(0, 9):
#                        if(Nodelist[((j * 9)+row)].index != self.index and i != j and Nodelist[((j * 9)+row)].set != True and len(Nodelist[((j * 9)+row)].possval) != 1):
#                            print()
#                            print(Nodelist[((j * 9)+row)].possval)
#                            if(self.possval[0] in Nodelist[((j * 9)+row)].possval):
#                                Nodelist[((j * 9)+row)].possval.remove(self.possval[0])
#                            if(self.possval[1] in Nodelist[((j * 9)+row)].possval):
#                                Nodelist[((j * 9)+row)].possval.remove(self.possval[1])
#                                print(self.possval)
#                                print(Nodelist[((j * 9)+row)].possval)
            ## Check row for doubles
#            for i in range(0, 9):
#                if(Nodelist[((col * 9)+i)].possval == self.possval and Nodelist[((col * 9)+i)].index != self.index):
#                    for j in range(0, 9):
#                        if(Nodelist[((col * 9)+j)].index != self.index and i != j):
#                            if(self.possval[0] in Nodelist[((col * 9)+j)].possval):
#                                Nodelist[((col * 9)+j)].possval.remove(self.possval[0])
#                            if(self.possval[1] in Nodelist[((col * 9)+j)].possval):
#                                Nodelist[((col * 9)+j)].possval.remove(self.possval[1])
###############################################                
    def updateConstraints(self, Nodelist):
        if(self.set == True):
            self.possval = [self.val]
        else:
            ## column first
            temp = self.index[0]
            ## row second
            temp2 = self.index[1]
            ### Remove all values set in column
            for i in range(0, 9):
                ## This will block out self too.
                if(Nodelist[((i * 9)+temp2)].set == True):
                    if(Nodelist[((i * 9)+temp2)].val in self.possval):
                        self.possval.remove(Nodelist[((i * 9)+temp2)].val)
            ###Remove all values set in row
            for j in range(0, 9):
                if(Nodelist[((temp * 9)+j)].set == True):
                     if(Nodelist[((temp * 9)+j)].val in self.possval):
                        self.possval.remove(Nodelist[((temp * 9)+j)].val)    
                        
            ## Messy section with many repeat checks.
            ## Remove all values set in box.
            ## Top left square
            ## Used for "depth"?
            d = 9
            Box = 0
            if(temp < 3 and temp2 < 3):
                ## Quick setup for now
                ## Not super efficient yet.
                Box = 1
                for i in range(0, 3):
                    if(Nodelist[i].set == True):
                        if(Nodelist[i].val in self.possval):
                            self.possval.remove(Nodelist[i].val)
                    if(Nodelist[9 + i].set == True):
                        if(Nodelist[9 + i].val in self.possval):
                            self.possval.remove(Nodelist[9 + i].val)
                    if(Nodelist[18 + i].set == True):
                        if(Nodelist[18 + i].val in self.possval):
                            self.possval.remove(Nodelist[18 + i].val)
            ## Top center square
            elif(temp < 3 and temp2 > 2 and temp2 < 6):
                Box = 2
                for i in range(3, 6):
                    if(Nodelist[i].set == True):
                        if(Nodelist[i].val in self.possval):
                            self.possval.remove(Nodelist[i].val)
                    if(Nodelist[9 + i].set == True):
                        if(Nodelist[9 + i].val in self.possval):
                            self.possval.remove(Nodelist[9 + i].val)
                    if(Nodelist[18 + i].set == True):
                        if(Nodelist[18 + i].val in self.possval):
                            self.possval.remove(Nodelist[18 + i].val)
            ## Top right square
            elif(temp < 3 and temp2 > 5):
                Box = 3
                for i in range(6, 9):
                    if(Nodelist[i].set == True):
                        if(Nodelist[i].val in self.possval):
                            self.possval.remove(Nodelist[i].val)
                    if(Nodelist[9 + i].set == True):
                        if(Nodelist[9 + i].val in self.possval):
                            self.possval.remove(Nodelist[9 + i].val)
                    if(Nodelist[18 + i].set == True):
                        if(Nodelist[18 + i].val in self.possval):
                            self.possval.remove(Nodelist[18 + i].val)
            ## Left middle square
            elif(temp > 2 and temp < 6 and temp2 < 3):
                Box = 4
                for i in range(0, 3):
                    ### start using "depth" here
                    if(Nodelist[i+(d * 3)].set == True):
                        if(Nodelist[i+(d * 3)].val in self.possval):
                            self.possval.remove(Nodelist[i+(d * 3)].val)
                    if(Nodelist[(d * 4) + i].set == True):
                        if(Nodelist[(d * 4) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 4) + i].val)
                    if(Nodelist[(d * 5) + i].set == True):
                        if(Nodelist[(d * 5) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 5) + i].val)
            ## Right middle square
            elif(temp > 2 and temp < 6 and temp2 > 5):
                Box = 6
                for i in range(6, 9):
                    if(Nodelist[i+(d * 3)].set == True):
                        if(Nodelist[i+(d * 3)].val in self.possval):
                            self.possval.remove(Nodelist[i+(d * 3)].val)
                    if(Nodelist[(d * 4) + i].set == True):
                        if(Nodelist[(d * 4) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 4) + i].val)
                    if(Nodelist[(d * 5) + i].set == True):
                        if(Nodelist[(d * 5) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 5) + i].val)
            ## Bottom left square
            elif(temp > 5 and temp2 < 3):
                Box = 7
                for i in range(0, 3):
                    if(Nodelist[i+(d * 6)].set == True):
                        if(Nodelist[i+(d * 6)].val in self.possval):
                            self.possval.remove(Nodelist[i+(d * 6)].val)
                    if(Nodelist[(d * 7) + i].set == True):
                        if(Nodelist[(d * 7) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 7) + i].val)
                    if(Nodelist[(d * 8) + i].set == True):
                        if(Nodelist[(d * 8) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 8) + i].val)
            ## Bottom center square
            elif(temp > 5 and temp2 > 2 and temp2 < 6):
                Box = 8
                for i in range(3, 6):
                    if(Nodelist[i+(d * 6)].set == True):
                        if(Nodelist[i+(d * 6)].val in self.possval):
                            self.possval.remove(Nodelist[i+(d * 6)].val)
                    if(Nodelist[(d * 7) + i].set == True):
                        if(Nodelist[(d * 7) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 7) + i].val)
                    if(Nodelist[(d * 8) + i].set == True):
                        if(Nodelist[(d * 8) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 8) + i].val)
            ## Bottom Right square
            elif(temp > 5 and temp2 > 5):
                Box = 9
                for i in range(6, 9):
                    if(Nodelist[i+(d * 6)].set == True):
                        if(Nodelist[i+(d * 6)].val in self.possval):
                            self.possval.remove(Nodelist[i+(d * 6)].val)
                    if(Nodelist[(d * 7) + i].set == True):
                        if(Nodelist[(d * 7) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 7) + i].val)
                    if(Nodelist[(d * 8) + i].set == True):
                        if(Nodelist[(d * 8) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 8) + i].val)
            ## Center square
            else:
                Box = 5
                for i in range(3, 6):
                    if(Nodelist[i+(d * 3)].set == True):
                        if(Nodelist[i+(d * 3)].val in self.possval):
                            self.possval.remove(Nodelist[i+(d * 3)].val)
                    if(Nodelist[(d * 4) + i].set == True):
                        if(Nodelist[(d * 4) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 4) + i].val)
                    if(Nodelist[(d * 5) + i].set == True):
                        if(Nodelist[(d * 5) + i].val in self.possval):
                            self.possval.remove(Nodelist[(d * 5) + i].val)

#################################################
### Found out that this is bugged after trying 
### Puzzles/Sudoku1-5star.txt and getting bad output.
### It might have something to do with the combination of
### backtracking and this? 
            if(len(self.possval) == 2):
                ### doubles check on a column
                for i in range(0, 9):
                    if(Nodelist[((i * 9)+temp2)].possval == self.possval and Nodelist[((i * 9))+temp2].index != self.index):
                        for j in range(0, 9):
                            if(Nodelist[((j * 9)+temp2)].index != self.index and i != j):
                                if(self.possval[0] in Nodelist[((j * 9)+temp2)].possval):
                                    Nodelist[((j * 9)+temp2)].possval.remove(self.possval[0])
                                if(self.possval[1] in Nodelist[((j * 9)+temp2)].possval):
                                    Nodelist[((j * 9)+temp2)].possval.remove(self.possval[1])
#                ### doubles check on a row
                for i in range(0, 9):
                    if(Nodelist[((temp * 9)+i)].possval == self.possval and Nodelist[((temp * 9)+i)].index != self.index):
                        for j in range(0, 9):
                            if(Nodelist[((temp * 9)+j)].index != self.index and i != j):
                                if(self.possval[0] in Nodelist[((temp * 9)+j)].possval):
                                    Nodelist[((temp * 9)+j)].possval.remove(self.possval[0])
                                if(self.possval[1] in Nodelist[((temp * 9)+j)].possval):
                                    Nodelist[((temp * 9)+j)].possval.remove(self.possval[1])
                ### doubles Box checks
                a = 0
                b = 0
                d1 = 0
                d2 = 0
                d3 = 0
                ## More of a just in case, but it should never happen.
                if(Box != 0):
                    if(Box == 1 or Box == 4 or Box == 7):
                        a = 0
                        b = 3
                    elif(Box == 2 or Box == 5 or Box == 8):
                        a = 3
                        b = 6
                    else:
                        a = 6
                        b = 9
                    if(Box < 4):
                        d1 = 0
                        d2 = 9
                        d3 = 18
                    elif(Box > 6):
                        d1 = 54
                        d2 = 63
                        d3 = 72
                    # 3 < x < 7
                    # 4,5,6
                    else:
                        d1 = 27
                        d2 = 36
                        d3 = 45
                    for i in range(a, b):
                        if(Nodelist[d1 + i].possval == self.possval and Nodelist[d1 + i].index != self.index):
                            for j in range(a, b):
                                if(Nodelist[d1 + j].index != self.index and Nodelist[d1 + j].index != Nodelist[d1 + i].index):
                                    if(self.possval[0] in Nodelist[d1 + j].possval):
                                        Nodelist[d1 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d1 + j].possval):
                                        Nodelist[d1 + j].possval.remove(self.possval[1])
                                if(Nodelist[d2 + j].index != self.index and Nodelist[d2 + j].index != Nodelist[d1 + i].index):
                                    if(self.possval[0] in Nodelist[d2 + j].possval):
                                        Nodelist[d2 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d2 + j].possval):
                                        Nodelist[d2 + j].possval.remove(self.possval[1])
                                if(Nodelist[d3 + j].index != self.index and Nodelist[d3 + j].index != Nodelist[d1 + i].index):
                                    if(self.possval[0] in Nodelist[d3 + j].possval):
                                        Nodelist[d3 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d3 + j].possval):
                                        Nodelist[d3 + j].possval.remove(self.possval[1])
                        if(Nodelist[d2 + i].possval == self.possval and Nodelist[d2 + i].index != self.index):
                            for j in range(a, b):
                                if(Nodelist[d1 + j].index != self.index and Nodelist[d1 + j].index != Nodelist[d2 + i].index):
                                    if(self.possval[0] in Nodelist[d1 + j].possval):
                                        Nodelist[d1 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d1 + j].possval):
                                        Nodelist[d1 + j].possval.remove(self.possval[1])
                                if(Nodelist[d2 + j].index != self.index and Nodelist[d2 + j].index != Nodelist[d2 + i].index):
                                    if(self.possval[0] in Nodelist[d2 + j].possval):
                                        Nodelist[d2 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d2 + j].possval):
                                        Nodelist[d2 + j].possval.remove(self.possval[1])
                                if(Nodelist[d3 + j].index != self.index and Nodelist[d3 + j].index != Nodelist[d2 + i].index):
                                    if(self.possval[0] in Nodelist[d3 + j].possval):
                                        Nodelist[d3 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d3 + j].possval):
                                        Nodelist[d3 + j].possval.remove(self.possval[1])
                        if(Nodelist[d3 + i].possval == self.possval and Nodelist[d3 + i].index != self.index):
                            for j in range(a, b):
                                if(Nodelist[d1 + j].index != self.index and Nodelist[d1 + j].index != Nodelist[d3 + i].index):
                                    if(self.possval[0] in Nodelist[d1 + j].possval):
                                        Nodelist[d1 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d1 + j].possval):
                                        Nodelist[d1 + j].possval.remove(self.possval[1])
                                if(Nodelist[d2 + j].index != self.index and Nodelist[d2 + j].index != Nodelist[d3 + i].index):
                                    if(self.possval[0] in Nodelist[d2 + j].possval):
                                        Nodelist[d2 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d2 + j].possval):
                                        Nodelist[d2 + j].possval.remove(self.possval[1])
                                if(Nodelist[d3 + j].index != self.index and Nodelist[d3 + j].index != Nodelist[d3 + i].index):
                                    if(self.possval[0] in Nodelist[d3 + j].possval):
                                        Nodelist[d3 + j].possval.remove(self.possval[0])
                                    if(self.possval[1] in Nodelist[d3 + j].possval):
                                        Nodelist[d3 + j].possval.remove(self.possval[1])
################################################
#   Old code
#                   if(Box == 1):
#                        for i in range(0, 3):
#                            if(Nodelist[i].possval == self.possval and Nodelist[i].index != self.index):
#                                for j in range(0, 3):
#                                    if(Nodelist[j].index != self.index and Nodelist[j].index != Nodelist[i].index):
#                                        if(self.possval[0] in Nodelist[j].possval):
#                                            Nodelist[j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[j].possval):
#                                            Nodelist[j].possval.remove(self.possval[1])
#                                    if(Nodelist[9 + j].index != self.index and Nodelist[9 + j].index != Nodelist[i].index):
#                                        if(self.possval[0] in Nodelist[9 + j].possval):
#                                            Nodelist[9 + j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[9 + j].possval):
#                                            Nodelist[9 + j].possval.remove(self.possval[1])
#                                    if(Nodelist[18 + j].index != self.index and Nodelist[18 + j].index != Nodelist[i].index):
#                                        if(self.possval[0] in Nodelist[18 + j].possval):
#                                            Nodelist[18 + j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[18 + j].possval):
#                                            Nodelist[18 + j].possval.remove(self.possval[1])
#                            if(Nodelist[9 + i].possval == self.possval and Nodelist[9 + i].index != self.index):
#                                for j in range(0, 3):
#                                    if(Nodelist[j].index != self.index and Nodelist[j].index != Nodelist[9 + i].index):
#                                        if(self.possval[0] in Nodelist[j].possval):
#                                            Nodelist[j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[j].possval):
#                                            Nodelist[j].possval.remove(self.possval[1])
#                                    if(Nodelist[9 + j].index != self.index and Nodelist[9 + j].index != Nodelist[9 + i].index):
#                                        if(self.possval[0] in Nodelist[9 + j].possval):
#                                            Nodelist[9 + j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[9 + j].possval):
#                                            Nodelist[9 + j].possval.remove(self.possval[1])
#                                    if(Nodelist[18 + j].index != self.index and Nodelist[18 + j].index != Nodelist[9 + i].index):
#                                        if(self.possval[0] in Nodelist[18 + j].possval):
#                                            Nodelist[18 + j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[18 + j].possval):
#                                            Nodelist[18 + j].possval.remove(self.possval[1])
#                            if(Nodelist[18 + i].possval == self.possval and Nodelist[18 + i].index != self.index):
#                                for j in range(0, 3):
#                                    if(Nodelist[j].index != self.index and Nodelist[j].index != Nodelist[18 + i].index):
#                                        if(self.possval[0] in Nodelist[j].possval):
#                                            Nodelist[j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[j].possval):
#                                            Nodelist[j].possval.remove(self.possval[1])
#                                    if(Nodelist[9 + j].index != self.index and Nodelist[9 + j].index != Nodelist[18 + i].index):
#                                        if(self.possval[0] in Nodelist[9 + j].possval):
#                                            Nodelist[9 + j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[9 + j].possval):
#                                            Nodelist[9 + j].possval.remove(self.possval[1])
#                                    if(Nodelist[18 + j].index != self.index and Nodelist[18 + j].index != Nodelist[18 + i].index):
#                                        if(self.possval[0] in Nodelist[18 + j].possval):
#                                            Nodelist[18 + j].possval.remove(self.possval[0])
#                                        if(self.possval[1] in Nodelist[18 + j].possval):
#                                            Nodelist[18 + j].possval.remove(self.possval[1])
#############################################################