print("Example : 1\n")
college_name = "BVC Engineering College."
dept_name = "Computer Science and Engineering"
name = "xxx"
address = "HYD"
txt = f"myself {name} , I am from {address} I am studying {dept_name} in {college_name}"
print(txt)

print("\n Example : 2\n")
item = "Book"
price = 999.4566
txt1 = f"The price of {item} is {price:.2f}."
print(txt1)

print("\nExample : 3\n")
a=10
b=6
c=8
p = f"The product of {a},{b} and {c} is {a*b*c}"
print(p,type(p))

print("\nExample : 4\n")
dict = { "name":"XXX","Age":27,}
txt2 = f"My name is {dict["name"]} and i am {dict["Age"]} years old."
print(txt2)

print("\nExample : 5(print the curly braces by using double curly braces)\n")
txt3 = f"My name is {{dict['name']}} and i am {{dict['Age']}} years old."
print(txt3)