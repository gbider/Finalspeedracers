#week 1 Decided on idea
#week 2 
#week 3 Had moving car
#week 4 Replaced moving car with scrolling background

#based off of https://youtu.be/AX8YU2hLBUg
import math, random, sys, os, time
import pygame
from pygame.locals import *
from collision import *
from loss import *
#variables
time = 0
factor = 0
speed = 0
score = 0
prevScore = 1
gameRound = 0


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

bg = pygame.image.load("mainBack.png").convert()
bgWidth, bgHeight = bg.get_rect().size

#character
#char = pygame.image.load("character.png").convert_alpha()


      
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

#COLLISION
def intersect():
    if (playerPosY < 550 and  playerPosY >= rect1PosX - 50) and (playerPosY < 550 and playerPosY <= rect1PosX + 50):      
        #print("The Circle's height is " + str(playerPosY) + " and the rectangle is at " + str(rect1PosX))
        return True
    else:
        return False

# main loop
playing = True

while playing:
	#check if close game
	events()
	#short hand to call key presses
	k = pygame.key.get_pressed()
	
	# if k[K_RIGHT]:
	# 	playerVelocityX = 2.5
	# elif k[K_LEFT]:
	# 	playerVelocityX = -2.5
	# else:
	# 	playerVelocityX = 0

	if k[K_SPACE]:
		if playerPosY <= 610:
			playerVelocityY = -2.5
	elif k[K_d]:
		print(str(playerPosX) + ", " + str(playerPosY))

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

	#moves x cord of screen
	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))
	
	#draw circle
	pygame.draw.circle(DS, WHITE, (int(circlePosX), int(playerPosY - 25)), int(circleRadius), 0)
	
	#Rectangle coord assigning
	factor += (speed + 0.5)
	rect1PosX = 1280 - factor
	rect1PosY = 410



	
	#draw rectangle
	#pygame.draw.rect(screen, color, (x,y,width,height), thickness)
	pygame.draw.rect(DS, BROWN, (rect1PosX, rect1PosY, 100, 50), 0)
	
	#collision checking
	intersect()
	if intersect() == True:
		print("YOU SCORED A POINT")
		score += 1
		prevScore = score
		print("Your score is " + str(score))
	#elif intersect() == False:
	
	#if rect1PosX > 500:
		#shouldI = 1
	#if rect1PosX < 450 and shouldI == 0:
		#print("Loss")

	if rect1PosX < 450 and prevScore != score:
		playing = False
		message_display("YOU LOSE")

	#check if redraw needed
	if rect1PosX < -50:
		factor = 0
		gameRound += 1
		prevScore = (score + 5)
	



	speed += 0.001
	

	#load character
	#DS.blit(char,(25,600))

	#update screen
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)

############