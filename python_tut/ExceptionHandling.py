a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=input("Enter the value of c: ")
# ZeroDivisionError
try: #this block contain error arising code
    d=a/b
    print("The value of d: ",d)
except Exception as e: #This block handle the error
    print("First block executed sucessfully.")
# TypeError
try:
    e=a+c
    print(e)
except Exception as e:
    print(e)
    print("Second block executed sucessfully.")
# list index out of range Error
l1=[1,2,3,4]
try:
    print("The value of l1[3] is ",l1[3])
    print("The value of l1[4] is ",l1[4])
except Exception as e:
    print(e)
    print("Third block executed sucessfully.")
# finally block is exceuted either exception is handle or not
finally:
    print("Finally block is executed.")
    x=10
    y=24
    print(x+y)
