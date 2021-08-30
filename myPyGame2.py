#JadonLee
#learn how change colors
#Learn to draw shapes
#Lear ho to control objects on the screen with key
import time, sys, pygame, os
pygame.init() #Initialize the game
WIDTH=500
HEIGHT=600
purple=[200,0,200]
white = [255,255,255]
red = [200,25,0]
green=[0,200,50]
os.system('cls')
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #declare our screen
screen.fill(green)
pygame.display.set_caption("Jadon's game")
BG = pygame.image.load("images\Background.jpg")
character = pygame.image.load("images\guard.png")
rad = 30
x=10
y=10
x2= 50
y2= 50
xa = 20
ya = 30
wbox=20
hbox=20
rect1= pygame.Rect(x,y,wbox, hbox)
rect2= pygame.Rect(x2,y2,wbox, hbox)
speed = 2
jump = 10
check = True
JumpCheck =False
JumpCheck2 = False
while check:        # ALL YOUR PROGRAMS WITH PYGAME MUST HAVE THIS PART
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False

        
    KB = pygame.key.get_pressed()
    if KB[pygame.K_RIGHT]: #move rectange two pixels to the right
        rect1.x += speed

    if KB[pygame.K_LEFT]:
        rect1.x -= speed

    if not JumpCheck:
        if KB[pygame.K_UP]:
            rect1.y -= speed

        if KB[pygame.K_DOWN]:
            rect1.y += speed

        if KB[pygame.K_SPACE]:
            JumpCheck =True
    else:
        if jump>= -10:
            rect1.y -= (jump*abs(jump))/2
            jump-=1
        else:
            jump = 10
            JumpCheck =False

    if KB[pygame.K_1]:
        rad += speed
    if KB[pygame.K_2]:
        rad -= speed
    if KB[pygame.K_d]: #move rectange two pixels to the right
        rect2.x += speed

    if KB[pygame.K_a]:
        rect2.x -= speed

    if KB[pygame.K_w]:
        rect2.y -= speed
    if KB[pygame.K_s]:
        rect2.y += speed
#movement of character start
    if KB[pygame.K_l]: 
        xa += speed #xa is the x coordinate of the character
    if KB[pygame.K_j]:
        xa -= speed
    if not JumpCheck2:
        if KB[pygame.K_i]:
            ya -= speed #ya is the y coordinate of the character
        if KB[pygame.K_k]:
            ya += speed
        if KB[pygame.K_m]:
            JumpCheck2 =True
    else:
        if jump>= -10:
            ya -= (jump*abs(jump))/2
            jump-=1
        else:
            jump = 10
            JumpCheck2 =False
    #movement of character end
    if rect1.x <0: rect1.x=0
    if rect1.x >WIDTH -wbox: rect1.x = WIDTH -wbox
    if rect1.y< 0: rect1.y = 0
    if rect1.y> HEIGHT- hbox: rect1.y = HEIGHT-hbox

    if rect2.x <0: rect2.x=0
    if rect2.x >WIDTH -wbox: rect2.x = WIDTH -wbox
    if rect2.y< 0: rect2.y = 0
    if rect2.y> HEIGHT- hbox: rect2.y = HEIGHT-hbox
    if rad < 0: rad = 1
    if rad > WIDTH/2: rad = 250
    if rect1.colliderect(rect2):
        rect1.x -=10
        rect2.x +=10
    screen.fill(purple)
    screen.blit(BG,(0,0))
    screen.blit(character, (xa,ya))
    pygame.draw.rect(screen, red, rect1)
    pygame.draw.rect(screen, purple, rect2)
    pygame.draw.circle(screen, (white), (x + 240, y +300), rad, 2)
    pygame.display.update()
    pygame.time.delay(30)
print("Goodbye")
pygame.time.delay(100)  #delay in milliseconds
pygame.quit()