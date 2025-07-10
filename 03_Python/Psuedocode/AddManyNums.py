#print("Hello from add many")

#add as many user inputted numbers together as wanted



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
        userInput = input("That's not a number I can add, try again: ")
    return userInput
     
#add a new number (user input) to the total. Return total.
def AddNewNum(total):
    newNum = "a"
    newNum = input("Next Number to add: ")
    #error check
    newNum = TryAgain(newNum)
    total = float(total) + float(newNum)
    return total

sum = 0
sum = AddNewNum(sum)
print (sum)
while CheckContinue():
    sum = AddNewNum(sum)
    print(sum)
print("The total sum is: " + str(sum))