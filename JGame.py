#Jadon Lee
#6/10/2021
# I am remaking my menu and using lists and letting the user alter the list based on the level.
myDinos = ["Bronto", "T-rex", "Raptor", "Quetz", "Dodo"]
varChoice = " "
def menu(): #my menu function
    print("*"*45)
    print("*"," "*3,"Dinosaur Safari"," "*21,"*")
    print("*"," "*7,"Main Menu"," "*23,"*")
    print("*"," "*41,"*")
    print("*"," "*2,"1- Is that dino in the list?"," "*9,"*")
    print("*"," "*2,"2- Reverse the order of the dino list "*1,"*")
    print("*"," "*2,"3- Find the index of the dino"," "*8,"*")
    print("*"," "*2,"4- Insert dino"," "*23,"*")
    print("*"," "*2,"5- Find dino on the list"," "*13,"*")
    print("*"," "*2,"6- Move a dino to the end of a list"," "*2,"*")
    print("*"," "*2,"EX- Exit Game"," "*24,"*")
    print("*"*45)
    print("Enter either 1,2,3,4,5,6, or EX", end= " ")
    varChoice = input()
    return varChoice 
def GamePause(): #my function to ask if they want to play again
    print("do you want to play again?")
    level = input()
    level = level.lower()
    if "yes" in level:
        return True
    if "no" in level:
        return False
    


while varChoice != "ex":
    varChoice = menu()
    if varChoice == "1": 
        convert = True
        while convert:
            print("You are in level 1: Is that dino in the safari?")
            print(myDinos)
            num = int(input("What number dinosaur do you want from 0-5?"))
            print(myDinos[num])
            convert= GamePause()
        
    if varChoice == "2": 
        convert = True
        while convert:
            print("You are in level 2: Reversing the order.")
            x = 4
            while x > -1:
                print(myDinos[x])
                x= x-1
            convert= GamePause()
    
    if varChoice == "3": 
        convert = True
        while convert:
            print(myDinos)
            name = input("What dinosaur do you want to delete from the list?")
            myDinos.remove(name)
            print(myDinos)
            print("You are in level 3: Is that dino in the safari?")
            convert= GamePause()
    if varChoice == "4": #works but has the same problem as level one
        convert = True
        while convert:
            print(myDinos)
            num1 = input("What dinosaur do you want to know the index of?")
            ret = myDinos.index(num1)
            print(ret, "is the index of", myDinos[ret])
            print("You are in level 4: Index of a dino.")
            convert= GamePause()

    if varChoice == "5":
        convert = True
        while convert:
            search = input("what dino do you want to search for in the list?")
            if search in myDinos:
                print(search,"is in the list.")
            if search not in myDinos:
                    print(search, "not found") #why no work?

        
            print("You are in level 5: Is that dino in the safari?")
            convert= GamePause()
            if convert == False:
                menu()
        
    if varChoice == "6": 
        convert = True
        while convert:
            print("You are in level 6: Add a dino to the list?")
            print(myDinos)
            add = input("What do you want to add to the list?")
            myDinos.append(add)
            print(myDinos)
            convert= GamePause()
print("goodbye")