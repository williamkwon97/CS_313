#  File: Triangle.py

#  Description: look for the greatest path sum

#  Student's Name:

#  Student's UT EID:

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:
import timeit


# returns the greatest path sum using exhaustive search
highest=0
import timeit
def brute_force (r,c,sum1,grid):
  if (len(grid)-1 <r):
      global highest
      if highest < sum1:
          highest=sum1
  else:
      sum1+= grid[r][c]
      return  brute_force(r+1,c,sum1,grid) or brute_force(r+1,c+1,sum1,grid)

# returns the greatest path sum using greedy approach
#def greedy (grid):
 # return

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid,r,idx):
    if(r==(len(grid)-1)):
        return grid[r][idx]
    else:
        return grid[r][idx] + max((divide_conquer(grid,r+1,idx),divide_conquer(grid,r+1,idx+1)))


# returns the greatest path sum and the new grid using dynamic programming

#def dynamic_prog (grid):
#  return

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    grid = []
    in_file = open('triangle.txt', 'r')
    line = in_file.readline()
    line = line.strip()
    num = int(line)

    for i in range(num):
        line = in_file.readline()
        line = line.strip()
        num_list = line.split()
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        grid.append(num_list)
    return grid

def main ():
  # read triangular grid from file
  grid=read_file()



  # output greatest path from exhaustive search
  sum1=0
  brute_force(0,0,sum1,grid)
  print("The greatest path sum through exhaustive search is ",highest)
  time1 = timeit.timeit(
      setup="from __main__ import brute_force",  # Import my_fn so timeit can use it
      stmt="brute_force(0,0,sum1,grid)",  # The statement to be timed
      number=1,  # Number of times it should be executed
      globals=locals()  # Gives timeit access to the local vars of the main function
  )

  print(time1)
  divide_conquer(grid,0,0)
  print("The greatest path sum through divide and conquer is ", divide_conquer(grid,0,0))
  time2 = timeit.timeit(
      setup="from __main__ import divide_conquer",  # Import my_fn so timeit can use it
      stmt="divide_conquer(grid,0,0)",  # The statement to be timed
      number=1,  # Number of times it should be executed
      globals=locals()  # Gives timeit access to the local vars of the main function
  )
  print(time2)
  # print time taken using exhaustive search
'''
  # output greatest path from greedy approach
  times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming
  times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
  times = times / 10

  
  print('The greatest path sum through exhaustive search is ' + str(exhaustive_search(triangle)) + '.')

  print('The greatest path sum through greedy search is ' + str(greedy(triangle)) + '.')

  print('The greatest path sum through recursive search is ' + str(rec_search(triangle)) + '.')

  print('The greatest path sum through dynamic programming is ' + str(dynamic_prog(triangle)) + '.')
'''

if __name__ == "__main__":
  main()