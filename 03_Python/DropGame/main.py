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
scene = 2

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

playY = 300
btnMargin = 10
btnFont = pygame.font.SysFont("Arial", 30)
playWord = btnFont.render("PLAY", False, green)
quitWord = btnFont.render("QUIT", False, green)
restartWord = btnFont.render("RESTART", False, orange)

#rect = screen, color, (x, y, width, height, curve)
playBtn = pygame.draw.rect(screen, black,((width/2)-(playWord.get_width()/2)- btnMargin, playY-btnMargin, playWord.get_width() + (btnMargin*2), playWord.get_height() + (btnMargin *2)), 0)
quitBtn = pygame.draw.rect(screen, black,((width/4)-(quitWord.get_width()/2)- btnMargin, playY-btnMargin, quitWord.get_width() + (btnMargin*2), quitWord.get_height() + (btnMargin *2)), 0)
restartBtn = pygame.draw.rect(screen, green,((width * .75)-(restartWord.get_width()/2)- btnMargin, playY-btnMargin, restartWord.get_width() + (btnMargin*2), restartWord.get_height() + (btnMargin *2)), 0)
#------------------
#Game Play Setup (Release the Slimes)
counter = 0
numOfThings = 7 #controls number of slimes that exist
slimeImage = []
slimeX = []
slimeY = []
slimeSpeed = []
baseSpeed = .1
speedMulti = 1.2

while counter < numOfThings:
    #add a random slime to the slime pool
    slimeImage.append(random.choice(slimes))
    #randomized x value between screen size
    slimeX.append(random.randint(0, width - slime.get_width()))
    #randomized y value between screen size
    slimeY.append(0 - random.randint(slime.get_height(), slime.get_height() * 2 ))
    #randomized speed
    slimeSpeed.append((baseSpeed + random.random())/100)
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
    if pygame.mouse.get_pressed()[0]: #if left click
        coords = pygame.mouse.get_pos()
        if scene == 0: #if title screen
            if pygame.Rect.collidepoint(playBtn, coords):
                scene = 1 #go to game
        
        elif scene == 1:#gameplay
            counter = 0
            while counter < numOfThings:
                #box collision check
                if coords[0] >= slimeX[counter] and coords[0] <= slimeX[counter] + slime.get_width() and coords[1] >= slimeY[counter] and coords[1] <= slimeY[counter] + slime.get_height():
                    #Send it back to top with new identity
                    slimeImage[counter] = random.choice(slimes)
                    slimeX[counter] = random.randint(0, width - slime.get_width())
                    slimeY[counter] = 0 - random.randint(slime.get_height(), slime.get_height() * 2 )
                    #increase the speed
                    slimeSpeed[counter] *= speedMulti
                counter +=1  

        else: #gameover screen
            #if gameover button is clicked
            if pygame.Rect.collidepoint(quitBtn, coords):
                gameOver = True
            #if restart button is clicked
            if pygame.Rect.collidepoint(restartBtn, coords):
                counter = 0
                while counter < numOfThings:
                    slimeImage[counter] = random.choice(slimes)
                    slimeX[counter] = random.randint(0, width - slime.get_width())
                    slimeY[counter] = 0 - random.randint(slime.get_height(), slime.get_height() * 2)
                    slimeSpeed[counter] = (baseSpeed + random.random())/ 100
                    counter += 1
                scene = 0


    ########
    #UPDATE
    ########
    if scene == 1: #game play scene
        counter = 0
        while counter < numOfThings:
            #check if hit bottom of screen
            if slimeY[counter] + slime.get_height() > height:
                #game over, man
                scene = 2
            #step down if not
            slimeY[counter] += slimeSpeed[counter]
            counter +=1

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

        #button changes if mouse is hovering over it
        coords = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(playBtn, coords): #green button
            playBtn = pygame.draw.rect(screen, green,((width/2)-(playWord.get_width()/2)- btnMargin, playY-btnMargin, playWord.get_width() + (btnMargin*2), playWord.get_height() + (btnMargin *2)), 0)
        else: #normal button
            playBtn = pygame.draw.rect(screen, black,((width/2)-(playWord.get_width()/2)- btnMargin, playY-btnMargin, playWord.get_width() + (btnMargin*2), playWord.get_height() + (btnMargin *2)), 0)
            screen.blit(playWord, ((width/2)-(playWord.get_width()/2), playY))
    
    elif scene == 1: #game play
        screen.fill(green)
        #draw slimes
        counter = 0
        while counter < numOfThings:
            screen.blit(slimeImage[counter], (slimeX[counter], slimeY[counter]))
            counter += 1

    else: #gameover
        screen.fill(black)
        #text
        screen.blit(gameOverTitle, (width/2 - gameOverTitle.get_width()/2, titleY))
        screen.blit(slime, ((width/2)-(gameOverTitle.get_width()/2)-slime.get_width(), titleY+ (gameOverTitle.get_height()-slime.get_height())))       
        screen.blit(rSlime, ((width/2) + (gameOverTitle.get_width()/2), titleY+ (gameOverTitle.get_height()-slime.get_height())))

        #buttons
        #Quit
        coords = pygame.mouse.get_pos()
        if pygame.Rect.collidepoint(quitBtn, coords):
            #if mouse hovers over quit button it'll be green
            quitBtn = pygame.draw.rect(screen, green,((width/4)-(quitWord.get_width()/2)- btnMargin, playY-btnMargin, quitWord.get_width() + (btnMargin*2), quitWord.get_height() + (btnMargin *2)), 0)
        else:
            quitBtn = pygame.draw.rect(screen, orange,((width/4)-(quitWord.get_width()/2)- btnMargin, playY-btnMargin, quitWord.get_width() + (btnMargin*2), quitWord.get_height() + (btnMargin *2)), 0)
            screen.blit(quitWord, ((width/4) - (quitWord.get_width()/2), playY))
        
        #Restart
        if pygame.Rect.collidepoint(restartBtn, coords):
            #if mouse hovers over restart, turn button orange
            restartBtn = pygame.draw.rect(screen, orange,((width * .75)-(restartWord.get_width()/2)- btnMargin, playY-btnMargin, restartWord.get_width() + (btnMargin*2), restartWord.get_height() + (btnMargin *2)), 0)
        else:
            restartBtn = pygame.draw.rect(screen, green,((width * .75)-(restartWord.get_width()/2)- btnMargin, playY-btnMargin, restartWord.get_width() + (btnMargin*2), restartWord.get_height() + (btnMargin *2)), 0)
            screen.blit(restartWord,((width *.75) - (restartWord.get_width()/2), playY))
    
    #flip the page/render the display
    pygame.display.flip()

########
#QUIT
########
pygame.display.quit()