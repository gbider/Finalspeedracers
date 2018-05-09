import pygame
import time
pygame.init()

#help from https://pythonprogramming.net/displaying-text-pygame-screen/

display_width = 1280
display_height = 720

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("YOU LOST")
clock = pygame.time.Clock()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    #game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, (124,10,2))
    return textSurface, textSurface.get_rect()

