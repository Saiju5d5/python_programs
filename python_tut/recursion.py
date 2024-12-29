print("the factorial of given number.\n")
n1 = int(input("Enter the value of n1: "))
def factorial(n1):
    if n1==0 or n1==1:
        return 1
    else:
        return n1 * factorial(n1-1)
print(factorial(n1))
print(factorial(5))

print("\nprint the fibonacci series.\n")
def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n = int(input("Enter the value of n: "))
for i in range (n+1):
    print(fibonacci(i),end=",")

print("\nprint the power of given number\n")
num = eval(input("Enter the value of num: "))
pow = int(input("Enter the value of pow: "))
def power(num,pow):
    if pow==0:
        return 1
    elif pow==1:
        return num
    else:
        return num*power(num,pow-1)
print(power(num,pow))