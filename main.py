# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 09:23:27 2021

@author: Brandon
"""

from Node import Node
import numpy as np
import re
import time
from Backtracking import GeneralSearch

def startProgram(text):
    # I would recommend just changing the input file.
    # Could have done a user input txt, but it seemed like a bad idea.
    filename = "Puzzles/" + text
    try:
        file = open(filename)
    except:
        ## Default open if file does not exist.
        file = open('Puzzles/Sudoku2-5star.txt')
        #file = open('Puzzles/Sudoku1Expert.txt')
        #file = open('Textbookpuzzle.txt')
        #file = open('Blankpuzzle.txt')
        #file = open('illegal.txt')
        ###file = open('input.txt')
    layout = np.zeros((9,9),dtype=int)
    curr = file.readlines()
    ### File should not be needed anymore.
    file.close()
    nums = []
    ## This is all the leniency I will give for file input
    ## Will make note of this in the write-up
    for n in range(len(curr)):
        nums.append(re.sub("[\n\s,]", "", curr[n]))
    ##print(nums)
    Nodelist = []
    invalid = False
    for i in range(9):
        for j in range(9):
            try:
                layout[i][j] = nums[i][j]
            except:
                invalid = True
                break
            ## to reference we will use Nodelist[((i * 9)+j)]
            Nodelist.append((Node(int(nums[i][j]),[i,j])))
            Nodelist[((i * 9)+j)].setState()
        if(invalid):
            ## Just to break out of the second loop.
            break
    ###Starting layout
    if(invalid == False):
        print(layout)
        print()
        ##print(Nodelist)
        backtracks = 0
        startTime = time.time()
        valid, backtracks = GeneralSearch(Nodelist,layout, backtracks)
        totalTime = time.time() - startTime
        if(valid):
            print()
            print(layout)
            print("Solution Found.")
            print("Took", totalTime, "seconds and")
            print(backtracks, "calls to backtrack/take a guess.")
        else:
            print("Failure")
            print("Either your puzzle is unsolvable or my program has bugs.")
    else:
        print("File is not valid for this program.")

def BeginFileInput():
    while True:
        print("Give the program an input file inside the Puzzles folder.")
        print("If the file can't be found it will be a default file.")
        print("If you want to quit just type Q or q")
        inputString = str(input("Puzzles/:"))
        if(inputString == "Q" or inputString == "q"):
            print("Thank you for using this sudoku solver.")
            break
        else:
            startProgram(inputString)
            print("\n")
            print("Would you like to solve another puzzle?")
            answer = str(input("y / ~n :"))
            if(answer == "Y" or answer == "y"):
                continue
            else:
                print("Thank you for using this sudoku solver.")
                break
        
BeginFileInput()