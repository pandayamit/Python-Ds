'''
Sets(can be mutable): Sets in python is a collection of unique elements(elemets of sets are always immutable).
sets are unordered unlike lists.

example:  s={1,2,2,2,3}
          print(s)

          output: {1,2,3}


Sets Method:

1. s.add(val)      :- adds a value
2. s.remove(val)   :- removes a val
3.s.clear()        :- empties the set
4.s.pop()          :- removes a random val
5.s.union(set2)    :-  return new union
6.s.intersection(set2) :- return new intersection


'''

# Example:1

s={1,2,2,3,3,5}
print(s)
print(type(s))
print(len(s))
s.add(8)
print(s)
empty_set={}    # it creates an empty dictionary to create empty set we have this command 
empty_sets=set()
print(type(empty_sets))
s.remove(1)
print(s)
s.pop()
print("pop",s)
s.clear()
print("clear",s)


# Example:2
print("--------------------------------------------------------------------------")
set1={1,2,3,4,6,7,9}
set2={1,3,5,8,10}
print(set1.union(set2))
print(set1.intersection(set2))