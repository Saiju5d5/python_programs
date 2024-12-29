import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# print greeting according to the current
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour=int(input("Enter hour: "))
print("Hour is ",hour)
if hour > 0 and hour <12:
    print("Goodmorning!")
elif hour >= 12 and hour < 16:
    print("Good Afternoon")
elif hour >= 16 and hour < 19:
    print("Good Evening!")
elif hour >= 19 and hour < 24:
    print("Good Night")
else:
    print("Invalid Input")