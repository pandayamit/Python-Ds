'''
Dictionary: key:value pairs
             |
        always unique  

Dictionary are muttable in pythons means its key will be reassigned to new value.
Dictonary are unordered unlike lists which is ordered with index number        

'''


# Example:
info={
    "name":"abc",
    "cgpa":9.2,
    "subjects":["math","science"],
    3.14:"PI"
}

# info["cgpa"]=9.8

# print(info)
# print(type(info))
# print(info["name"])
# print(info[3.14])



'''
Dictonary Methods:

1. d.keys()  -> returns all keys
2. d.values() -> return all values 
3. d.items() -> return (key,val) pairs 
4. d.get(val) -> return val according to key
5. d.update(new_item) -> adds new item to dict

'''


print(info.keys())
# dict_keys=info.keys()
dict_keys=list(info.keys())     # typcasting dict to list
print(dict_keys)
print(type(dict_keys))

dict_values= list(info.values())
print(dict_values)

print (info.items())
print(info.get("cgpa"))

info.update(
    {
     "city":"Delhi"
    }
)

print(info)