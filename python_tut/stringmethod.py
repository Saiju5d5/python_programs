a="wel come to python"
b="Bishal"
c="Wel Come to JAVA"
d="wel come to html wel come to c++"
f=b.replace("Bishal","sailesh")
print(a.upper()) #convert into uppercase
print(b.lower()) #convert into lowercase
print(a.capitalize()) #capitalize fisrt of sentences and remaining convert into lowercase
print(c.capitalize())
print(b.replace("Bishal","Rohit"))
print(a.split()) #splits the given string at the  specified instances and return the specified strings into list
print(d.count("wel")) #counts the number of times thd given value has occured in the string
print(a.endswith("thon")) #check the string ends with a given value ,if yes return True otherwise False
print(d.startswith("we")) #check the string starts with a given value ,if yes return True otherwise False
print(a.find("py")) #search the given value in the stringe and returns index, if value is not present returns -1
e="abc123"
print(e.isalnum()) #return True if string contain both alpha and numeric
print(a.isalnum())
print(c.isalpha()) #returns True if string contain alphabet only
print(e.isalpha())
print(a.islower()) #returns True if string contain all lowercase
print(b.isalpha())
print(c.isupper()) #returns True if string contain all uppercase
print(a.title()) #capitalize first letter of each word within the string
print(f)