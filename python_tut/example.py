# # reverser order
# s = "Hello World"

# def new():
#     r = reversed(list(s))
#     o= ""
#     for letter in r:
#         o = o + letter
#     print(o)
# new()


# def Fibonacci(n):

#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)


# # Driver Program
# print(Fibonacci(9))

# s = {1,2,3,4,5,6,7,7,5}
# fs = frozenset(s)
# print(s,type(s))
# print(fs,type(fs))
# fs.add(10)

# d= {}
# print(d)
# d[0]="pyhton"
# d[2]="java"
# d[3]="c++"
# d[6]="css"
# print(d)
# d[1]="html"
# # d[0]="javascript"
# # print(d)
# # class parent:
# def old(x,y):
#     print("parent class.\n")
#     print("python programming.\n")
#     print(x+y)
# # class child(parent):
# def new(a,b):
#     print("Child class.\n")
#     print(a-b)
# old(2,3)
# new(3,2)
#help(bool)
a=1.5
b=2.5
c=a+b
if (c := 4):
    print("True")
else:
    print("False")
