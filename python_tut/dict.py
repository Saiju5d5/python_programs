info = {
    "name" : "xxx",
    "age" : 26,
    "salary" : 25000,
    "company" : "TCS"
} 
print(info)
print(info["name"])
print(info.keys()) #keys() method is used to print all the keys in the dictionary
print(info.values()) #values method is used to print all the values in the dictionary
print(info.get("salary")) # get() method is used to print the values of their corresponding key
for key in info.keys():
    print(info[key])
for key,value in info.items(): #items() method is used to print key value pair 
    print(f"The corresponding value of {key} is {value}")
info1={
    "Name":"yyy",
    "Age":23,
    "Company":"amazon"
}
info.update(info1) #update the dictionary (already existing key value is updated and also new data is added)
print(info)
print(info1)
info1.pop("Name") #delete the the key and value 
print(info1)
del info["name"]
del info1["Company"]
print(info)
print(info1)

''' 1.buit in dictionary function are:-
len(), any(), all(), sorted() 
2.Built in dictionary methods are:-
pop(), popitem(), update(), clear(), keys(), values(), items(),copy() '''
