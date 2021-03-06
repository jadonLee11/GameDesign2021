#Jadon Lee
#6/25/2021
#The game is a game that requires the player to repeat a pattern that is shown on the screen.
#I used lists and random to create the patterns for the player to repeat
#I used datetime, time, and files to make a scoreboard on a text file.
#The game can go on forever, but if you lose a level, points are taken away.
import random, sys, time, os, datetime
dt=datetime.datetime.now() 
pizza=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A") #This is the date
Scoreboard="Scoreboard.txt" #my text file that the scoreboard is stored in
score = 0 #score of the player
numberListEasy= ["1","2","3","4"] #list of numbers for easy level
numberListMedium = ["1","2","3","4","5","6"] #list of numbers for medium level
numberListImpossible= ["1","2","3","4","5","6"] #list of numbers for impossible level.
def replay(): #my function to ask the player if they want to play again
    print("do you want to do it again?")
    level = input()
    level = level.lower() #lowercases the input so that it isnt case sensitive
    if "y" in level:
        return True #if they answer yes, the level will re loop
    else:
        return False #if they answer no, the main menu will open

def updateScore(score): #funtion to write the score into the scoreboard file
    FileWrite=open(Scoreboard,'a') 
    line=line=str(score)+ name+"\t"+ pizza+ "\t\t" #defines what to write into the file
    FileWrite.write("\n"+line) #writes the line into the file
    FileWrite.close() #closes the file

def printScore(): #function to read the scoreboard file
    HIGHESTSCORES=[] #list of highest scores
    F = open("scoreboard.txt") #opens text files
    rscore = F.readlines() 
    sortedscore = sorted(rscore, reverse= True) #sort scores from highes to lowest
    for line in range(7):
        chedder =(str(sortedscore[line])) #gets the scores that are in top 7
        HIGHESTSCORES.append(chedder) # puts them into the list
    F.close() #closes file
    for i in range(6):
        print(HIGHESTSCORES[i]) #prints top 6 scores

def menu(): #menu function.
    print("""
    **********************
    *    Jadons Number   *
    *        Game        *
    * 1. easy            *
    * 2. Medium          *
    * 3. Impossible      *
    * 4. Highest scores  *
    * 5. instructions    *
    * 6. Exit game       *
    **********************
    """)
    print("enter either 1, 2, 3, 4, 5, or 6".title(), end = "  ") #asks the user what they want to do
    choice = input() #sets a variable to the input
    return choice #returns variable

def easy(score): #function for the easy level
    convert = True #loop
    while convert: 
        random.shuffle(numberListEasy) #randomizes the list
        print(numberListEasy) #prints the randomized list
        time.sleep(2) #shows the list for two seconds
        os.system('cls') #deletes the list
        answer= input("What are the numbers?") #asks the player what the numbers are
        if answer == numberListEasy[0]+numberListEasy[1]+numberListEasy[2]+numberListEasy[3]: #if the answer is correct
            score +=1 #gets one points
            print("congradulations, you won")

        else: #if the answer is not right
            print("better luck next time")
            score -=1 #takes away one point
        convert= replay() #asks the player if they want to play again
        os.system('cls') #gets rid of clutter
    updateScore(score) #uploads score to scoreboard
    

        

def medium(score): #function for medium level
    convert = True
    while convert:# loop
        random.shuffle(numberListMedium) #randomizes list
        print(numberListMedium) #prints randomized list
        time.sleep(2) #shows list for two seconds
        os.system('cls') #deletes the list
        answer= input("What are the numbers?") #asks the user what the pattern was
        if answer == numberListMedium[0]+numberListMedium[1]+numberListMedium[2]+numberListMedium[3]+numberListMedium[4]+numberListMedium[5]:#if answer is right
            score +=1.5 #two points is awarded
            print("congradulations, you won")
        else:
            print("better luck next time")
            score -=1.5 #two points are taken away
        convert= replay() #asks player if they want to play again
        os.system('cls')# gets rid of clutter
    updateScore(score) #writes score into scoreboard

def impossible(score): #function for impossible level
    convert = True
    while convert: #loop
        random.shuffle(numberListImpossible) #randomizes the list again
        print(numberListImpossible) #prints list
        time.sleep(.9
        ) #shows list for 1 second
        os.system('cls') #deletes list
        answer= input("What are the numbers?")# asks for numbers
        if answer == numberListImpossible[0]+numberListImpossible[1]+numberListImpossible[2]+numberListImpossible[3]+numberListImpossible[4]+numberListImpossible[5]: # if answer is right
            score +=2 #add two
            print("congradulations, you won")
        else:
            print("better luck next time")
            score -=2 #take away two
        convert= replay()# asks player if they want to play again
        os.system('cls') #clears clutter
    updateScore(score) #writes score into scoreboard
def instructions(): #function for instructions option
    convert = True
    while convert: #list
        print("""
        Instructions:
        You will pick a level, then a group of numbers will show up on your screen.
        Your task is to repeat the code of numbers back to the computer too get points.
        The harder the difficulty, the harder it will be to complete. Every win on easy 
        will score you one point, but every lose, you will lose one. every win on medium will 
        score you one point five points, but every lose will take away one point five. Every win on 
        impossible will award two points, but every lose will take away two.
        your scores will be saved separately for each level. The scoreboard only functions when 
        there is atleast 7 scores in it.
        """) #instructions
        convert= replay() #asks if they want to repeat the instructions
        os.system('cls') #clears instructions

def scoreBoardLevel(): #function to read and print the scoreboard
    convert = True
    while convert:
        printScore() #function to print the file
        convert= replay()
        os.system('cls')


#main function
os.system('cls') #clears clutter
name=input("What is your name ") #asks what the players name is
os.system('cls')# deletes previous question
choice = menu() #opens the menu so that the player picks a level.
os.system('cls') #clears the menu
while choice != "6": #loop while not exiting the game
    if  choice == "1":
        easy(score) #easy level function
        
    if choice == "2":
        medium(score) #medium level function

    if choice == "3" :
        impossible(score) #impossible level function

    if choice == "4" :
        scoreBoardLevel() #scoreboard function

    if choice == "5":
        instructions() #instruction function

    choice = menu()# menu function
    os.system('cls')
print("Goodbye, have a nice day!".center(100)) #prints goodbye if exit