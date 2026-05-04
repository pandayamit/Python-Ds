'''
List:- List is a one of 4 builtin datatype of python the other builtin datatypes are -> tuples, dictionary and sets.

List:- List is a muttable sequence of values. In list we can store different type of values like strings and float numbers.
  
  ex- marks=[20,30,38,10,90] -> here at index[0]=20,index[1]=30 and so on...

  muttable means we can overwrite or change list value 
  ex- marks[2]=40 -> now in marks list at index 2 38 is replaced by 40 


List Methods(funtions):

1. l.append(val)   -> add one element at end 
2. l.insert(val)   -> insers element at idx
3. l.sort()        -> arranges in increasing order
4. l.reverse()     -> reverses order


'''

# Example-1 
marks=[20,40,35,90,80,92]
# print(marks)
# print(len(marks))
# print(marks[2])
# marks[3]=98
# print(marks)


# Example-2 
# scores=[30,54,94,90,"abc",99.99]
# print(scores)
# print(len(scores))
# print(scores[4])
# print(type(scores))



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Slicing in Lists <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Example-1
# print(marks[0:5])
# print(marks[4:len(marks)])
# print(marks[3:])
# print(marks[-5:])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Lists Methods <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Example:

# marks.append(82)
# print("append",marks)
# marks.insert(0,5)
# print("insert at 0:",marks)
# marks.sort()
# print("sort:",marks)
# marks.sort(reverse="true")
# print("sort reverse:",marks)
# marks.reverse()
# print(marks)




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Loops with Lists <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''
Generally we use for loop with lists 
'''

# Example:

nums=[1,4,6,10,27]
for val in nums:
  print(val)

# Example-2:Its an example of linear search
nums2=[1,2,10,4]
x=10
idx=0
for val in nums:
  if(val==x):
    print(f"{x} found at idx={idx}")
    break
  idx+=1

 
