#print("Hello from addTwo")
#take two numbers from user and print the sum


#Is the input a number?
def IsNum(userInput):
    return bool(userInput.isdigit() or isinstance(userInput, float))

#While not a number, keep prompting
def TryAgain(userInput):
    while not IsNum(userInput):
        userInput = input("That's not a number I can add; try again: ")
    return userInput


num1 = input("Give me a number: ")
num1 = TryAgain(num1)
num2 = input("Give me another number: ")
num2 = TryAgain(num2)
print(num1 + " + " + num2 + " = " + str((float(num1) + float(num2))))