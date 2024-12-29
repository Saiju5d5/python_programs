n=int(input("Enter the valud of n : "))
print("/n print number")
for j in range(n): #print from 0 to n-1
    print(j)
for i in range(2,n): #print from 2 to n-1
    print(i)
for i in range(3,n,2): #print from 3 to n by incremnting  2 number
    print(i)
print("\nprint list")
fruits=["apple","mango","Banana","kiwi","cherry","orange","Grapes"]
for fruit in fruits:
    print(fruit)
    for i in fruit:
        print(i)
print("\nbreak statement inside for loop")
for fruit in fruits:
    if fruit=="cherry":
        break
    print(fruit)
print("/n continue statement in for loop")
s="wel come to python world!"
for i in s:
    if i=="o" or i=="h":
        continue
    print(i)