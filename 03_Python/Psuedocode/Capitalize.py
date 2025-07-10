#print("Hello from Cap")

#take a user string and print out capitalized version
#check if letter
#.isalpha()

#check if number
def CheckIfNum(userInput):
    if userInput.isdigit():
        print("Numbers can't be capitalized!")
    return userInput.isdigit()
#check if spaces
def CheckIfSpaces(userInput):
    if userInput.isspace():
        print("Spaces can't be capitalized!")
    return userInput.isspace()
#check if Empty
def CheckIfEmpty(userInput):
    if not userInput:
        print("Empty entry can't be capitalized!")
        return True
    else:
        return False
#check if already capped
def CheckIfCapped(userInput):
    if userInput == str.upper(userInput):
        print("This is already capitalized!")
        return True
    else:
        return False
#check everything
def CheckAll(userInput):
    while CheckIfNum(userInput) or CheckIfSpaces(userInput) or CheckIfEmpty(userInput) or CheckIfCapped(userInput):
        userInput = input("Type something else: ")
    return userInput

strToUpper = input("Write something to capitalize: ")
print(str.upper(CheckAll(strToUpper)))

#at its most simple below is all we have to do:
#print(str.upper(input("Write something to capitalize: ")))