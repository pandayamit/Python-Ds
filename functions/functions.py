'''
Functions: Functions in python is a block of statement that perform a specific task. Function have 2 parts. Functions is a reusable components of a code.
1. Function definition -> here we write our logic
2. Function Call => here we invoke our function
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Function syntax <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def fxname():
    ________
    ________
    ________
    ________

'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   Example    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# def hello():         #function definition
#     print("Hello World")
#     print("python functions")

# hello()               #function call


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     Example-2    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#function definition:- herev a, b are called parameters

# def sum(a,b):
#     s=a+b
#     return s

#function call:-here 2,5 are called the arguments 

# ans = sum(2,5)
# print(ans)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Example-3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# def amit(a,b):
#     s=a+b
#     return s
# print(amit(2,8)) 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Example-4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# average of 3 numbers 



# def amit(a,b,c):
#     s=(a+b+c)/3
#     return s
# avg=amit(4,5,10)
# print(avg)    



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Types of Functions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
There are 2 types of functions in Python
1- Built in function ---> ex=> print(), input(), type(), range()
2- User defined function ---> defined by user itself

'''


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lambda Function>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
1) Lambda function in python is used where a minimal task is used to perform like average calculate of numbers etc we don't use it for complex task.

2) Lambda functions are generally used for higher order functions.

3) Higher order functions are those where a functions is defined inside a () or any function return function from itself--> ex return fnx
'''

# ------------------------------------------Example-1---------------------------------------

# sum =lambda a,b:a+b
# print(sum(4,5))

# ------------------------------------------Example-2----------------------------------------

# avg= lambda a,b,c:(a+b+c)/3
# print(avg(3,7,9))

# -------------------------------------Example-3------------------------------------------

# Write a functiom to print a factorial of 'n' numbers.


def cal_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact= fact*i
    return fact
n = int(input("enter any number:"))
print(cal_factorial(n))        
  
