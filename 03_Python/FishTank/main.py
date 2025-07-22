#three standard imports for pygame games
import sys
import pygame
import random

########
#LOAD
########
pygame.init()

tiles = 8
scorebuffer = 30
wave = pygame.image.load("wave.png")
water = pygame.image.load("water.png")
waveW = wave.get_width()
waveH = wave.get_height()

#placeholder table
v = "v" #wave
o = "o" #water
waterMap = [v, v, v, v, v, v, v, v,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o]

#switch over values to images
for i, item in enumerate(waterMap):
    if waterMap[i] == v:
        waterMap[i] = wave
    if waterMap[i] == o:
        waterMap[i] = water


#Setup the screen
width = tiles * waveW
height = tiles * waveH + scorebuffer
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fish Tank")



#FISH LOADER
fishies = [pygame.image.load("fish_blue.png"),
           pygame.image.load("fish_brown.png"),
           pygame.image.load("fish_green.png"),
           pygame.image.load("fish_orange.png"),
           pygame.image.load("fish_red.png")]

counter = 0
lFish = 7
lFishImage = []
lFishx = []
lFishy = []
lFishSpeed = []


while counter < lFish:
    #add image
    lFishImage.append(random.choice(fishies))
    #start off screen
    lFishx.append(0)
    #start between score buffer and bottom - fish size
    lFishy.append(random.randint(scorebuffer*2, height - fishies[0].get_height()))
    #randomize speed
    lFishSpeed.append((.1 + random.random()) / 50)
    counter += 1




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
    counter = 0
    while counter < lFish:
        lFishx[counter] += lFishSpeed[counter]
        counter+=1

    ########
    #DRAW
    ########
    #DRAW THE WATER FIRST
    count = 0 #count rows
    countx = 0 #count columns

    for i, item in enumerate(waterMap):
        screen.blit(waterMap[i], (0 + (waveW * countx), scorebuffer + (waveH * count)))
        if (i+1)%tiles == 0:
            count = count + 1 #go down one row
            countx = 0 #reset to left
        else:
            countx = countx + 1

    #DRAW THE FISH ON TOP
    counter = 0
    while counter < lFish:
        screen.blit(lFishImage[counter], (lFishx[counter], lFishy[counter]))
        counter +=1

    #flip display
    pygame.display.flip()

########
#QUIT
########
pygame.display.quit()