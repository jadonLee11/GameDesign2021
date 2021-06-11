#Jadon Lee
#6/20/2021
#lists and their functions
#indexing a list always starts in 0
myNumbers=[1,2,3,4,5,9,34]
myFruits=["apples", "cherries", "mangoes", "bananas"]
print(myFruits)
myFruits.append("kiwi")
for fruit in myFruits: #for each element in your array get the value
 print(fruit, end=", ")
print()
counter=len(myFruits)
for x in range(0,counter-1): #length of array is one more bc index starts with 0
 [print(myFruits[x], end=", ")]
print(myFruits[counter-1])
myFruits[1]="berries" #edit a list or replace a term
print(myFruits[1:3])
if "apples" in myFruits:
 print("I have apples")
else:
 print("I need apples")