#A Robot moves in a Plane starting from the origin point (0,0). 
# The robot can move toward UP, DOWN, LEFT, RIGHT. 
# The trace of Robot movement is as given following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after directions are steps.  
# Write a program to compute the distanmod2_1.py ce current position after sequence of movements.
# Hint: Use math module.
'''
#starts at origin
from math import sqrt
x = 0 
y = 0 
grid = [x,y]
def up(n):
    grid[1] = grid[1]+n
    return grid

def down(n):
    grid[1] = grid[1]-n
    return grid

def right(n):
    grid[0] = grid[0]+n
    return grid

def left(n):
    grid[0] = grid[0]-n
    return grid

def distance(list):
    dis = sqrt(((list[0])**2)+(list[1])**2)
    print(dis)

print(up(2))
print(down(2))
print(right(5))
print(left(100))
distance(grid)    
'''

 
#Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
# Hint: Use if/elif to deal with conditions
'''
xyzdata = [1,15,2,4]
(xyzdata.sort())
print(xyzdata)

def searching(x):
    for i in xyzdata:
        if (x == i):
            index = xyzdata.index(x)
            print("element %d found at %d"%(x,index))
            break
        else :
            print("cannot be found")

searching(4)

'''

#Weather forecasting organization wants to show is it day or night. 
# So, write a program for such organization to findwhether is it dark outside or not.
# Hint: Use time module.
'''
import datetime
from datetime import time
x = datetime.datetime.now()
#x = time(hour = 5)
print(x.hour)
ampm = x.strftime("%p")
hour1 = x.strftime("%H")
type(hour1)
hour2=int(hour1)
if(hour2 >= 7):
    print("night")
elif(0 <= hour2 <=3 ):
    print("night")
else:
    print("morning")

'''

#Write a program to find distancebetween two locations when their latitude and longitudes are given.
# Hint: Use math module.
'''
import math 
x1 = int(input("latitude1: "))
y1 = int(input("longitude1: "))
x2 = int(input("latitude2: "))
y2 = int(input("longitude2: "))
location1 = {'latitude':x1 ,'longitude':y1}
location2 = {'latitude':x2 ,'longitude':y2}

lat1 = location1['latitude']
lat2 = location2['latitude']

lon1 = location1['longitude']
lon2 = location2['longitude']
distance = math.sqrt(((lat2-lat1)**2)+((lon2-lon1)**2))
print(distance)
'''

#NOT COMPLETE
#Design a software for bank system.
#  There should be options like cash withdraw, 
# cash credit and change password. According to user input, 
# the software should provide required output.
# Hint: Use if else statements and functions.
'''


class Bankaccount():
    def __init__(self):
        self.balence = 0
        self.password = 1234
        print("bank account")  
    def credit(self):
        amount = float(input("credit amount"))
        self.balence = self.balence + amount
        print("amount credited : ",amount)
    def debit(self):
        amount = float(input("debit amount: "))
        if (self.balence > amount): 
            self.balence = self.balence - amount
            print("amount debited : ",amount)
        else : print("you can only withdraw : ",self.balence)
    def display(self):
        print("the remaining amount is :",self.balence)
    
    def change_password(self):
        phonecheck = int(input("your phone number : "))
        if phonecheck == 9949039788 :
            newpass = int(input("please enter new password : "))
            self.password = newpass
            return ('next')
        else : print("wrong") 
            
    def check_password(self):
        x = int(input("enter password : "))
        print(self.password)
        if x == self.password:
            return ('next')
        else :
            self.change_password()


s = Bankaccount()
s.check_password()
m = print(s.check_password())
if m == 'next':
    print("welcome s you can access your bank account")
    print("the amount in your bank",  s.display())
    s.debit()
    s.credit()
else : print("access denied")
'''

# Write a program which will find all such numbers which are divisible by 7 
# but are not a multiple of 5, 
# between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
list1 = []
for i in range(2000,3201):
    if (i%7 == 0) and (i%5 != 0):
        list1.append(i)
        x = ','.join(map(str,list1))
        print(x)
'''
#Write a program which can compute the factorial of a given numbers. Use recursion to find it. 
'''
number = int(input("fact of nmber : "))
x = 1
for i in range(1,number+1):
    x = x*i
print(x)
'''

#Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D  is  the  variable  whose  values  should  be  input  to  your  program 
# in  a  comma-separated sequence.
'''
from math import sqrt
d = [int(x) for x  in input("enter numbers : ").split(',')]
k = ','.join(map(str,d))
print(k)
l=[]
for i in d: 
    x = (sqrt((2*50*i)/30)) 
    z = int(x)
    l.append(z)
print(','.join(map(str,l)))
'''

#NOT COMPLETE
#Write a program which takes 2 digits,
#  X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡-Y-1


#Write a program that accepts a comma separated sequence 
# of words as input and prints the words in a comma-separated
#  sequence after sorting them alphabetically.
'''
x = input()
v = x.split(',')
x = sorted(v)
print(','.join(map(str,x)))
'''
#Write a program that accepts sequence of lines as 
# input and prints the lines after making all characters
#  in the sentence capitalized. Suppose the 
# following inputis supplied to the program:
'''
string1 = input()
y = string1.upper()
print(y)
'''

#Write a program that accepts a sequence of whitespace separated 
# words as input and   prints   the   words   after   removing   
# all   duplicate   words   and   sorting   them alphanumerically.
'''
passage = input("enter messasge")
y = passage.split()
x = sorted(y)
print(' '.join(map(str,x)))
'''
#Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit 
#  binary numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not. 
#  The numbers that are divisible by 5 are to be printed in a comma separated sequence.
''''
x = (input("enter binary only"))
map(int,x)
print(x)
y = x.split(',')
print(y)
for i in range(0,len(y)):
    y[i] = int(y[i])
print(y)    
z=[]
for k in y :
    if(k%5 == 0):
        z.append(k)
    else :
        continue
    print(z)
'''
#Write  a  program  that  accepts  a  sentence  and  calculate 
#  the  number  of  upper  case letters and lower case letters.
'''
x = input()
print(x)
countu = 0
countl = 0
spaces = 0
for i in x:
    if(i == ' '):
        spaces = spaces + 1
    elif(i == i.upper()):
        countu = countu + 1
    elif(i == i.lower()):
        countl = countl + 1
print("upper cases ",countu)
print("lower cases",countl)
print("spaces count",spaces)
'''
#Give example of fsum and sum function of math library.
'''
import math 
x = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,]
print(sum(x))
print(math.fsum(x))
'''