n = eval(input("Enter the value of n between 5 and 15 : "))
if n<5 or n>15:
    raise ValueError("Value must be in between 5 and 15.")
else:
    print("The given input is correct.")