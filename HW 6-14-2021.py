#Jadon Lee

# 06/11/2021 
#Word Game 
# We are creating a list of words 
# randomly select a word from the list for the user to guess 
# give the user some turns 
# show the word to the user with the characters guessed   
# play the gane as long as the user has turns or has guessed the word 
import random 
import sys 
import os 
import time 
import datetime 
 
os.system('cls') 
#Global variables 
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware'] 
name=" " 
score=0 #to total the number of wins 
file="Scoreboard.txt" 
dt=datetime.datetime.now() 
linef=str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A") 
def menu(): 
    print("""
    print("*********************") 
    print("*Jadon's Game menu  *")
    print("*                   *")
    print("*1. play game       *")
    print("*                   *")
    print("*2. Print Scores    *")
    print("*                   *")
    print("*3. Change Player   *")
    print("*                   *")
    print("*4. Exit Game       *")
    print("*                   *")
    print("*********************")
    """)

    return input("What is your choice? ") 
def updateWord(word, guesses):  # function with a parameter to update word 
    for char in word: 
        if char in guesses: 
            print(char,end=' ') 
        else: 
            print('_', end =' ') 
def printScore(): 
    FileRead=open(file,'r') 
    print(FileRead.read()) 
    FileRead.close() 
     
def updateScore(score): 
    FileWrite=open(file,'a') 
    line=name+"\t"+ linef+ "\t\t"+str(score) 
    FileWrite.write("\n"+ line) 
    FileWrite.close() 

#main program 
def PlayGame(answer, score):    
    while "Y" in answer: 
        os.system('cls') 
        print("Good luck ", name, "!") 
        word=random.choice(gameWords) 
        counter=len(word) 
        print(counter) 
        print (word)    #delete when we finish the code 
        turns= 10   #should we conider controlling this number when he/she misses 
        guesses='' 
        updateWord(word, guesses) 
        while turns>0 and counter >0: 
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
            updateWord(word, guesses) 

        if counter==0:  
            print("\n Congradulation!") 
            score +=1 
        else: 
            print("Good try, but not good enough") 
        answer=input("Do you want to play again? ").upper() 
    updateScore(score) 

check=True 
while check:
    name = input("What is your name")
    varChoice= menu() 
    if "1" in varChoice: 
        PlayGame("Y",score) 
    elif "2" in varChoice: 
        printScore() 
        input("press enter if done") 
        os.system('cls') 
    elif "3" in varChoice: 
        name=input("What is your name? ") 
    else: 
        print("Goodbye") 
        check=False 
    time.sleep(1) 

     

 
 
 
 

 