#  File: Boxes.py

#  Description: nesting boxes

#  Student Name: William Kwon

#  Student UT EID: uk669

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created:10/14/18

#  Date Last Modified: 10/19/18

def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])
def check_list(a):
    nest_box= True
    for i in range(len(a)-1):
        nest_box = does_fit(a[i],a[i+1])
        if (nest_box == False):
            return nest_box
    return  nest_box
def sub_sets (a, b,bigger, lo):
  hi = len (a)
  if (lo == hi):
    if (len(b)>=2):
        bigger.append(b)
  else:
    c = b[:]
    b.append (a[lo])
    if(check_list(b)):
        sub_sets (a, b, bigger, lo + 1)
    if(check_list(c)):
        sub_sets (a, c, bigger,lo + 1)
    else:
        lo +=1
def check_biggest(bigger):
    b=0
    for i in range(len(bigger)):
        if(len(bigger[i])>b):
            b =len(bigger[i])
    for i in range(len(bigger)):
        if(len(bigger[i])==b):
            for j in range(len(bigger[i])):
                print (bigger[i][j] , end= '\n')
            print()
    return

def main():

    in_file = open('boxes.txt', 'r')


    line = in_file.readline()
    line = line.strip()
    num_boxes = int(line)

    box_list = []

    for i in range(num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for i in range(len(box)):
            box[i] = int(box[i])
        box.sort()
        box_list.append(box)

    box_list.sort()

    list = []
    biggest = []

    sub_sets(box_list, list, biggest, 0)
    if (len(biggest) == 0):
        print('No Nesting Boxes')
    else:
        print('Largest Subset of Nesting Boxes')
        check_biggest(biggest)

    # close the file
    in_file.close()


main()