--add numbers from the user until they say that they're done

function printUserSum()
    --variables
    local done = false
    local sum = 0
    local userNum = nil
    local userChoice = nil

    while done == false do --user wants to add more
        while (userNum == nil or userNum == "" or not tonumber(userNum)) do
            print("Number to add to total: ")
            userNum = io.read()
        end
        --once valid, add userNum to current sum
        sum = sum + userNum
        --reset userNum for new number
        userNum = nil
        
        --check if user wants to add another number?
        print("Press Q to QUIT, any other key to CONTINUE: ")
        userChoice = io.read()
        if string.upper(userChoice)=="Q" then
            print("Your sum is: " .. sum)
            done = true
            break
        end
        userChoice = nil
    end
end