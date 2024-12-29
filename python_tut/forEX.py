# print the sum of natural number
n=int(input("Enter the value of n: "))
sum=0
for i in range(n+1):
    sum+=i
print("The sum of given numbers is ",sum)
# print the sum of only odd number
oddsum=0
for i in range(n+1):
    if i%2!=0:
        oddsum+=i
print("The sum of given odd numbers is ",oddsum)
# print the sum of only even number
evensum=0
for i in range(n+1):
    if i%2==0:
        evensum+=i
print("The sum of given even numbers is ",evensum)
# print the number of digit in the given number
num=int(input("Enter the value of num : "))
num=str(num)
count=0
for i in num:
    count+=1
print(count)
# print the multiplication table
Num=eval(input("Enter the value of Num: "))
for i in range(11):
    print(Num,"x",i,"=",Num*i)
# print the given number is palidrome or not
Number=eval(input("Enter the value of Number : "))
Number=str(Number)
rev_num=""
for i in Number:
    rev_num=i+rev_num
if rev_num==Number:
    print("The given Number is Palidrome Number")
else:
    print("The given number is not palidrome number")