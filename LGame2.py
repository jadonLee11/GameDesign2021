#Jadon Lee
#starting from lucas's code
#While loop is a loop that repeats until condition is met
#if statement ---> branching or selection based on conditions
#functions are a piece of code that we create to prevent repetition. starts with a def key
#I am also making the inputs not case sensitive
varChoice=" "
def menu():
    print("*"*28)
    print("*", " "*6, "Dino Safari"," "*5, "*")
    print("*", " "*2, "Menu"," "*16, "*")
    print("*", " "*2, "Level 1"," "*13, "*")
    print("*", " "*2, "Level 2"," "*13, "*")
    print("*", " "*2, "Level 3", " "*13, "*")
    print("*", " "*2, "Level 4", " "*13, "*")
    print("*", " "*2, "Level 5", " "*13, "*")
    print("*", " "*2, "Print Scores"," "*8, "*")
    print("*", " "*2, "Exit Game"," "*11, "*")
    print("*"*28)
    print("enter either l1, l2, l3, l4, print, or ex".title(), end = "  ")
    varChoice = input()
    varChoice = varChoice.lower()
    print(varChoice)
    return varChoice
def score():
    print("your scores:")
    print("800 Bob")
    print("820 Rob")
    print("839 Alex")
    print("760 Tom")
def GamePause():
    print("do you want to play again?")
    level = input()
    level = level.lower()
    if "y" in level:
        return True 
    else:
        return False


varChoice = menu()
while varChoice != "ex":
    if varChoice == "l1" or varChoice == "1":
        convert = True
        while convert:  #boolean variable either true or false
            print("You are in level 1")
            convert= GamePause()

    if varChoice == "l2" or varChoice == "2":
        convert = True
        while convert:  #boolean variable either true or false
            print("You are in level 2")
            convert= GamePause()
       
    if varChoice == "print" :
        score()
    if varChoice == "l3" or varChoice == "3":
        print("you are in level 3")
    varChoice = menu() #call function
print("Goodbye, have a nice day!".center(100))

