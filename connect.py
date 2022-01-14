import math
import traceback

#The board class, operations include adding counters, and detecting wins
class board():
    
    
    def __init__(self, length, width, board = 0) -> None:
        try:
            self.length = length
            self.width = width
       
            #initializes a 2D integer array that is equivalent to the board
            #integer keys: 0 is unoccupied, 1 is occupied by player 1, and 2 is occupied by player 2, etc... Max 9 players
            #initially sets the board to all 0's
            self.board = [[0 for x in range(length)]for y in range(width)]
            self.gameOver = False

        except Exception as e:
            print(e)

    #adds a counter to the correct column number    
    def addCounter(self, playerNum, colNum):

        #if number is out of range of len(row) give an error and do not allow user to place counter there
        while (colNum >= len(self.board[0])):
            print("Out of range")
            cn = input(f"Player {playerNum} please enter a column")
            colNum = int(cn)
        

        #if all columns are full, then its game over
        isFull = True
        for x in self.board[0]:
            if (self.board[0][x] == 0):
                isFull = False
                break
        
        if isFull == True:
            print("All cells full, the game is a draw!")
            self.endgame()


        #checks if individual column is full. If full, do not allow user to place a counter there
        while (self.board[0][colNum] != 0):
            print("Sorry, this column is full, please choose a different column")
            cn = input(f"Player {playerNum} please enter a column")
            colNum = int(cn)
        

        else:          
            #finds the first cell that is not a 0. We go from the bottom up
            for j in range (len(self.board) - 1, -1, -1):
                print(f"j is {j}")
                if self.board[j][colNum] == 0:
                    
                    self.board[j][colNum] = playerNum
                    break
        
            self.checkWin()


    #checks for a win condition
    def checkWin(self):
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):

                #we check any cell that is occupied by a marker for a "streak". If we find a streak of 4 we win
                if self.board[i][j] != 0:
                    #streak = 1 (passed in the last argument when calling checkStreak)
                    value = self.board[i][j]
                    top_left_diag = self.checkStreak(value, i-1, j-1, 1, iop=-1, jop=-1)
                    if (top_left_diag == True):
                        return True
                    top_right_diag = self.checkStreak(value, i+1, j-1, 1, iop=1, jop=-1)
                    if (top_right_diag == True):
                        return True
                    bot_left_diag = self.checkStreak(value, i-1, j+1, 1, iop=-1, jop=1)
                    if (bot_left_diag == True):
                        return True
                    bot_right_diag = self.checkStreak(value, i+1, j+1, 1, iop=1, jop=1)
                    if (bot_right_diag == True):
                        return True
                    top = self.checkStreak(value, i, j-1, 1, iop=0, jop=-1)
                    if (top == True):
                        return True  
                    bot = self.checkStreak(value, i, j+1, 1, iop=0, jop=1)
                    if (bot == True):
                        return True
                    left = self.checkStreak(value, i-1, j, 1, iop=-1, jop=0)
                    if (left == True):
                        return True
                    right = self.checkStreak(value, i+1, j, 1, iop=1, jop=0)
                    if (right == True):
                        return True

                    

    #We check if the cell in question is equal to the value. If it is, we call checkStreak again in the same direction.
    def checkStreak(self, number, row, col, streak, iop, jop) -> bool: 

        #check for streak length. If streak = 4, we return True and the game is won and we quit the game
        if streak == 4:
            self.printboard()
            print(f"Player {number} wins! GG")
            self.endgame()
            return True

            
        #check for boundary conditions. If out of bounds, we cannot have a streak in the said direction, and we just return false
        elif (row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0])):
            return False

        #If in bounds, and the cell is the same number as the value, then we call the function again in the same direction as before
        elif (self.board[row][col] == number):
            next_i = row + iop
            next_j = col + jop
            streak= streak + 1
            self.checkStreak(number, next_i, next_j, streak, iop, jop)

        #If in bounds, but the value of the cell to check is 0, the streak is broken
        else:
            return False
    
    #ends the game if the game is determined to have been won, or over due to running out of columns
    def endgame(self):
        self.board = [[0 for x in range(len(self.board[0]))]for y in range(len(self.board))]
        print("THANK YOU FOR PLAYING, I HOPE YOU HAD A NICE DAY :D")
        self.gameOver = True
    
    #prints the board
    def printboard(self):
        for row in self.board:
            print(row)

l = input("How many columns do you want your board to be?")
length = int(l)
while (length < 5 or length > 30):
    l = input("Invalid board size, please re-enter a number between 5 and 30 columns")
    length = int(l)

r = input("How many rows do you want your board to be?")
width = int(r)
while (width < 5 or width > 30):
    r = input("Invalid board size, please re-enter a number between 5 and 30 rows")
    length = int(r)

p = input("How many players are playing?")
players = int(p)
while (players < 2 or players > 9):
    p = input("Invalid number of players, please pick between 2 to 9 players")
    players = int(p)

b = board(length, width)
b.printboard

#keeps looping through the turns as long as the game is still going
while b.gameOver == False:

    for x in range(1, players + 1):
        #immediately ends the game if it is declared to be game over
        if b.gameOver == True:
            break
        input1 = input(f"Player {x} please enter the column number you wish to place your counter in. Leftmost column is 0, and rightmost column is {len(b.board[0]) - 1}")
        colNum1 = int(input1)
        b.addCounter(x, colNum1)
        #prints the board at the intermediate stage
        b.printboard()



