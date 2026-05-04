# print("hello")
# amit = "amit pandey"
# print(amit)
# amit2=23
# amit3=34
# print(amit2+amit3)


# 2. example of avegrage of two numbers by taking input from user  

# a = float(input("please enter first number:"))
# b= float(input("please rnter the 2nd number:"))
# print((a+b)/2)



# 3. conditionals- if,elif,else 
  
    #    example:1
# age=float(input("Enter your age:"))
# if age>=18:
#     print("Congratulations, You can vote")
# else:
#     print("Oops!, You are under 18, can't vote")


                 #  Example:2

# color= input("Please write Traffic Signal Color:")
# if color=="red":
#     print("You have to stop and wait for signal change")
# elif color=="green":
#     print("Green signal indicates, You have to go")
# elif color=="yellow":
#       print("Read to go when yellow color appears")
# else:
#     print("Oops!,You wrote wrong color")        



                        # Example:3

# age=float(input("Enter Your age:"))
# if age<13:
#     print("Hey!, you are a child")
# elif age>=13 and age<=18:
#     print("You are a Tennager")
# else:
#     print("You are a adult Person")  


                #    Example:4

# userName=input("Enter Your UserName:")
# password=input("Enter you Password:")

# if (userName=="admin" and password=="pass"):
#     print("Login Successfull")
# elif (userName!="admin"):
#     print("Wrong UserName entered")
# else:
#     print("Wrong Password entered")       


                #    Example:5- Find a number is multipe of 5 or not
# n= float(input("Enter the number:"))
# if (n % 5==0):
#     print("The entered number is a multiple of 5")
# else:
#     print("Oops!, entered number is not a multiple of 5")

    
                # Example-6 : Find a number is Even number or Odd Number

# n=float(input("Please enter the number:"))
# if (n%2==0):
#     print("Hey!, it's a Even Number:",n)
# else:
#     print("It's a odd number:",n)







# 4. Nesting: Nesting means that a condition inside another condition and so on......

                            #   Example:1: 
# username=input("Enter the username:")
# password=input("Enter the password:")
# if (username=="admin" and password=="pass"):
#     print("Login Successfull")
# else:
#     if (username!="admin"):
#         print("Wrong username")
#     else:
#         print("Wrong password") 




# 5.    Match Case in Python - It's a altenative of  if,elif and else conditions

                        #  Example-1:

color=input("Enter the Traffic color name:")
match color:
    case "Green": 
        print("Go")
    case "Yellow":
        print("Yellow")
    case "Red":
        print("Stop")       
    case _:
        print("Wrong color name entered") 