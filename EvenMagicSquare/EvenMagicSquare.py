#  File: EvenMagicSquare.py

#  Description: create even magic square

#  Student Name:William Kwon

#  Student UT EID: uk669

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created:10/22/18

#  Date Last Modified:10/24/18
d=dict()
def permute (a, lo):


     hi = len(a)

     #d = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [])


     if (lo == hi):
         if check_square(a) is True:


            n= 1
            while n in d.keys():
                n+=1

            d[n]=a[:]

            if n==10:
              return d

     elif (lo==4):

         SR1 = (sum(a[0:4]))

         if SR1==34:
             for i in range(lo, hi):
                 a[lo], a[i] = a[i], a[lo]

                 ret=permute(a, lo + 1)
                 if ret is not None:
                     return ret
                 a[lo], a[i] = a[i], a[lo]


         elif SR1 !=34:
             pass
             #function end

     elif lo==8:

         SR2 = sum(a[4:8])
         if SR2==34:
             for i in range(lo, hi):
                 a[lo], a[i] = a[i], a[lo]
                 ret = permute(a, lo + 1)
                 if ret is not None:
                     return ret
                 a[lo], a[i] = a[i], a[lo]


         elif SR2 !=34:
             pass


     elif lo==12:
             SR3 = sum(a[8:12])
             if SR3==34:
                 for i in range(lo, hi):
                     a[lo], a[i] = a[i], a[lo]
                     ret = permute(a, lo + 1)
                     if ret is not None:
                         return ret
                     a[lo], a[i] = a[i], a[lo]


             elif SR3!=34:
                 pass
     elif lo==16:
            SR4 = sum(a[12:16])
            if SR4 == 34:
                for i in range(lo, hi):
                    a[lo], a[i] = a[i], a[lo]
                    ret = permute(a, lo + 1)
                    if ret is not None:
                        return ret
                    a[lo], a[i] = a[i], a[lo]


            elif SR4 != 34:
                pass


     else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            ret = permute(a, lo + 1)
            if ret is not None:
                return ret
            a[lo], a[i] = a[i], a[lo]




def make_square():
  

    magic_square= list(range(1,17))
    return magic_square



def check_square(a):
    CS1 = sum(a[0::4])
    if CS1 == 34:
        CS2 = sum(a[1::4])
        if CS2 == 34:
            CS3 = sum(a[2::4])
            if CS3 == 34:
                CS4 = sum(a[3::4])
                if CS4 == 34:
                    D1 = (a[0] + a[5] + a[10] + a[15])
                    if D1 == 34:
                        D2 = (a[3] + a[6] + a[9] + a[12])
                        if D2 == 34:
                            return True
    return False


def print_square(a):
    cols = 4
    rows = 4
    magic_square=[a[x:x + cols] for x in range(0, len(a), cols)][:rows]
    for r in range(0,len(magic_square)):
        for c in range(0,len(magic_square)):
            print ('%4d' %  (magic_square[r][c]),end=' ')
        print()

def main():



    #n = int(input("Please enter an odd number:"))

    magic_square = make_square()


    d=permute(magic_square,0)
    print(d)
    num_ms=int(input("Enter number of magic squares (1 - 10): ")+'\n')

    if num_ms==1:
        print_square(d[1])
    if num_ms==2:
        print_square(d[1])
        print('\n')
        print_square(d[2])
    if num_ms==3:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
    if num_ms==4:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
        print('\n')
        print_square(d[4])

    if num_ms==5:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
        print('\n')
        print_square(d[4])
        print('\n')
        print_square(d[5])
    if num_ms==6:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
        print('\n')
        print_square(d[4])
        print('\n')
        print_square(d[5])
        print('\n')
        print_square(d[6])
    if num_ms==7:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
        print('\n')
        print_square(d[4])
        print('\n')
        print_square(d[5])
        print('\n')
        print_square(d[6])
        print('\n')
        print_square(d[7])
    if num_ms==8:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
        print('\n')
        print_square(d[4])
        print('\n')
        print_square(d[5])
        print('\n')
        print_square(d[6])
        print('\n')
        print_square(d[7])
        print('\n')
        print_square(d[8])
    if num_ms==9:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
        print('\n')
        print_square(d[4])
        print('\n')
        print_square(d[5])
        print('\n')
        print_square(d[6])
        print('\n')
        print_square(d[7])
        print('\n')
        print_square(d[8])
        print('\n')
        print_square(d[9])
    if num_ms==10:
        print_square(d[1])
        print('\n')
        print_square(d[2])
        print('\n')
        print_square(d[3])
        print('\n')
        print_square(d[4])
        print('\n')
        print_square(d[5])
        print('\n')
        print_square(d[6])
        print('\n')
        print_square(d[7])
        print('\n')
        print_square(d[8])
        print('\n')
        print_square(d[9])
        print('\n')
        print_square(d[10])


    #print_square(magic_square)




main()