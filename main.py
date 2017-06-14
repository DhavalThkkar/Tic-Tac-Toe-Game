#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:57:45 2017

@author: thakkar_
"""
def init():
    global player1
    global player2
    global list_numbers
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1 = input("Enter the name of Player 1:")
    player2 = input("Enter the name of Player 2 :")
    print("\n\nWelcome {} and {} to the game of Tic Tac Toe\n".format(player1,player2))
        # Starting Layout
    print("""This is the representation for choosing the column where you need to fill 'X' or 'O'
          _{}_|_{}_|_{}_      
          _{}_|_{}_|_{}_
           {} | {} | {} 
          """.format(*list_numbers))
    print("Here 'X' is assigned for {} and 'O' is assigned for {}".format(player1,player2))
    
def start():
    p1_count = 0
    p2_count = 0
    if (p1_count % 2 != 0 and p1_count == 1):
        input("\n{} Choose a number from the Grid to replace with 'X' ".format(player1))
        p1_count += 1
    else:
        input("\n{} Choose a number from the Grid to replace with 'O' ".format(player2))
        p2_count += 1
        
def win():
    pass
    
    
# Main Function
if __name__ == "__main__":
    init()
    start()