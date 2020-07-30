#Write a program which will find factors of given number and find whether the factor is even or odd.
def fatorization_of(x):
    print("list : ")
    for i in range(1, x+1):
        if x % i == 0:
            print(i," : is a factor")
        else:
            print(i," : is not the factor\n\n")

num = 10

fatorization_of(num)

#case2 Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically. 
list = []
no_of_inputs = int(input("no of inputs: "))
for i in range(0,no_of_inputs):
    list.append(input("give strings: "))

list.sort()
print(list,"\n\n")

#Write a program, whichwill find all the numbers between 1000 and 3000 (both included) 
#such that each digit of a number is an even number. The numbers obtained should be printed 
#in a comma separated sequence on a single line.


i = 1000
for i in range(1000,3001):
    v = str(i)
    a = v[0]
    b = v[1]
    c = v[2]
    d = v[3]
    l = int(a)
    m = int(b)
    n = int(c)
    o = int(d)
    
    if((l%2==0) and (m%2==0) and (n%2==0) and (o%2==0) ):
        print(i)
    

#Write a program that accepts a sentence and calculate the number of letters and digits.
x = input()
counta = 0
counti = 0
for i in x:
    if i.isalpha():
        counta = counta + 1
    elif i.isdigit():
        counti = counti + 1
    else:
        print("not recognized")

print("number : ",counti, "alphabets",counta)


def pallindrome(x):
    if (x == x[::-1]):
        print("pallindrome")
    else : (" not ")

pallindrome("dud")

