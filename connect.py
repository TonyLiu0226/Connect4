import math
import traceback

#The board class, operations include adding counters, and detecting wins
class board():
    
    
    def __init__(self, length, width, board = 0) -> None:
        try:
            self.length = length
            self.width = width

            if (self.length < 5 or self.width < 5):
                raise Exception("Size is not big enough")
       
            #initializes a 2D integer array that is equivalent to the board
            #integer keys: 0 is unoccupied, 1 is occupied by player 1, and 2 is occupied by player 2
            #initially sets the board to all 0's
            self.board = [[0 for x in range(length)]for y in range(width)]
        except Exception as e:
            print(e)

    #adds a counter to the correct column number    
    def addCounter(self, playerNum, colNum):
        #checks if column is full. If full, do not allow user to place a counter there
        if (self.board[0][colNum] != 0):
            print("Sorry, this column is full, please choose a different column")
            cn = input(f"Player {playerNum} please enter a column")
            self.addCounter(self, playerNum, int(cn))

        else:          
            #finds the first cell that is not a 0. We go from the bottom up
            for j in range (len(self.board) - 1, -1, -1):
                print(f"j is {j}")
                if self.board[j][colNum] == 0:
                    
                    self.board[j][colNum] = playerNum
                    break
        
            print(self.board)
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
                    top_right_diag = self.checkStreak(value, i+1, j-1, 1, iop=1, jop=-1)
                    bot_left_diag = self.checkStreak(value, i-1, j+1, 1, iop=-1, jop=1)
                    bot_right_diag = self.checkStreak(value, i+1, j+1, 1, iop=1, jop=1)
                    top = self.checkStreak(value, i, j-1, 1, iop=0, jop=-1)
                    bot = self.checkStreak(value, i, j+1, 1, iop=0, jop=1)
                    left = self.checkStreak(value, i-1, j, 1, iop=-1, jop=0)
                    right = self.checkStreak(value, i+1, j, 1, iop=1, jop=0)

                    

    #We check if the cell in question is equal to the value. If it is, we call checkStreak again in the same direction.
    def checkStreak(self, number, row, col, streak, iop, jop) -> bool: 
        #prints out all values in the parameter
        print(f"number to check: {number}, i: {row}, j: {col}, streak: {streak}. i will be incremented by {iop} and j will be incremented by {jop}")

        #check for streak length. If streak = 4, we return True and the game is won and we quit the game
        if streak == 4:
            print(f"Player {number} wins! GG")
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

b = board(19, 5)
print(b.board)
b.addCounter(1, 5)
b.addCounter(1, 3)
b.addCounter(2, 4)
b.addCounter(1, 4)
b.addCounter(2, 2)
b.addCounter(1, 5)
b.addCounter(2, 3)
b.addCounter(1, 5)
b.addCounter(2, 5)
b.addCounter(1, 18)
b.addCounter(2, 4)
