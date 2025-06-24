--print("Hello from Convert to Upper")
--Take a user string and return/print it as capitalized
function printUppercase()
    --variables
    local userInput = nil
    upperUserInput = nil

    --while user input is invalid or not able to be capitalized
    while (userInput == nil or userInput == "" or userInput == string.upper(userInput) or tonumber(userInput)) do
        print("What would you like to capitalize: ")
        userInput = io.read()
    end
    --once valid user input, convert to uppercase
    upperUserInput = string.upper(userInput)

    --print capitalized string
    print(upperUserInput)
    
end

function changeToUppercase()
    --variables
    local userInput = nil
    upperUserInput = nil

    --while user input is invalid or not able to be capitalized
    while (userInput == nil or userInput == "" or userInput == string.upper(userInput) or tonumber(userInput)) do
        print("What would you like to capitalize: ")
        userInput = io.read()
    end
    --once valid user input, convert to uppercase
    upperUserInput = string.upper(userInput)

    --print capitalized string
    --print(upperUserInput)
    return upperUserInput
end