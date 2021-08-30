import random 
varChoice = " "
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware'] 

name=input("What is your name ") 
def menu():
    print("*"*45)
    print("*"," "*3,"Dinosaur Safari"," "*21,"*")
    print("*"," "*7,"Main Menu"," "*23,"*")
    print("*"," "*41,"*")
    print("*"," "*2,"1- play"," "*30,"*")
    print("*"," "*2,"2- print scores"," "*22,"*")
    print("*"," "*2,"3- Exit"," "*30,"*")
    print("*"*45)
    print("Enter either 1,2, or 3", end= " ")
    varChoice = input()
    return varChoice 
score=0 #to total the number of wins 
while varChoice != 3:
    menu()
    if varChoice == 1:

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

     # find a way to decide if the person won the game or not  

     # keep a count of how many words they guessed    

     # #ask user if the want to play again 

      

answer=input("Do you want to play again? ").upper() 

print(name," your score is: ", score) 

 