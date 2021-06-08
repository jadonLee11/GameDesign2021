#Jadon Lee
#6/7/2021
#I will be making my game menu that allows the player to pick what they want to do
score = ("15,234")
var= 1
while var ==1 :   
    print("*********************") #this is my menu
    print("*Jadon's Game menu  *")
    print("*                   *")
    print("*1. level 1         *")
    print("*                   *")
    print("*2. level 2         *")
    print("*                   *")
    print("*3. Print Scores    *")
    print("*                   *")
    print("*4. Exit Game       *")
    print("*                   *")
    print("*********************")
    print()
    print("Where do you want to proceed?")
    choice = int(input())
    if choice == 1:
        var = 2
        print("""
               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  
""")
        print("To return to menu, enter 1")
        choice = int(input())
        if choice == 1:
            var = 1
        
        
    if choice == 2:
        print("""
,-----.
`.`_.`\\
     \ \\
      \ \\
       \ \\
        \ `-''^^^^^''-.
         \             `-._
         >>   >  <  <__    ^'-----...,,_
         //__/`---'\__\\`'''''''''''''``
        """)
        print("To return to menu, enter 1")
        choice = int(input())
        if choice == 1:
            var = 1
    if choice == 3:
        print("Game score")
        print(score)
        print("To return to menu, enter 1")
        choice = int(input())
        if choice == 1:
            var = 1
    if choice == 4:
        var = 2
        print("Game Over")
        