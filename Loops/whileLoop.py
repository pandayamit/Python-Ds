# Loops: There are 2 types of loop in python -1.While loop, 2.For loop 


                                # Example-1: Finite Loop-5x

# count = 1

# while (count <= 5):
#     print("Hello world",count)
#     count +=1
# print("after loop,count=",count)


                        #   Example-2:Print a number from 1 to 5

# i = 1
# while (i <= 5):
#     print(i)
#     i += 1


#                     Example-3- Print a reverse number from 5 to 1

# i = 5
# while (i >= 1):
#     print(i)
#     i -= 1


#                   Example-4: Print Multiplication table of any number 'n'


# n = int(input("Enter the number:"))
# i=1
# while (i<=10):
#     print(n*i)
#     i+=1



'''    
Break and continue in Python:-Break means its terminates the loop and on the other hand continue means skipping the current iteration and go to next iteration

 '''
#  Example for Break

# i=1
# while (i <= 10):
#     if(i % 8 == 0):
#         break
#     print(i)
#     i +=1
# print("Outside Loop.....")   



# Example for Continue

# i=1
# while (i<=10):
#     if(i%3==0):
#         i+=1
#         continue
#     print(i)
#     i+=1






# Example- Print odd number with or without using continue

# Without using continue 

# i=1
# while (i<=10):
#     print(i)
#     i+=2


# >>>>>>>>>>>>>>by using continue 

i=1
while (i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1