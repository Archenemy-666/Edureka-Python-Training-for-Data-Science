grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))
print(enumerateGrocery)
# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

str1 = "hello how are yo"
list1 = str1.split()
enustr = enumerate(list1)
list(enustr)

lis1 = list(range(0,11))
even_vals = (lambda x: x%2 == 0)
odd_vals = (lambda x : x%2 != 0)
mul_7 = (lambda t : t % 7 == 0)

print(list(filter(even_vals,list(range(1,36)))))
