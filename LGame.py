#Jadon Lee
#starting from lucas's code
#While loop is a loop that repeats until condition is met
#if statement ---> branching or selection based on conditions
#functions are a piece of code that we create to prevent repetition. starts with a def key
varChoice = " "
def menu(): #declaring a function
    print("*"*28)
    print("*"," "*6,"Forerunner"," "*6,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"L1- Two Betrayls"," "*4,"*")
    print("*"," "*2,"L2- Sacred Icon"," "*5,"*")
    print("*"," "*2,"L3- The Storm"," "*7,"*")
    print("*"," "*2,"EX- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or EX", end= " ")
    varChoice = input() #local variable
    return varChoice 
def score():
    print("Your scores:")
    print("23457 Peter")
    print("23456 Jadon")
    print("12343 James")
    print("507 Ben")   
def gamePause():
    print(print("Do you want to change levels?")
    level = input()
    if level !='no':
        varChoice= menu()

varchoice= menu() #call function

while varChoice != "EX":
    if varChoice == "L1":
        print("You are in level 1")
        print("do you want to change levels?")
        level = input()
        if level != 'no' :
            varchoice= menu


    if varChoice == "L2":
        print("You are in level 2")
    if varChoice == "L3":
        score()
    varChoice = menu()
    varchoice = str(input())
print("Goodbye, Have a nice day")


    

