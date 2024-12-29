# program to create a Normal pyramid
n=int(input("Enter the value of n : "))
print("\nNormal Pyramid")
for i in range (n):
    a=" * "
    a=a*i
    print(f'{a: ^20}')
# program to create a invert pyramid
print("\n Invert pyramid\n")
for i in range (n):
    a=" * "
    a=a*(5-i)
    print(f'{a: ^20}')