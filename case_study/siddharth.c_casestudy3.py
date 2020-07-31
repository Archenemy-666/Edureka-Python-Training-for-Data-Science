import re 

password = input("enter RefId : ")
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
        print("Valid RefId") 
        break

s = password
x = s.encode('utf-16')
print(x,"refid encoded")
key = int(input("please enter key to get back RefId"))
if(key == 1234):
    y = x.decode('utf-16')
    print("decrypt: ",y)



