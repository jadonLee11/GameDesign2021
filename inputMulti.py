#Jadon Lee
#6/4/2021
# We are going to print multiplication tables
# using print statements and a variable
# input ---> variable is a container that will hold data and an address 
#variables need to have valid name
#I am also making all of the math tables of any inputted value.
print("Math tables")
print()
print("What is the base?")
base = int(input())
print("Mutliplication table of", base)
for var in range(1,11):
    print(base,"x",var,"=",base * var)
print()
print("Division table of", base)
for var in range(1,11):
    print(base,"/",var,"=",base / var)
print()
print("Addition table of", base)
for var in range(1,11):
    print(base,"+",var,"=",base + var)
print()
print("Subtraction table of", base)
for var in range(1,11):
    print(base,"-",var,"=",base - var)

