import time, os, sys, hashlib

os.system('cls')
file = "scoreboard.txt"
FILE = open(file, 'r')
#print(FILE.read())
FILE.close()
FILE = open(file, 'r')
contest_List = FILE.readlines()
#print(contest_List)
FILE.close()
#for element in contest_List:
    #print(element)
sorted_List= sorted(contest_List, reverse =False)[::-1]
#sorted_List= sorted(contest_List, reverse= True)[::-1]
for line in range(6):
    print(sorted_List[line])
