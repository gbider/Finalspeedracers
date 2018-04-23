#week 1 Decided on idea
#week 2 
#week 3 Had moving car
#week 4 Replaced moving car with scrolling background



#based off of https://youtu.be/AX8YU2hLBUg
import math, random, sys, os, time
import pygame
from pygame.locals import *

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
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("mario.png").convert()
bgWidth, bgHeight = bg.get_rect().size


stageWidth = bgWidth * 2
stagePosX = 0

stageHeight = bgHeight * 2
stagePosY = 0

startScrollingPosX = HW
startScrollingPosY = HH

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 360
playerVelocityX = 0
playerVelocityY = 0
###################

# main loop
time = 0

while True:
	events()
	k = pygame.key.get_pressed()
	
	if k[K_RIGHT]:
		shouldIRun = True
		#jump = True
		playerVelocityX = 2.5
	elif k[K_LEFT]:
		shouldIRun = True
		#jump = True
		playerVelocityX = -1.5
	# elif k[K_DOWN]:
	# 	playerVelocityY = 2.5
	# 	print(playerPosY) 
	elif k[K_SPACE]:
		if playerPosY <= 360:
			print("yo playerPos Y equal to 360")
			playerVelocityY = -2.5
			# if playerPosY <= 250:
			# 	print("playerposy is <= 250")
			# 	playerVelocityY = 2.5
			# if playerPosY > 360:
			# 	print("stopping")
			# 	playerVelocityY = 0
			# 	playerPosY = 360
			# 	shouldIRun = False
			# else:
		# 	print("yo im prob screwing up the code")
		# 	playerVelocityY = 0
	else:
		playerVelocityX = 0

	#max cords
	if playerPosY <= 250:
		playerVelocityY = 2.5
	if playerPosY > 360:
		playerVelocityY = 0
		playerPosY = 360
	#################################################################	
	#moving player on x axis
	playerPosX += playerVelocityX

	circlePosX = startScrollingPosX
	stagePosX += -playerVelocityX

	#should move player on Y axis
	playerPosY += playerVelocityY

	circlePosY = startScrollingPosY
	stagePosY += -playerVelocityY
	###############################################################
	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))
	
	# rel_y = stagePosY % bgHeight
	# DS.blit(bg, (rel_y + bgHeight, 0))
	# if rel_y > H:
	# 	DS.blit(bg, (rel_y, 0))

	pygame.draw.circle(DS, WHITE, (int(circlePosX), int(playerPosY - 25)), int(circleRadius), 0)

	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)

############

