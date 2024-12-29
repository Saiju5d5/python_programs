sports=["cricket","football","volleybal","table tennis","kabbadi"]
enum=enumerate(sports,1)
l=list(enum)
print(enum)
print(type(enum))
print(l) #To print as list
print(tuple(list(enumerate(sports)))) #print tuple by using enumerate function
print(tuple(l))
print(dict(list(enumerate(sports)))) #print dict by using enumerate function
print(dict(l))
print(set(l))