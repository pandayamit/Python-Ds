'''
Tuples: Tuples in python are immutable sequence of values menas once we define any value inside tuple we can't change it.

Tuples are created with paranthesis:(),while lists are created with []
'''

# Example:1
# tup=(1,2,10,4,"abc",3.14)
# print(type(tup))
# print(len(tup))
# print(tup[2])

'''
note: We can assign value to tuples as it is immutable when we will do this it throws error.
example:
 tup[2]=20
 print(tup[2]) 
'''

# For creating single value tuples we have to strictly follow this syntax 

# tup2=(1,)
# tup3=("abc",)
# print(f"{tup2} and {tup3}")
# print(tup2)



# Slicing in Tuple 

# tup4=(1,2,4,7,8,32)
# print(tup4[2:])



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> Loops in Tuples <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# tup =(1,2,3,4,5)
# sum=0
# for val in tup:
#     sum +=val
# print(f" sum of val is {sum}")




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Methods in tuples   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''
t.index(val) -> returns 1st occurence idx
t.count(val) -> counts total occurences 
''' 

tup=(1,2,2,3,2,4)
print(tup.index(2))
print(tup.count(2))