# defaultly python take user input as string
a=input("Enter the value of a : ")
b=input("Enter the value of b : ")
# define specific value to the variable
# assign interger value
c=int(input("Enter the value of c : "))
# assign float value
d=float(input("Enter the value of d : "))
# we can assign both integer and float by using eval()
e=eval(input("Enter the value of e : "))
f=eval(input("Enter the value of f : "))
print(a+b,type(a),type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))