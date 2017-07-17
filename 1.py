import numpy as np
import itertools
import subprocess as sp

class TicTacToe(object):
   
    def __init__(self):
       self.turn = 0
       self.board = np.zeros((3,3))
       self.won = False
       self.whowon = 0
    
    def playturn (self, row, column):
    	allowed = list(itertools.product(range(3), range(3)))
        
        if (row,column) in allowed and self.board[row,column]==0:
            self.turn +=1
            self.turn %=2
            self.board[row,column] = -1 if self.turn == 0 else 1
            
    def gameOver(self):
        rows = self.board.sum(axis=1)
        columns = self.board.sum(axis=0)
        
        if 3 in list(rows) + list(columns):
            self.won = True
            self.whowon = 1
            
        if -3 in list(rows) + list(columns):
            self.won = True
            self.whowon = -1
        
        if self.board.trace() == 3:
            self.won = True
            self.whowon = 1 

        if self.board.trace() == -3:
            self.won = True
            self.whowon = -1

        reversedArray = np.fliplr(self.board)

        if reversedArray.trace() == -3:
            self.won = True
            self.whowon = -1
        
        if reversedArray.trace() == 3:
            self.won = True
            self.whowon = 1
        
        if np.all(self.board):
            self.won = True
            self.whowon = 2
       
    def printBoard(self):
        
        for x in self.board:
            string = ""
            for y in x:
                if y == 0:
                    string += "_ "
                if y == -1:
                    string += "O "
                if y == 1:
                    string+= "X "
            print string
            
                



    
game1 = TicTacToe()
while(game1.won == False):
    tmp = sp.call('clear',shell=True)
    game1.printBoard()
    if game1.turn == 0:
        player = "1s"
    elif game1.turn == 1:
        player = "2s"
    var1, var2 = raw_input("Player %s turn: " % player).split(",")
    var3 = int(var1)
    var4 = int(var2)
    game1.playturn(var3, var4)
    game1.printBoard()
    game1.gameOver()
if(game1.won == True):
    tmp = sp.call('clear',shell=True)
    game1.printBoard()
    if game1.whowon == 1:
        print("Player 1 wins!")
    elif game1.whowon == -1:
        print("Player 2 wins!")
    elif game1.whowon == 2:
        print("It's a tie!")
