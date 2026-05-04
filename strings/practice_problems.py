'''
Stdent Enrollments:
 Given a list of tuples with info(name,subject):
    1. List of all unique course 
    2. list student enrolled in english
    3. create dictionary (set,set of course)
'''

info=[
    ("Alice","Math"),("Bob","Science"),("Alice","Science"),("Charlie","Math"),("Bob","Math"),("Alice","English"),("Charlie","English")
]
unique_courses=set()
for tup in info:
    # print(tup[0]) # name
    unique_courses.add(tup[1]) # course
print(unique_courses)

#--------------------------------2----------------------------------
print("----------------------2:---------------------------")
for name,course in info:
    # print(name,course)
    if(course=="English"):
        print(name)

#-----------------------------------3--------------------------------
print("----------------------3-------------------------")
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)   
print(dict)            