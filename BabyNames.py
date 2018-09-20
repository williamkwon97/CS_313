#  File: BabyNames.py

#  Description:  allow a user to query a data base of the 1000 most popular baby names in the United States per decade for the past 11 decades

#  Student Name: William Kwon

#  Student UT EID:  uk669

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/12/18

#  Date Last Modified:


import operator
def main():
    in_file = open("names.txt", "r")
    master_dict= {}


    ranks = []
#making a master dictionary
    for line in in_file:
        name, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = line.split(' ')
        ranks = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
        for i in range(len(ranks)):
            ranks[i] = int(ranks[i])
        master_dict[name] = ranks
    print(master_dict)
    in_file.close()


    # display all the options
    print('Options:')
    print('Enter 1 to search for names.')
    print('Enter 2 to display data for one name.')
    print('Enter 3 to display all names that appear in only one decade.')
    print('Enter 4 to display all names that appear in all decades.')
    print('Enter 5 to display all names that are more popular in every decade.')
    print('Enter 6 to display all names that are less popular in every decade.')
    print('Enter 7 to quit. \n')
    #check user input is valid
    valid=False
    while valid == False:
        try:
            options = int(input("Enter Choice:"))
            if (options < 0 or options > 7):
                print("exit the program because you didn't type between 0-7")
                exit()
        except ValueError:
            print (ValueError)
            exit()
        valid=True


 # search for name and return  highest ranked decade
    if options == 1:
        search = str(input("Enter a name:"))
        if search in master_dict:
            rankings=master_dict[search]
            highest=min(rankings)
            if highest!=0:
              rankings=rankings.index(highest)
            else:
              for i in range(len(rankings)):
                if rankings[i] ==0:
                 rankings[i]=1001


        elif search not in master_dict:
            print (search, "does not appear in any decade")
        dec = 1900 + (10 * rankings)
        print('\nThe matches with their highest ranking decade are: ')
        print(search, dec)
#to display data for one name.
    if options == 2:

        search = str(input("Enter a name:"))

        if search in master_dict:
            rankings = master_dict[search]
            print(search,':',' '.join(str(i) for i in rankings))
            highest = min(rankings)
            if highest != 0:
                for i in range (len(rankings)):
                    print(str(1900 + (i * 10)) + ": " + str(rankings[i]))
            else:
                for i in range(len(rankings)):
                    if (rankings[i] == 0):
                        rankings[i] = 1001
        elif search not in master_dict:
            print("name does not exist.")
#display all names that appear in only one decade.
    if options == 3:

            decade = eval(input('Enter decade: '))

            idx = (decade - 1900) // 10
            nameslist = []
            rankinglist=[]
            for i in master_dict:
                  if (master_dict[i].count(0) == 10) and (master_dict[i][idx] > 0) :
                           nameslist.append(i)
                           rankinglist.append(master_dict[i][idx])
            combine_list=dict(zip(nameslist,rankinglist))
            sortedlistint= sorted(combine_list.items(), key=operator.itemgetter(1))
            print("The names are in order of rank:")
            for x in sortedlistint:
                print (x[0],x[1])
# to display all names that appear in all decades.

    if options == 4:

        nameslist = []
        for i in master_dict:
            if master_dict[i] == 0:
                master_dict[i] = 1001
            if 0 not in master_dict[i]:
                nameslist.append(i)
        nameslist.sort()
        print((len(nameslist)), "names appear in every decade. The names are:")
        for i in nameslist:
            print(i)
#to display all names that are more popular in every decade.
    if options == 5 :
            lenofindex = (len(master_dict[name]) - 1)
            increasing = []
            for names in master_dict:
                count = 0
                for i in range(lenofindex):
                    if master_dict[names][i] > master_dict[names][i + 1]:
                        count+=1
                if count == lenofindex:
                    increasing.append(names)
            increasing.sort()
            print(str(len(increasing)) + " names are more popular in every decade.")
            for i in increasing:
                print(i)
#to display all names that are less popular in every decade.
    if options == 6:

            descreasing = []
            lenofindex=(len(master_dict[name])-1)
            for names in master_dict:
                count = 0
                for i in range(lenofindex):
                    if master_dict[names][i] < master_dict[names][i + 1]:
                        count += 1
                if count == lenofindex:
                    descreasing.append(names)
                if (count == 9) and (master_dict[names][lenofindex] == 0):
                    descreasing.append(names)
            descreasing.sort()
            print(str(len(descreasing)) + " names are less popular in every decade.")
            for i in descreasing:
                print(i)

    if options == 7:
        print('Goodbye.')
        exit()






main()