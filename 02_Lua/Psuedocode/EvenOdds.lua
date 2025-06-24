--print("Hello from evenOdds")

--random number 10 times, see how many are even and how many odd
--variables
zerocount = 0
evencount = 0
oddcount = 0
counter = 0
checkNum = nil --random number

--randomizatioin
--set up random number generator
math.randomseed(os.time()) -- randomize the randomizer
math.random() ; math.random() ; math.random() -- get rid of any old values

while counter < 10 do
    --get random num(checkNum)
    checkNum = math.random(0, 100)
    

    --check if 0
    if checkNum == 0 then
        zerocount = zerocount + 1
        print(checkNum.." is 0")

    --if not 0
    else
        --check if odd
        if math.fmod(checkNum, 2) == 1 then 
            oddcount = oddcount + 1
            print(checkNum.." is odd")
        --even
        else
            evencount = evencount +1
            print(checkNum.." is even")
        end
    end
    counter = counter + 1
end

print("Zeroes: "..zerocount)
print("Left: "..oddcount)
print("Right: "..evencount)