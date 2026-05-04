print(".....For Loop.....")

# For Loop: for loop is used for the sequential traversal like in  strings array etc...

# in => in is a membership operator. and it is used to check the presence of a value or variable.It can be used both conditionals and loops. 


                      # Example for in inside conditionals

# string="hello"
# if "l" in string:
#     print("l exists in string")
# else:
#     print("l does'nt exists in string")




# for loop examples

# example-1
# string="Amit"
# for i in string:
#     print(i)


# example-2: range-(0 to n-1)

# for i in range(5):
#     print(i+1)

# for i in range(6):
#     print("Hello World")


# Example-3: find the total numbers of "i" in given phrase

# phrase="Artificial intelligence"
# count=0
# for ch in phrase:
#     if(ch=="i"):
#         count+=1
# print("count of i=",count)        



# Example-4: Print vowel count in a string

# string="artificial"
# count=0
# for ch in string:
#     if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
#         count+=1
# print("Total number of vowel in a string=",count)        



# Ranges:- Sequences Generated :  range(start,stop,step)- By default start is 0 and step is +1
# example: range(5)->0,1,2,3,4
# range(1,6)-> 1,2,3,4,5
# range(1,10,2)-> 1,3,5,7,9
    # code 
# for i in range(5):
#     print(i)
# for i in range(1,20,3):
#     print(i)     





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Example<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Print sum of first n natural numbers 

# n =int(input("Enter te number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum =",sum)