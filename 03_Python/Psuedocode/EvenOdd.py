import random

#print("Hello from Even Odd")

#get 10 random numbers
#print out how many are even (right),
#how many are odd (left)
#how many are zero

counter = 0
zeroCount = 0
evenCount = 0
oddCount = 0
theNum = 0

while counter < 10:
    #get a new random number
    theNum = random.randint(0,100)
    print(theNum)
    if theNum == 0: # is zero
        zeroCount = zeroCount + 1
    elif theNum % 2 == 1: #is odd
        oddCount = oddCount + 1
    else: #is even
        evenCount = evenCount + 1
    counter = counter + 1

print("Zero Count: " + str(zeroCount))
print("Right Count: " + str(evenCount))
print("Left Count: " + str(oddCount))