# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:45:31 2021

@author: Brandon
"""
import copy
from Node import Node

##
def GeneralSearch(Nodelist, layout, Backtracks):
    Going = True
    prevCount = 0
    while Going:
        for i in range(len(Nodelist)):
            Nodelist[i].updateConstraints(Nodelist)
            #Nodelist[i].checkForNakedDoubles(Nodelist)
            Nodelist[i].updateValue()
        count = 0
        for i in range(len(Nodelist)):
            if(len(Nodelist[i].possval) == 0):
                return False, Backtracks
            if(Nodelist[i].set == True):
                count += 1
        if(count == len(Nodelist)):
            for i in range(layout.shape[0]):
                for j in range(layout.shape[1]):
                    layout[i][j] = Nodelist[((i * 9)+j)].val
            Going = False
            return True, Backtracks
        if(count == prevCount):
#            for i in range(9):
#                print(Nodelist[(9 * i) + 0].val,Nodelist[(9 * i) + 1].val,Nodelist[(9 * i) + 2].val,Nodelist[(9 * i) + 3].val,
#                      Nodelist[(9 * i) + 4].val,Nodelist[(9 * i) + 5].val,Nodelist[(9 * i) + 6].val,Nodelist[(9 * i) + 7].val,
#                      Nodelist[(9 * i) + 8].val)
            Backtracks += 1
            temp, worked, Backtracks = BacktrackingSearch(Nodelist, 2, layout, Backtracks)
            if(worked):
                Nodelist = temp
                Going = False
                return True, Backtracks
            else:
                Going = False
                ##print("Hit a wall.")
                for i in range(layout.shape[0]):
                    for j in range(layout.shape[1]):
                        layout[i][j] = Nodelist[((i * 9)+j)].val
                ##print(layout)
                return False, Backtracks
        prevCount = count

###############################################
### Changed general search to handle guesses.
#def searchWithAGuess(Nodelist, layout):
#    Going = True
#    prevCount = 0
#    while Going:
#        for i in range(len(Nodelist)):
#            Nodelist[i].updateConstraints(copy.deepcopy(Nodelist))    
#        count = 0
#        for i in range(len(Nodelist)):
#            if(len(Nodelist[i].possval) == 0):
#                return False
#            if(Nodelist[i].set == True):
#                count += 1
#            elif(len(Nodelist[i].possval) == 1):
#                Nodelist[i].updateValue()
#                count += 1
#        if(count == len(Nodelist)):
#            for i in range(layout.shape[0]):
#                for j in range(layout.shape[1]):
#                    layout[i][j] = Nodelist[((i * 9)+j)].val
#            Going = False
#            return True
#        if(count == prevCount):
#            ##Loop this part
#            temp, worked = BacktrackingSearch(copy.deepcopy(Nodelist), 2, layout)
#            if(worked):
#                Nodelist = temp
#                Going = False
#                return True
#            else:
#                Going = False
#                print("Hit a brick wall.")
#                for i in range(layout.shape[0]):
#                    for j in range(layout.shape[1]):
#                        layout[i][j] = Nodelist[((i * 9)+j)].val
#                return False
#        prevCount = count
#######################################

def BacktrackingSearch(Nodelist,val,layout, Backtracks):
    indexes = []
    Finding = True
    ## By the logic that the val must be one of its possvals.
    ## You probably only need to take one value from the nodelist.
    ## To change this all you need to do is not break after indexes.append(i).
    ## There is no point to remove it, and removing it just makes the program run longer.
    while Finding:        
        for i in range(len(Nodelist)):
            if(len(Nodelist[i].possval) == val):
                indexes.append(i)
                break
        if(val > 9):
            Finding = False
        elif(len(indexes) == 0):
            val += 1
        else:
            Finding = False
    while len(indexes) != 0:
        tempindex = indexes.pop(0)
        for i in range(val):
            save = copy.deepcopy(Nodelist)
            temparr = save[tempindex].possval
            save[tempindex].possval = [temparr[i]]
            save[tempindex].updateValue()
            valid, Backtracks = GeneralSearch(save,layout, Backtracks)
            if(valid):
                return save, True, Backtracks
    return Nodelist, False, Backtracks
    