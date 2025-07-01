--REMEMBER WITH OUR DEBUGGER F5 for debug, SHIFT F5 for non-debug
--This is your debug code. It goes at the very top of main.
if arg[2] == "debug" then
    require("lldebugger").start()
end

-- Game where multiple images fall from sky
-- User clicks to send them back to top 
-- Click images before they hit the bottom or game over 

--should have title screen, level 1, game over
function titleLoad()
    slimeFire = love.graphics.newImage("slime_fire.png")
    titleText = "Slime Drop"
    --Update the window to be titled the titleText
    love.window.setTitle(titleText) 
    
end

--Set up draw for the title WARNING, THIS IS HARDCODED FOR 800x600
function titleDraw()
    --create text at 100 pts
    love.graphics.setFont(love.graphics.newFont(100))
    --formatted text print (works for any size screen)
    love.graphics.printf(titleText, 0, 200, love.graphics.getWidth(), "center")

    --create a button
    love.graphics.setColor(1,1,1)
    --type, x, y, width, height, cornerx, cornery, segments
    --This is hard coded to be a button on the left half of a 800 x 600 screen
    love.graphics.rectangle("fill", 50, 450, 250, 100, 10, 10, 6)
    love.graphics.setColor(1,0,0)
    love.graphics.setFont(love.graphics.newFont(75))
    love.graphics.printf("PLAY", 50, 450, 250, "center")
    love.graphics.setColor(1,1,1) --reset color back to white so it doesn't bleed
end

--Create randomized table of stars
function randomizeStars()
    --setup randomization
    math.randomseed(os.time())
    math.random(); math.random(); math.random()

    count = 100 --number of stars we want on our canvas 
    stars = {} --this is the table of x, y values for our stars
    while count > 0 do
        stars[#stars+1] = math.random(0, love.graphics.getWidth()) --get random x value 
        stars[#stars+1] = math.random(0, love.graphics.getHeight()) --get random y value 
        count = count - 1 
    end
    return stars
end

--take a parameter of a table of x and y points and draw stars at those points
function drawStars(stars)
    --starglow (big brush, light opacity)
    love.graphics.setColor(math.random(), math.random(), math.random(), .22)
    love.graphics.setPointSize(10)
    love.graphics.points(stars)

    --center (small brush, high opacity)
    love.graphics.setColor(1,1,1,1)
    love.graphics.setPointSize(2)
    love.graphics.points(stars)
end
-----------------------------------------------------------------
-- LOAD ALL THE THINGS
--
-----------------------------------------------------------------
function love.load()
    --by default, Love sets your window to 800x600
    success = love.window.updateMode(800, 600)  
    starsTable = randomizeStars() --this creates our randomized table of stars 
    --load title stuff
    titleLoad()

    -- 0 = title screen
    -- 1 = game screen
    -- 2 = game over screen
    scene = 0

    --Set up spikes
    spikes = love.graphics.newImage("spikes.png")

    --Set up slime variables
    slimeF = love.graphics.newImage("slime_fire.png")
    slimeNums = 5 -- how many
    slimeX = {} -- where at (x)
    slimeY = {} -- where at (y)
    slimeSpeed = {} -- how fast 
    minSpeed = 10
    maxSpeed = 20
    speedMod = 1
    count = slimeNums

    --Randomization
    math.randomseed(os.time())
    math.random(); math.random(); math.random()

    --initially populate the slimes
    while count > 0 do
        --get an x value between 0 and width of screen minus width of slime 
        slimeX[#slimeX+1] = math.random(0, love.graphics.getWidth() - slimeF:getWidth())
        -- get a random y value between 1 and 2 slimes above window
        slimeY[#slimeY+1] = 0 -- math.random(slimeF:getHeight(), slimeF:getHeight()*2)
        -- get a random speed between min and max 
        slimeSpeed[#slimeSpeed+1] = math.random(minSpeed, maxSpeed)
        count = count - 1 --count down
    end

end
-----------------------------------------------------------------
-- CLICK ALL THE THINGS
--
-----------------------------------------------------------------
function love.mousepressed(x, y, button, istouch)
    --if it's left click
    if button == 1 then
        --if on title screen
        if scene == 0 then
            --if title screen
            --click play button
            --HARD CODED WARNING
            if x >= 50 and x <= 300 and y >= 450 and y <= 550 then
               scene = 1 -- go to game play 
            end
        end
        --in game
        if scene == 1 then
           --check EACH image and see if it has collided with the mouse click 
           for i, value in ipairs(slimeX) do
                if x >= slimeX[i] and x <= slimeX[i] + slimeF:getWidth() and y >= slimeY[i] and y <= slimeY[i] + slimeF:getHeight() then
                    --print ("hit in the thing")
                    --randomize
                    math.randomseed(os.time())
                    math.random(); math.random(); math.random()
                    --send back to top and change the speed
                    speedMod = speedMod + 1
                    maxSpeed = maxSpeed + speedMod
                    slimeX[i] = math.random(0, love.graphics.getWidth() - slimeF:getWidth())
                    slimeY[i] = 0 - math.random(slimeF:getHeight(), slimeF:getHeight() * 2)
                    slimeSpeed[i] = math.random(slimeSpeed[i], maxSpeed) --can only get faster
                    break --so that it only clicks ONE thing and not overlapping things
                end
           end
        end
    end
end

-----------------------------------------------------------------
-- UPDATE ALL THE THINGS
--
-----------------------------------------------------------------
function love.update(dt)
    --if gameplay scene
    if scene == 1 then
        for i, value in ipairs(slimeX) do
            if slimeY[i] + slimeF:getHeight() >= love.graphics.getHeight() - (spikes:getHeight()/2) then
                --print ("Over the Edge")
                love.event.quit("restart") --having "restart" will restart the thing
            end
            --Move slime 
            slimeY[i] = slimeY[i] + slimeSpeed[i] * dt
        end
    end

end

-----------------------------------------------------------------
-- DRAW ALL THE THINGS
--
-----------------------------------------------------------------
function love.draw()
    drawStars(starsTable)
    --TITLE SCREEN
    if scene == 0 then
        --draw the title screen
        titleDraw()
    end
    --GAMEPLAY
    if scene == 1 then
        --Draw spikes across the bottom of the screen 
        for x = 0, love.graphics.getWidth(), spikes:getWidth() do
            love.graphics.draw(spikes, x, love.graphics.getHeight() - spikes:getHeight())
        end
        --draw all the slimes
        for i, value in ipairs(slimeX) do
            love.graphics.draw(slimeF, slimeX[i], slimeY[i])
        end
    end
    --GAMEOVER
    if scene == 2 then
        --draw the game over screen
    end

end




--This gives us highlighting of error issues allong with our breakpoints
local love_errorhandler = love.errorhandler

function love.errorhandler(msg)
    if lldebugger then
        error(msg, 2)
    else
        return love_errorhandler(msg)
    end
end

