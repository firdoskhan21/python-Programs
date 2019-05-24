# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:58:09 2019

@author: firdos
"""
class game(Exception):
    pass
while(True):
    try:
        print "Welcome to the rock, paper scissor game....."
        player1=raw_input("enter 1st player name:")
        player2=raw_input("enter 2nd player name:")
        choiceply1=raw_input("which one 1st player want to choose rock, paper or scissor:")
        choiceply2=raw_input("Which one second player want to choose:")
        choice=['rock', 'paper','scissor']
        if choiceply1 in choice and choiceply2 in choice:
            if (choiceply1==choiceply2):
                print ("there a tie , plzz enter unique choices")
            elif (choiceply1=="rock" and choiceply2=="scissor"):
                print ("this round is won by first player")  
            elif (choiceply1=="scissor" and choiceply2=="rock"):
                print ("this round is won by 2nd player")
        
            elif(choiceply1=="scissor" and choiceply2=='paper'):
                print ("this round is won by 1st player")
            elif(choiceply1=="paper" and choiceply2=="scissor"):
                print ("this round is won by 2nd player")
            
            elif(choiceply1=="paper" and choiceply2=="rock"):
                print ("this round is won by 1st player")
            elif(choiceply1=="rock" and choiceply2=="paper"):
                print ("this round is won by 2nd player")
    
            termination=raw_input("Do you want to continue:(y/n)")
            if(termination=="y" or termination=="Y"):
                raise game
        else:
            break
    except game:
        print("plesase try again....")

        
