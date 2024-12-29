t1=("wel","come",'to',"python",True,12,23,34)
print("\n Print the tuple")
print(t1)
print(type(t1))
print(t1[2:6])
if "wel" in t1:
    print("yes it is in given tuple")
else:
    print("NO")
# creating tuple using repition
tup=("Hello",)*5
print(tup,type(tup))
tup2=(t1,tup) #creating nested tuple
print(tup2)
# creating tuple using for loop
t2=("world",)
for i in range(5):
    t2=(t2,)
    print(t2)

country=("Nepal","india","japan","canada","Bangladesh","Bhutan")
print(country,type(country))
l1=list(country)
print(l1,type(l1))
l1.append("Pakistan")
print(l1,type(l1))
country=tuple(l1)
print(country,type(country))
country=country + (4,5)
print(country,type(country))
x=reversed(country)
print(list(x))
