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

#placeholder water table
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


#placeholder for sand table
#this is a separate map because or sand has a wibbly edge that won't meet flush
#plus we're going to put some seaweed behind it
sandEdges = [pygame.image.load("dirt00.png"),
             pygame.image.load("dirt01.png"),
             pygame.image.load("dirt02.png"),
             pygame.image.load("dirt03.png"),
             pygame.image.load("dirt04.png"),
             pygame.image.load("dirt05.png"),
             pygame.image.load("dirt06.png"),
             pygame.image.load("dirt07.png")]

sandInner = [pygame.image.load("dirtIn00.png"),
             pygame.image.load("dirtIn01.png"),
             pygame.image.load("dirtIn02.png"),
             pygame.image.load("dirtIn03.png")]
m = "m" #top edge
u = "u" #inside

sandMap = [m, m, m, m, m, m, m, m,
           u, u, u, u, u, u, u, u]

for i, item in enumerate(sandMap):
    if sandMap[i] == m:
        sandMap[i] = random.choice(sandEdges)
    if sandMap[i] == u:
        sandMap[i] = random.choice(sandInner)


flora = [pygame.image.load("grass00.png"),
         pygame.image.load("grass01.png"),
         pygame.image.load("grass02.png"),
         pygame.image.load("grass03.png"),
         pygame.image.load("grass04.png"),
         pygame.image.load("grass05.png"),
         pygame.image.load("grass06.png"),
         pygame.image.load("grass07.png"),
         pygame.image.load("grass08.png"),
         pygame.image.load("grass09.png"),
         pygame.image.load("grass10.png"),
         pygame.image.load("grass11.png"),
         pygame.image.load("rock00.png"),
         pygame.image.load("rock01.png")]

floraMap = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate(floraMap):
    floraMap[i] = random.choice(flora)


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
    lFishx.append(random.randint(fishies[0].get_width()*-4, width))
    #start between score buffer and bottom - fish size
    lFishy.append(random.randint(scorebuffer*2, height - fishies[0].get_height()*3))
    #randomize speed
    lFishSpeed.append((.1 + random.random()) / 25)
    counter += 1



score = 0
scoreFont = pygame.font.SysFont("Arial", 30)
scoreText = scoreFont.render("Score: " + str(score), False, (255, 255, 255))





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
    if pygame.mouse.get_pressed()[0]: #left clicky
        coords = pygame.mouse.get_pos()
        counter = 0
        while counter < lFish:
            #box collision check
            if coords[0] >= lFishx[counter] and coords[0] <= lFishx[counter] + fishies[0].get_width() and coords[1] >= lFishy[counter] and coords[1] <= lFishy[counter] + fishies[0].get_height():
                #reset
                #add image
                lFishImage[counter] = random.choice(fishies)
                #start off screen
                lFishx[counter] = 0 - random.randint(fishies[0].get_width(), fishies[0].get_width()*4)
                #start between score buffer and bottom - fish size
                lFishy[counter] = random.randint(scorebuffer*2, height - fishies[0].get_height()*3)
                #randomize speed
                lFishSpeed[counter] = (.1 + random.random()) / 25
                score += 1
                scoreText = scoreFont.render("Score: " + str(score), False, (255, 255, 255))
                break
            counter += 1
    
    #print (score)
    ########
    #UPDATE
    ########
    counter = 0
    while counter < lFish:
        #if fish has exited the right hand side of the screen
        if lFishx[counter] >= width:
            #reset
            #add image
            lFishImage[counter] = random.choice(fishies)
            #start off screen
            lFishx[counter] = 0 - random.randint(fishies[0].get_width(), fishies[0].get_width()*4)
            #start between score buffer and bottom - fish size
            lFishy[counter] = random.randint(scorebuffer*2, height - fishies[0].get_height()*3)
            #randomize speed
            lFishSpeed[counter] = (.1 + random.random()) / 25

        else:
            #increase movement left
            lFishx[counter] += lFishSpeed[counter]
        counter+=1

    ########
    #DRAW
    ########

    
    #DRAW THE WATER FIRST
    count = 0 #count rows
    countx = 0 #count columns
    screen.fill((0, 0, 0))
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

    
    for i, item in enumerate(floraMap):
        screen.blit(floraMap[i],((flora[0].get_width()) * i, (height - sandEdges[0].get_height() * 3 + 12 )))
    #DRAW SAND ON TOP OF THAT
    countx = 0
    count = 0
    for i, item in enumerate(sandMap):
        screen.blit(sandMap[i], (sandEdges[0].get_width() * countx, (height - sandEdges[0].get_height()*2) + sandEdges[0].get_height() * count))
        if (i+1)%tiles == 0:
            count = count + 1 #go down one row
            countx = 0 #reset to left
        else:
            countx = countx + 1

    screen.blit(scoreText,(0,0))
    #flip display
    pygame.display.flip()

########
#QUIT
########
pygame.display.quit()