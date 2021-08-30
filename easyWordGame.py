#Jadon Lee
#06/11/2021
#Word Game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word
import random

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name =input("What is your name?")
print(name, end = " ")
answer = input(" Do you want to play? ").upper()
print("\n ",gameWords) #delete when code works properly


def GamePause(): #my function to ask if they want to play again
    print("do you want to play again?")
    level = input()
    level = level.lower()
    if "yes" in level:
        return True
    if "no" in level:
        return False

def level():
    print(name," Good luck")
    word=random.choice(gameWords)
    print(word)
    turns=10  # find better way to create turns
    guesses=''
    counter=len(word)
    while turns >0 and counter>0:
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
        newGuess=input("\n Give me a letter ")
        if newGuess in word:
            cheese =word.count(newGuess)
            counter = counter- cheese
            guesses += newGuess    #guesses= guesses+newGuesses
            print("You are Right!!" )
        else:
            turns -= 1
            print ("Sorry that is wrong you still have ", turns," turns") 
    if counter == 0:
        print("good job, you won")
    else:
        print("you lost")

def completeLevel():
        level()
        GamePause()
        x = GamePause()
        if x == True:
            level()
        else:
            print("Goodbye")

while "Y" in answer:
    completeLevel()
    answer="n"
    print("Goodbye")