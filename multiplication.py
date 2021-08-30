#Jadon Lee
# We are going to print multiplication tables
# using print statements and a variable
# input ---> variable is a container that will hold data and an address 
#variables need to have valid name
base = 2
numberBase = "multiplication"
base3 = 3.5
print(base + base3)
print(1 * base) #multiplication is represented with * 
print(2 * base) #division uses /
print(3 * base)
print(4 * base)
print(5 * base)
print(6 * base)
print(7 * base)
print(8 * base)
print(9 * base)
print(10 * base)
#when we repeat something, we should loop, loop with a counter
base= 2
for base in range(2,10) :
    for counter2 in range(1,11) :
        print(counter2 * base, end=" ")
    print()

    