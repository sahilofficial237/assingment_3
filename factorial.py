#taking input from the user
num=int(input("enter a number:"))

#factorial code below
def factorial(num):
    if (num<=1):
        return 1
    else:
        return num*(factorial(num-1))
result=factorial(num)
print(result)