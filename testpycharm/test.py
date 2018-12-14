#  File: Triangle.py

#  Description: Print all the times and different algorithims

#  Student's Name: Ebrahim Haji

#  Student's UT EID: eah3345

#  Partner's Name: - 

#  Partner's UT EID: - 

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 03/09/2018

#  Date Last Modified: 03/09/2018

import time

# returns the greatest path sum using exhaustive search
max_ = 0
def exhaustive_search(row, col, grid, sum_):
  if (len(grid) - 1 < row):
    global max_
    if max_ < sum_:
      max_ = sum_
  else:
    sum_ += grid[row][col]
    return exhaustive_search(row + 1, col, grid, sum_), exhaustive_search(row + 1, col + 1, grid, sum_)
  

# returns the greatest path sum using greedy approach
def greedy (grid):
  _sum = grid[0][0]
  initial_max = 0
  for row in range(0, len(grid) - 1):
    _max = max(grid[row + 1][initial_max] , grid[row + 1][initial_max + 1])
    move_along = grid[row + 1].index(_max)
    if move_along > initial_max:
     initial_max = move_along
    _sum += _max
  return _sum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid, row, index):
  if (row == (len(grid) - 1)):
    return grid[row][index]
  else:
    return grid[row][index] + max((rec_search(grid, row + 1, index)), (rec_search(grid, row + 1, index + 1)))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid_):
  grid = grid_
  for row in range(len(grid) - 1, 0, -1):
    for column in range(0, len(grid[row]) - 1):
      _max = max(grid[row][column] , grid[row][column + 1])
      grid[row - 1][column] = grid[row - 1][column] + _max
  return (grid, grid[0][0])
      
      

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  _list = []
  in_file = open('triangle.txt', 'r')
  line = in_file.readline()
  line = line.strip()
  num_ = int(line)
  
  for i in range(num_):
    line = in_file.readline()
    line = line.strip()
    num_list = line.split()
    for i in range(len(num_list)):
      num_list[i] = int(num_list[i])
    _list.append(num_list)
  return _list 

def main():
  
  _list = read_file()

  ti = time.time()
  # output greates path from exhaustive search
  sum_ = 0
  exhaustive_search(0,0,_list, sum_)
  print("The greatest path sum through exhaustive search is", max_)
  tf = time.time()
  del_t = tf - ti
  # print time taken using exhaustive search
  print('The time taken for exhaustive search is', round(del_t, 10) , 'seconds\n')
  
  ti = time.time()
  # output greates path from greedy approach
  print("The greatest path sum through greedy is", greedy(_list))
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach
  print('The time taken for greedy is', round(del_t, 10) , 'seconds\n')
  
  ti = time.time()
  # output greates path from divide-and-conquer approach
  print("The greatest path sum through divide-and-conquer is",rec_search(_list, 0 , 0))
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach
  print('The time taken for divide-and-conquer is', round(del_t, 10) , 'seconds\n')
  
  ti = time.time()
  # output greates path from dynamic programming
  _dynamic = dynamic_prog(_list)
  print("The greatest path sum through dynamic is",_dynamic[0][0])
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming
  print('The time taken for dynamic is', round(del_t, 10) , 'seconds')

if __name__ == "__main__":
  main()



















