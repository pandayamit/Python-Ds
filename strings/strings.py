
# Note: Strings in python are immutable means once any value is assigned to any variable then after it can't be reassigned or changed 

word = "string"
word2= "python"
#concatenate
print(word + word2)

# length calculate 
print(len(word+word2))

# printing any index value 
print(word2[2])

# for loop used for strings 

for ch in word:
    print(ch)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Slicing in Strings <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#  Slicings in strings are the concept which is used to create sub strings from a string or  create multiple slices from a piece of string

# syntax ->   str[st idx : end idx]    , where end idx is not included

#  Example:1-

word3= "Python"
print(word3[2:4+1])

# example:2 
word4 = "I study from ElectAps"
print(word4[13:21+1])
print(word4[13:22])
print(word4[13:])
print(word4[13:len(word4)])
print(word4[:len(word4)])
print(word4[:])

# Example:3

words= "Amit"
print(words[-4:-1])
print(words[-4:])
print(words[:-4]) 




# >>>>>>>>>>>>>>>>>>>>>>> Formatting in Strings <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

'''
there are to ways to formatting any strings 
1- format() -> it has placeholder and placement value
2. f-strings -> in F-strings we used Literal string interpolation means inside strings we can embed any variable or expressions
'''


# Example:1

a=5
b=9
sum= a+b

#  Normal formatting
print("sum is {}".format(sum))
print("Language is {}".format("python"))
print("sum of {} & {} is {}".format(a,b,sum))

#  Index based formatting
print("sum of {1} & {0} is {2}".format(a,b,sum))

#  Value based formatting
print("Value of vars {a} & {b}".format(a=5,b=8))


#  Example of F-Strings

print(f"The sum of {b} & {a} is {a+b}")
print(f"The avg of {b} & {a} is {(a+b)/2}")

