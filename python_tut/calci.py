x = eval(input("Enter the value of x: "))
y = eval(input("Enter the value of y: "))
def sum():
    return x+y
def sub():
    return x-y
def mul():
    return x*y
def div():
    return x/y
def mod():
    return x%y

ch=str(input("Enter a/b/c/d/e: "))
if ch=="a":
    print("result= ",sum())
elif ch=="b":
    print("result= ",sub())
elif ch=="c":
    print("result= ",mul())
elif ch=="d":
    print("result= ",div())
elif ch=="e":
    print("result= ",mod())
else:
    print("invalid input")