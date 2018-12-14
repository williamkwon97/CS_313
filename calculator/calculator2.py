import math
import statistics
import itertools

# Description: calulator for lazy people who need to online HW
# You can always modified the code to caculate diffeernt stuff
# How to use this Caclulator
#1.Just copy and paste the numbers from the problem
#2 emove Hashtag if you want to use that specific function
# For example you copy the list of numbers with comma init than instead of add comma one by one use a=a.replace.
# a is list and b is list 2 so you can calculate convariance of coffiencent of variation
a = '0 5 10 '
#a = a.replace(',', '')

a=a.split()
a=sorted(a) #use when you want sort by ascending order for a

b= " 0  5 10  15 	"
b=b.split()
c="0.01	0.06	0.02	0.10 0.04	0.15	0.20	0.10 0.01	0.15	0.15	0.01 "
c=c.split()

d="0.01	0.06	0.02	0.10"
d=d.split()
f="0.04	0.15	0.20	0.10"
f=f.split()
g="0.01	0.15	0.15	0.01"
g=g.split()
e="0.00 0.01 0.05  0.06"
e=e.split()


list=[float(i) for i in a]
list2=[float(i) for i in b]
list3=[float(i) for i in c]

list4=[float(i) for i in d]
list5=[float(i) for i in f]
list6=[float(i) for i in g]
list7=[float(i) for i in e]
list=sorted(list)
list2=sorted(list2)
     #Standard deviation second Rule            #print this when you want range of b         #print this when you want mode for b
newlista=[]
newlistb=[]
s=[]
print(list3)
for i in list:
    for y in list2:
        s.append(i*y)

expectsumdiff=[s*list3 for s,list3 in zip(s,list3)]
print((expectsumdiff))
expectofx=5*sum(list5)+10*sum(list6)
expectofy=5*.36+10*.37+15*.21
print(sum(expectsumdiff)-(expectofx*expectofy))
print((sum(expectsumdiff)-(expectofx*expectofy))/(math.sqrt(expectofx)*math.sqrt(expectofy)))

'''
for i in list:
    newlistb.append(10*i-3)
list=(newlistb)
print(list)
for i in list:
    newlista.append(i**2)
'''

expectsum=[list*list2 for list,list2 in zip(list,list2)]
expectsum1=[newlista*list2 for newlista,list2 in zip(newlista,list2)]


expectsum=sum(expectsum)
expectsum1=sum(expectsum1)
var=expectsum1-expectsum**2



#print(sum(expectsum),sum(expectsum1),sum(expectsum1)-sum(expectsum)**2)





#print(stdev,var)
#print(newlistb)

#credit William Kwon'''