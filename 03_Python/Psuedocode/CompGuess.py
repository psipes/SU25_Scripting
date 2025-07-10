import random
#min/max INCLUSIVE

#print("Hello from Compguess")

#computer prints out number between 0 and user defined maximum number

#while playagain loop
#user defined number
#comp num

#while user does not input y or n, ask user for y or n. 
# y return true, n return false
def CheckContinue():
    playAgain = "a"
    while playAgain != "Y" or playAgain != "N":
        playAgain = input("Would you like to add another number? > Y/N ")
        if str.upper(playAgain) == "Y":
            return True
        if str.upper(playAgain) == "N":
            return False
        
#check if letter
def InputIsAlpha(userInput):
    if userInput.isalpha():
        return True
    else:
        return False
    
#check if space
def InputIsSpaces(userInput):
    if userInput.isspace():
        return True
    else:
        return False
    
#check if enter key
def InputIsEnter(userInput):
    if len(userInput) < 1:
        return True
    else:
        return False
    
#master error check
def TryAgain(userInput):
    while InputIsAlpha(userInput) or InputIsEnter(userInput) or InputIsSpaces(userInput):
        userInput = input("Invalid Entry, I need a number: ")
    return userInput


userMax = "a"
compNum = "a"

userMax = input("Give me a maximum whole number: ")
userMax = TryAgain(userMax)
compNum = random.randint(0,int(userMax)) #python is max INCLUSIVE, add one to make sure num is included
print(compNum)

while CheckContinue():
    userMax = input("Give me a maximum whole number: ")
    userMax = TryAgain(userMax)
    compNum = random.randint(0,int(userMax)) #python is max INCLUSIVE, add one to make sure num is included
    print(compNum)

