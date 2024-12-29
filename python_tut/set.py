# program for set and its operation
s1 = {1,2,3,6,8,6,2,"sunday","monday","Tuesday","saturday"}
s2 = {"monday","saturday","friday",3,5,2,1,0,4,6,7 }
print(s1,type(s1))
print(s2,type(s2))
print(s1 | s2) #using union operator
print(s1.union(s2)) #using union() method
print(s1 & s2) #using intersection operator
print(s1.intersection(s2)) #using intersection() method
print(s1-s2) #using difference operator 
print(s1.difference(s2)) #using differece() method
print(s2-s1)#using difference operator 
print(s2.difference(s1))#using differece() method
print(s1^s2) #using symmetric difference operator
print(s1.symmetric_difference(s2)) #using symmeteric_difference() method