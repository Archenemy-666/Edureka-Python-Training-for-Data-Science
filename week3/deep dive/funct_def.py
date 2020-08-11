def print_name(str):
    print("Welcome to Python, ",str)
    return()


str=input("Enter your name :")
print_name(str)


def fact(num):
    if num < 0:
        return(0)
    elif num <= 1:
        return(1)
    else:
        fact = 1
        for i in range(1,num+1):
            fact = fact*i
        return(fact)
print(__name__)
