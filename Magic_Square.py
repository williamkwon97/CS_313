'''
  File: MagicSquare.py

  Description:Generate Magic Square

  Student's Name: William Kwon

  Student's UT EID: uk 669
 
  Partner's Name: n/a

  Partner's UT EID: n/a

  Course Name: CS 313E 

  Unique Number: 51350

  Date Created: 9/3/18

  Date Last Modified: 9/7/18
'''

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
import itertools
def make_square(n):
 
      # generate 2D
    magic_square = [[0 for a in range(n)]for b in range(n)]
 
    # inital position c= column and r=row
    c = n/2
    r = n-1    
    magic_square[c][r]=1
    count = 2
    while count <= (n**2):
        #moving one right and down
        r=r+1
        c=c+1
        #1st condition if it at very right and down coner
        if  c==n and r== n:
            r=r-2
            c=c-1
        # 2nd condition if goes beyong column but not row
        if c == n and r <n:
            c = 0
            r
        # 3rd condition if goes beyong row but not column
        if r ==n and c<n: 
            r = 0
        # 4th condition if there is number inside of grid
        if magic_square[c][r] !=0:
            r=r-2
            c=c-1

      
        magic_square[c][r]=count
        count+=1
        
        
    return magic_square
# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any ue
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
  
  
  lengthMS=len(magic_square)
  for r in range(0,lengthMS):
      for c in range(0,lengthMS):
     
        print '%4d' % (magic_square[c][r]),
      print
# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True

def check_square ( magic_square ):
  n=len(magic_square)
  print "This is a magic square and the canonical sum is" ,n*(n*n+1)/2
  #check the sum of column
  lenghtMS = len(magic_square[0])
  sum_col =0
  for c in range(0,n):
    sum_col =0
    for r in range(lenghtMS):
      sum_col += magic_square[r][c]
    if (sum_col !=n*(n*n+1)/2):
      return False and "This is not a magic square"
  #check the sum of row
  sum_row=0
  for c in range(0,n):
    sum_row=0
    for r in range(0,n):
      sum_row+=magic_square[r][c]
    if (sum_col !=n*(n*n+1)/2):
      return False and "This is not a magic square"
    

  #check the sum of diagonal
  sum_dig=sum([ magic_square[i][i] for i in range(len(magic_square))])
  if (sum_dig !=n*(n*n+1)/2):
    return False and "This is not a magic square"
  #check the sum of another diagonal
  sum_dig2=sum([ magic_square[len(magic_square)-i-1][i] for i in range(len(magic_square))])
  if (sum_dig2 !=n*(n*n+1)/2):
    return False and "This is not a magic square"
  return True
  
 # Check the user input

  # Create the magic square

  # Print the magic square

  # Verify that it is a magic square

  
def main():
  # Prompt the user to enter an odd number 1 or greater
  option=int(raw_input("Please enter an odd number:"))
      
  while (n % 2 == 0 or n<1 ):

       n = int(raw_input("Please enter an odd number:"))
  # Create the magic square
  magic_square=make_square(n)
  print "Here is a "+str(n)+" x "+str(n)+" magic square:"+"\n"
  # Print the magic square
  print_square ( magic_square )

  # Verify that it is a magic squar
  check_square(magic_square)
if __name__ == "__main__":
  main()
  # This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
# Prompt the user to enter an odd number 1 or greater

 