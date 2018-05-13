#week 1 Decided on idea
#week 2 
#week 3 Had moving car
#week 4 Replaced moving car with scrolling background

#based off of https://youtu.be/AX8YU2hLBUg
import math, random, sys, os, time
import pygame
from pygame.locals import *
from loss import *
#variables
time = 0
factor = 0
speed = 0
score = 0
prevScore = 1
gameRound = 0
myfont = pygame.font.SysFont("monospace", 16)

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Speed Racer")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BROWN = (139, 69, 19)

#define background
bg = pygame.image.load("mainBack.png").convert()
bgWidth, bgHeight = bg.get_rect().size
     
#creating stage
stageWidth = bgWidth * 2
stagePosX = 0

stageHeight = bgHeight * 2
stagePosY = 0

#set cords
startScrollingPosX = HW
startScrollingPosY = HH

#circle stats
circleRadius = 25
circlePosX = circleRadius

#starting place
playerPosX = circleRadius
playerPosY = 600
playerVelocityX = 0
playerVelocityY = 0
###################

pass_limit = 5

#COLLISION function
def intersect():
    if (playerPosY < 525 and  (playerPosY + 40) >= leftcord) and (playerPosY < 525 and (playerPosY + 40) <= rightcord):      
        #print("The Circle's height is " + str(playerPosY) + " and the rectangle is at " + str(rect1PosX))
        return True
    else:
        return False

# main loop	
playing = True

while playing:
	#check if you want to close the game byt he esc button
	events()
	#short hand to call key presses
	k = pygame.key.get_pressed()
	if k[K_SPACE]:
		if playerPosY <= 610:
			playerVelocityY = -2.5
	elif k[K_d]:
		print("The circle is at"+ str(playerPosX) + ", " + str(playerPosY))
		print("The rectangle is at" + str(rect1PosX) + ", " + str(rect1PosY))
		print("The left cord of the rectangle is " + str(leftcord) + " right is " + str(rightcord))

	#sets how the circle moves based on the speed, essentially just the speed of circle
	playerVelocityX = speed 

	#max cords to limit and control jumping
	if playerPosY <= 500:
		playerVelocityY = 2.5
	if playerPosY > 610:
		playerVelocityY = 0
		playerPosY = 610
	
	#moving player on x axis		
	playerPosX += playerVelocityX
	circlePosX = startScrollingPosX
	stagePosX += -playerVelocityX

	#moves player on Y axis and influences jumping
	playerPosY += playerVelocityY
	circlePosY = startScrollingPosY

	#moves x cord of screen and works with the looping background
	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))
	
	#draw the circle
	pygame.draw.circle(DS, WHITE, (int(circlePosX), int(playerPosY - 25)), int(circleRadius), 0)


	
	#Sets the coords of the rectangle and the speed at which they change based of factor
	factor += (speed + 0.5)
	rect1PosX = 1280 - factor
	rect1PosY = 410
	
	#draw rectangle
	#formula for drawing rect: pygame.draw.rect(screen, color, (x,y,width,height), thickness)
	pygame.draw.rect(DS, BROWN, (rect1PosX, rect1PosY, 100, 50), 0)

	leftcord = pygame.draw.rect(DS, BROWN, (rect1PosX, rect1PosY, 100, 50), 0).left
	rightcord = pygame.draw.rect(DS, BROWN, (rect1PosX, rect1PosY, 100, 50), 0).right
	#print(str(leftcord) + " ," + str(rightcord))
	#collision checking and score setting
	intersect()
	if intersect() == True:
		score += 1
		prevScore = score
		#message_display(str(score))
		print("Your score is " + str(score))
		#setScore()
	#sets the score in the top left
	###THE BELOW CODE IS TRIP TRUMAN'S
	#####I got this code from stack overflow

	### i have been searching for LITERALLY DAYS on how to get surf to work
	####after realizing that surf was a library, i tried to figure out how to import it
	## i then searched  on stack overflow, and i got the following code

	scoretext = myfont.render("Score {0}".format(score), 1, (255,255,255))
	DS.blit(scoretext, (5, 10))

	###THANK GOD, i have literally worked for 8 hours this weeekend on this, and finally got it

    ##this is satisfying as hell

	######################THIS ENDS TRIP'S CODE####################
	if rect1PosX < 450 and prevScore != score:
		playing = False
		message_display("YOU LOSE")

	#check if redraw of rectangle is needed
	if rect1PosX < -50:
		factor = 0
		gameRound += 1
		prevScore = (score + 5)

	#makes the game get faster 
	speed += 0.001
	
	#update screen
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)

############
