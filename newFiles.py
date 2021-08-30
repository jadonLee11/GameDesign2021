#Jadon Lee
#6/14/2021
#we are going to learn how to open files. read files, to write files
import os
import sys
import time
print("Hello... let me guess your name...")
time.sleep(2)
print("...almost...")
time.sleep(2)
os.system('cls')
print("... yes you are Jadon")
file=input("please enter a file name add extension of the file. EX. file.txt :")
if os.path.exists(file):
    PENCIL=open(file,'r')
    print(PENCIL.read())
    PENCIL.close()
else:
    print("the file does not exist")
BOOK = open
