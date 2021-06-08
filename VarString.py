#Jadon Lee
#use different types of variables
#use strings functions
#use while loop
num1 = 10
num2 = 3.5
num3 = 0xadfe1235331fea
name = "computer"
#       01234567   the last index is 7 len = 8
print(type(num1))
print(type(num2))
print(type(num3))
print(type(name))
print(name[2]) #print the letter in box 2
print(name[2:7]) #print the boxes from 2-6
numIndex = len(name)
print(numIndex)
print(name * 3)
for var in range(1,4) :
    print(name[3:], end=" ") #print from 3 to end
    print(name[3:numIndex])#print from 3 to end
print("done")
#concadanation
name="Peter"
lastName= "Smith"
fullName= name+" "+lastName
print(fullName)
print("Smith" in fullName)
while "Smith" in fullName:
    print(fullName)
    fullName='Peter Sims'
print("done")
