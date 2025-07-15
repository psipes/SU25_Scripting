#three standard imports for pygame games
import sys
import pygame
import random

##########################
#-------------------------
# This is a game where you click sprites before they reach the bottom of the screen
# Game ends when sprite ends bottom of screen
#--------------------------
##########################

########
#LOAD
########
pygame.init() #starts the game/initialized everything

#scenes
# 0 = title, 1 = game, 2 = gameover/replay
scene = 0

#load slime images
slime = pygame.image.load("slimePurple.png")
slime2 = pygame.image.load("slimeGreen.png")
slime3 = pygame.image.load("slimeBlue.png")

slimes = [slime, slime2, slime3]

#flipped slime (for aesthetics)
rSlime = pygame.transform.flip(slime, True, False) #slime, horizontal flip, vertical flip

#Setup the Screen
width = 600
height = 400
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Don't Let the Slime Splat!")
pygame.display.set_icon(slime)

#define colors
green = (74, 93, 35)
orange = (243, 121, 78)
black = (0, 0, 0)

#------------------------------
#Title and Gameover Page Stuff
titleY = 100
titleFont = pygame.font.SysFont("Arial", 65)
slimeTitle = titleFont.render("It's Raining Slime", False, green)
gameOverTitle = titleFont.render("Slime Went Splat", False, green)


########
#GAME LOOP
########
gameOver = False
while gameOver == False:
    #quit event: the Pygame special
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    ########
    #MOUSE CLICKS
    ########

    ########
    #UPDATE
    ########

    ########
    #DRAW
    ########
    if scene == 0:
        screen.fill(orange)
        #centered title
        screen.blit(slimeTitle, ((width/2)-(slimeTitle.get_width()/2), titleY))
        #slime left
        screen.blit(slime, ((width/2)-(slimeTitle.get_width()/2)-slime.get_width(), titleY+ (slimeTitle.get_height()-slime.get_height())))       
        screen.blit(rSlime, ((width/2) + (slimeTitle.get_width()/2), titleY+ (slimeTitle.get_height()-slime.get_height())))

    #flip the page/render the display
    pygame.display.flip()

########
#QUIT
########