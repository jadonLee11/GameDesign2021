import time,sys,os
TOPSCORES=[]
file = open("scoreboard.txt")
readscores = file.readlines()
sortedscore = sorted(readscores, reverse= True)
for line in range(7):
    scoreprint =(str(sortedscore[line]))
    TOPSCORES.append(scoreprint)
file.close()
for i in range(6):
    print(TOPSCORES[i])