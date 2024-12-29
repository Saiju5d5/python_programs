print("Example 1\n")
a=eval(input("Enter the value of a: "))
b=eval(input("Enter the value of b: "))
result = {a<b:"a is less than b",a>b:"a is greater than b"}.get(True,"Equal")
print(result)
print("\nExample 2\n")
print(a) if a>b else print(b) 
c=10 
print(c) if a>b else 0
