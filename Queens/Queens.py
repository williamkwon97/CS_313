
# Solution to the 8 Queens Problem
#  File: Queens.py

#  Description: how can we place queens that no queen can capture another.

#  Student Name:William Kwon

#  Student UT EID:uk669

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:31350

#  Date Created:10/27/18

#  Date Last Modified:10/29/18
class EightQueens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    self.sols=0
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # check if no queen captures another
  def isValid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        rowDiff = abs (row - i)
        colDiff = abs (col - j)
        if (rowDiff == colDiff) and (self.board[i][j] == 'Q'):
          return False
    return True

  def recursiveSolve (self, col):
    if (col == self.n):
      self.printBoard()
      print()
      self.sols+=1
    else:
      for i in range (self.n):
        if (self.isValid (i, col)):
          self.board[i][col] = 'Q'
          if (self.recursiveSolve (col + 1)):
            return True
          self.board[i][col] = '*'
      return False

  # solve the problem
  def solve (self):
        self.recursiveSolve(0)
        self.printthesolutions()

  # print the board
  def printBoard (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ' )
      print ()
  def printthesolutions(self):
      print('There are total', self.sols,"solutions for a ", self.n ,'*', self.n,'board.')

def main():
  # create object
  userinput=0
  while (userinput <1  or userinput> 8):
      userinput = int(input("Enter the size of board: "))

  queens = EightQueens (userinput)
  queens.solve()
  userinput=0


main()