
#What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))

#What will be the output?
d ={"john":40, "peter":45}
print(list(d.keys()))

#A website requires a user to input username and password to register. Write a program
#to check the validity of password given by user. Following are the criteria for checking password:
#1. At least 1 letter between [a-z]
# 2.At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
import re 
password = input("enter password : ")
while True:   
    if (len(password)<6 and len(password)>12): 
        print("get hold of your limits")
        break
    elif not re.search("[a-z]", password): 
        print("dont you get it include lowercase")
        break
    elif not re.search("[0-9]", password): 
        print("eehhhh!!! numbers please")
        break
    elif not re.search("[A-Z]", password): 
        print("hey man i need an uppercase too")
        break
    elif not re.search("[_@$]", password): 
        print("dont make me swear use the symbols")
        break
    else: 
        print("Valid Password") 
        break

#Write a for loop that prints all elements of a list and their position in the list.a = [4,7,3,2,5,9]
list = [4,7,3,2,5,9]
value = 0 
for i in list:
    print(i,value)
    value = value+1

#Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.
string = input()
print(string[::2])


#Please write a program which accepts a string from console and print it in reverse order.
newstuff = input()
print(newstuff[::-1])

#Please write a program which count and print the numbers of each character in a string input by console.
counting_char = input()
sub_string=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in sub_string:
    count =  counting_char.count(i)
    if (count >= 1):
        c = count
        print(i,c)

#With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
#    write   a program to make a list whose elements are intersection of the above given lists.
list1 = [1,3,6,78,35,55]
list2= [12,24,35,24,88,120,155]
print(list(set(list1) & set(list2)))

#By usinglist comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
list1 = [12,24,35,24,88,120,155]
list1.remove(24)
print(list1)
list2 = list1
list2.remove(24)
print(list2)


#By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
listc = [12,24,35,70,88,120,155]
for i in listc:
    if i == 12 or 88 or 120:
     listc.remove(i)
    print(listc) 

#By using list comprehension, please write a program to print the list after removing delete 
# numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
listd = [12,24,35,70,88,120,155]
def removeele(listd):
    for i in listd:
        if (i%5 ==0) or (i % 7 == 0):
            listd.remove(i)
    print(listd)
removeele(listd)
for i in listd :
    if (i%5 == 0) or (i % 7 == 0):
        removeele(listd)
    print(listd)

#Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).

def idk(n):
    t = 0.0
    for i in range(1,n+1):
     print(i)
     x = i+1
     y = i/x
     print(y)
     print(t)
     t = t + y
     print(t)
idk(5) 


    




        


