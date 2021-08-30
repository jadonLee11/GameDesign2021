import os
import sys
import time
import datetime
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware'] 
file="scoreSheet.txt"
score = 0 
dt=datetime.datetime.now()
linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A")+"\t"
def menu():
    print("""
    print("*********************") 
    print("*Jadon's Game menu  *")
    print("*                   *")
    print("*1. play game       *")
    print("*                   *")
    print("*2. Print Scores    *")
    print("*                   *")
    print("*3. Print Scores    *")
    print("*                   *")
    print("*4. Exit Game       *")
    print("*                   *")
    print("*********************")
    """)
    varChoice = input("pick 1, 2, 3, or 4")
    return varChoice
def GamePause(): #my function to ask if they want to play again
    print("do you want to play again?")
    level = input()
    level = level.lower()
    if "yes" in level:
        return True
    if "no" in level:
        return False
    
def printScore(score):
 FileRead=open(file,'r')
 print(FileRead.read())
 FileRead.close()
 
def updateScore(score):
 Filewrite=open(file,'a')
 line=name+"\t"+linef+"\t\t"+str(score)
 Filewrite.write("\n"+line)
 Filewrite.close()

import random 


def playGame():
    varChoice = menu()
    score = " "
    while varChoice != 3:
        if varChoice == "1": 
            print("Good luck ", name, "!") 
        word=random.choice(gameWords) 
        counter=len(word) 
        print(counter) 
        print (word)    #delete when we finish the code 
        turns= 10   #should we conider controlling this number when he/she misses 
        guesses='' 
        while turns>0 and counter >0: 
            for char in word: 
                if char in guesses: 
                    print(char,end=' ') 
                else: 
                    print('_', end =' ') 
            newGuess=input("\n\n Give me a letter ") 
            #check that the new letter has not been used before 
            if newGuess not in guesses: 
                if newGuess not in word: 
                    turns -=1    #       turns = turns -1 
                    print("Wrong! You have  ", turns, "guesses left") 
                else: 
                    counter -=word.count(newGuess) #deleten repeated letters 
                    print("nice guess!") 
                guesses += newGuess 
            else: 
                print("you used this one already") 

        if counter ==0: 
            print("Fantastic you are Champion") 
            score +=1 
        else: 
            print("Sorry, try harder next time") 
            convert = True
            while convert:
                
                convert= GamePause()
    
    
    answer=input("Do you want to play again? ").upper() 
    print(name," your score is: ", score) 
    return answer
    

#main code
check = True
name=input("What is your name ") 
while check:
    varChoice= menu()
    if "1" in varChoice:
        playGame()
    elif "2" in varChoice:
        updateScore(score)
    #elif "3" in varChoice:
    
    else:
        print("thank you")
        check = False
time.sleep(1)
 