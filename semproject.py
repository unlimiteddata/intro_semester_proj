import Draw
# I hereby certify that this program is solely the result of my own work and 
# is in compliance with the Academic Integrity policy of the course syllabus
# and the academic integrity policy of the CS department.

# Amira Isenberg
# Semester Project Fall 2021
# This program consists of three separate earthquake animations,
# each one displaying what happens during an earthquake of one of
# three magnitudes (3.0, 6.0, or 9.5). The user can click on any 
# of the buttons on the home screen to be directed to an 
# animation of an earthquake of the selected magnitude. 
# See the end of the project code for the sources of the information provided.
###############################################################################

# CONSTANTS:
GROUND_X  = 100            # starting x value of the ground
GROUND_Y  = 400            # starting y value of the ground
CANVAS_W  = 800            # canvas width
CANVAS_H  = 600            # canvas height
HOUSE_X   = 600            # starting x value of the house
HOUSE_Y   = 310            # starting y value of the house
OFFICE_X  = 150            # starting x value of the office building
OFFICE_Y  = 150            # starting y value of the office building
OFFICE_W  = 240            # office building width
OFFICE_H  = 250            # office building height
TREE_X    = 400            # starting x value of the tree
TREE_Y    = 255            # starting y value of the tree
FAULT_H   = 30             # height of the individual pieces of the fault line

# CUSTOM COLORS:
light_brown = Draw.color(143, 67, 49) 
dark_brown  = Draw.color(102, 48, 35)
light_blue  = Draw.color(112, 112, 255)
light_gray  = Draw.color(212,212,212)
darker_gray = Draw.color(156, 156, 156)
turquoise   = Draw.color(14, 237, 234)

# Draw the home screen: 
def homescreen():
    Draw.setBackground(light_gray)
    Draw.setFontFamily('Bahnschrift SemiLight')
       
    # Draw cracks (so the screen looks like cracked cement):
    Draw.picture("crack_hs.gif",36,5)
    Draw.picture("crack_hs.gif",673,32)
    
    # The title of the project, with a shadow behind for added impact:
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(26)
    Draw.setFontBold(True)
    Draw.setColor(Draw.color(96,96,96)) 
    Draw.string("AMIRA'S EARTHQUAKE ANIMATION", 99, 99)
    Draw.setColor(Draw.BLACK)
    Draw.string("AMIRA'S EARTHQUAKE ANIMATION", 101, 101) 
    
    # Introductory message with instructions:
    Draw.setFontBold(False)
    Draw.setColor(Draw.color(36,36,36)) 
    Draw.setFontSize(13) 
    Draw.string("Each one of the buttons below represents a number on the Richter scale, \nwhich is used to measure the magnitude of an earthquake and \nhypothetically ranges from 1-10. In actuality, the largest magnitude ever \nrecorded for an earthquake is 9.5, while earthquakes below 2 occur quite \nfrequently and cause little to no damage. You can press each button to see \nan animation of an earthquake of that magnitude.", 110, 155)

    # Draw 3 light blue boxes with darker gray outlines to serve as buttons
    # With the x values 250 pixels apart, starting at x=50:
    for x in range(50,551,250):
        Draw.setColor(turquoise)
        Draw.filledRect(x,350,200,150)
        Draw.setColor(darker_gray)
        Draw.rect(x,350,200,150)
        
    # Draw the numbers in the center of the buttons:
    # Dictionary format is: desired x value of number:"number"
    magnitudes = {120:"3.0",370:"6.0",620:"9.5"}
    Draw.setColor(Draw.BLACK)
    for k in magnitudes:
        Draw.setFontSize(36)
        Draw.string(magnitudes[k],k,395)

# 4 different right triangles for the interlocking pieces of the ground:
def downTriangle1(x,y,wide,high): # downwards facing right triangle
    coords = [x,       y,
              x+wide,  y,
              x+wide,  y+high]
    Draw.filledPolygon(coords) 
    
def downTriangle2(x,y,wide,high): # right triangle facing opposite direction 
    coords = [x,y,
              x+wide,y,
              x,y+high]
    Draw.filledPolygon(coords)     
    
def upTriangle1(x,y,wide,high):   # upwards facing right triangle
    coords = [x,          y,
              x,          y+high,
              x+wide,     y+high]
    Draw.filledPolygon(coords)
    
def upTriangle2(x,y,wide,high):   # right triangle facing opposite direction
    coords = [x,       y,
              x-wide,  y+high,
              x,       y+high]
    Draw.filledPolygon(coords)    
    
# Draw a lighter background for the ground to account for any gaps,
# filling the entire bottom of the canvas:
def groundBack():
    Draw.setColor(light_brown) 
    Draw.filledRect(0,GROUND_Y,CANVAS_W,CANVAS_H)         

# Draw the left part of the ground using the triangle functions from above for
# the edge, and rectangles to fill in the rest:
# Numbers are arbitrary. 
def ground1(x=GROUND_X,y=GROUND_Y): 
    # Call the function to draw the background that fills the ground gaps
    groundBack() 
    
    Draw.setColor(dark_brown)
    upTriangle1(x,y,35,30)
    downTriangle2(x,y+30,35,30)
    upTriangle1(x,y+30,45,50)
    downTriangle2(x,y+80,39,34) 
    upTriangle1(x,y+70,60,50)  
    downTriangle2(x,y+120,60,50) 
    upTriangle1(x,y+110,75,55)
    downTriangle2(x,y+165,75,50) 
    upTriangle1(x,y+140,80,60)
    Draw.filledRect(0,400,x,y)

# Draw the right part of the ground using the triangle functions from above for
# the edge, and rectangles to fill in the rest:
# Numbers are arbitrary.     
def ground2(x=GROUND_X,y=GROUND_Y):        
    Draw.setColor(dark_brown)
    downTriangle1(x,y,50,45)
    upTriangle2(x+50,y,30,45)
    downTriangle1(x+18,y+45,30,28)
    upTriangle2(x+60,y+65,30,25)
    downTriangle1(x+30,y+90,35,30)
    upTriangle2(x+73,y+110,30,25)
    downTriangle1(x+45,y+135,35,30)
    upTriangle2(x+90,y+155,30,25)
    downTriangle1(x+60,y+180,35,30)
    
    Draw.filledRect(x+300,y,400,300)
    Draw.filledRect(x+48,y,255,110)
    Draw.filledRect(x+60,y+110,255,40)
    Draw.filledRect(x+80,y+150,255,60)

# Draw two types of parallelograms to use in drawing the fault line:
def fault1(x,y,wide,high):           # looks like a line with positive slope
    coords = [x,            y,
              x-wide,       y,
              x-high-wide,  y+high,
              x-high,       y+high]
    Draw.filledPolygon(coords)  
    
def fault2(x,y,wide,high):           # looks like a line with negative slope
    coords = [x,            y,
              x+wide,       y,
              x+high+wide,  y+high,
              x+high,       y+high]
    Draw.filledPolygon(coords)  
 
# Combine the two parallelogram functions defined above to make a fault line: 
# Numbers are arbitrary.
def faultLine(x=GROUND_X,y=GROUND_Y,w=5,h=FAULT_H):    
    Draw.setColor(light_brown)
    
    fault2(x,y,          w,h)
    fault1(x+35,y+30,    w,h/2)
    fault2(x+14,y+45,    w,h)
    fault1(x+49,y+75,    w,h/2)
    fault2(x+28,y+90,    w,h)
    fault1(x+63,y+119,   w,h/2)
    fault2(x+43,y+134,   w,h)
    fault1(x+78,y+165,   w,h/2)
    fault2(x+58,y+180,   w,h)
    
# Draw an isosceles triangle for the roof of the house:    
def houseTriangle(x,y,wide,high):   
    coords = [x,             y,
              x-(wide/2), (y+high),
              x+(wide/2), (y+high)]
    Draw.setColor(Draw.DARK_BLUE)
    Draw.filledPolygon(coords)    
    
# Draw the body of the house with the roof on top and a door in front:
def house(x=HOUSE_X,y=HOUSE_Y): 
    houseWidth  = 100              # width of the house body
    houseHeight = 90               # height of the house body
    doorWidth   = 20               # width of the door for the house
    doorHeight  = 40               # height of the door for the house  
    
    # Draw the rectangle for the house body:
    Draw.setColor(light_blue)
    Draw.filledRect(x,y,houseWidth,houseHeight) 
    
    # Draw the rectangle for the door of the house:
    # Starting x value of the door is centered at the middle of the house (
    # houseWidth/2) and the middle of the door (doorWidth/2)
    # Starting y value of the door is located at y + the height of the house 
    # - the height of the door to ensure that the door hits the bottom exactly    
    Draw.setColor(Draw.DARK_GRAY)
    Draw.filledRect(x+((houseWidth /2)-(doorWidth/2)), \
                    y+(houseHeight-doorHeight),doorWidth, \
                   doorHeight)
    
    # Draw the triangle for the roof of the house:
    # Starting x value of triangle is x + half of the house width 
    # Starting y value of triangle is y - the height of the house
    houseTriangle(x+(houseWidth/2),y-houseHeight,houseWidth,houseHeight)  

# Draw the windows of the office building:
def officeWindows(x=OFFICE_X,y=OFFICE_Y):
    officeMargin = 50      # The margin around the edge of the office building
    windowMargin = 25      # The margin around each individual window
    windowHeight = windowWidth = 30   # window height and width = 30
    
    Draw.setColor(Draw.DARK_GRAY) 

    # The starting x value of each window is the starting x value of the office
    # building + the margin of the office building:
    windowX= x + officeMargin 

    # Each x value is the starting x value of the window + ((window width + 
    # window margin) * column number)
    # Each y value is the row number, starting at 180 and increasing by the
    # office building margin each time (for a total of 4 rows):
    for row in range(180,331,officeMargin): 
        for col in range(3):
            Draw.filledRect(windowX+((windowWidth + windowMargin)*col),row,\
                            windowWidth,windowHeight)  
        
# Draw the full office building, including the windows:
def office(x=OFFICE_X,y=OFFICE_Y):
    #Draw the rectangle for the body:
    Draw.setColor(Draw.LIGHT_GRAY)
    Draw.filledRect(x,y,OFFICE_W,OFFICE_H)
    
    # Draw the windows: 
    officeWindows(x,y)

#Draw the tree by importing a picture of a tree:   
def tree(x=TREE_X,y=TREE_Y):  
    Draw.picture("tree.gif",x,y)

# Draw the background for all 3 animations: 
def animationBackground():
    Draw.setBackground(Draw.WHITE) 
    
    # Draw all the pieces of the animation- the tree, both pieces of the 
    # ground, the house, the office, and the fault line:
    tree()
    ground1()
    ground2()
    house()
    office()
    faultLine(GROUND_X,GROUND_Y,2,FAULT_H)      
    Draw.show() 

# Function that moves the house and the office by a designated dx (change in x):
def structureMove(dx):
    house(HOUSE_X+dx,HOUSE_Y)
    office(OFFICE_X+dx,OFFICE_Y)

# Function that moves the tree by a designated dx (change in x) and dy
# (change in y). It is separate from the house and office because it is further
# behind on the canvas (so that the roots are not in front of the ground)
# (dy is defaulted to zero because dy is only not zero once): 
def treeMove(dx,dy=0):
    tree(TREE_X+dx,TREE_Y+dy)
    
# Function that moves the x values of the different pieces of the ground by 
# dx (the parameter). w = the width of the fault line:
def groundMove(dx,w):
    ground1(GROUND_X+dx,GROUND_Y)
    ground2(GROUND_X+dx,GROUND_Y)     
    faultLine(GROUND_X+dx,GROUND_Y,w) 

# Function that increases the width of the fault line by 0.5 until it reaches 
# the number passed in as the limit. This mimics what happens to a fault line
# during a real earthquake: 
def faultWiden(limit):
    for i in range(5,limit):
        faultLine(GROUND_X,GROUND_Y,i+0.5,FAULT_H)
        Draw.show(200) 
    Draw.show()  
    
# Function that makes the second piece of the ground move down to mimic the 
# motion of tectonic plates that occurs during earthquakes.
# Meaning of the parameters:
# w = width of the fault line
# dx = amount of change for the x value; dy = amount of change for the y value
def groundDrop(w,dx,dy=1):
    # dx and dy are the same, but it would look too confusing if the y changed
    # by dx: 
    dy = dx 

    # Clear the canvas, then show the same components, except with the tree,
    # second part of the ground, house, office, and fault line moved by the dx
    # and dy passed in for each animation: 
    Draw.clear()
    treeMove(dx,dy)    
    ground1()   
    ground2(GROUND_X+dx*2,GROUND_Y+dy)  
    structureMove(dx)       # moves the house and office 
    faultLine(GROUND_X+dx,GROUND_Y+dy)  
    Draw.show(800)

# Function that shakes the ground a certain number of times.
# Meaning of the parameters:  
# dx = the amount of change for the x value; n = number of times the ground 
# shakes; w = width of fault line                    
def groundShake(dx,n,w):  
    for i in range(n):
        # Draw the components of the animation normally. The other items 
        # besides for the ground are drawn as well because the screen clears 
        # later on:   
        Draw.clear()
        tree()
        ground1()
        ground2() 
        # The w is needed here because it changes later:         
        faultLine(GROUND_X,GROUND_Y,w)  
        house()
        office()
        Draw.show(40) 
        
        # Draw the ground and fault line with the x increased by the dx that 
        # was passed in. The other components are drawn normally as well 
        # because the screen is cleared:
        Draw.clear()
        tree()
        groundMove(w,dx)  # moves both pieces of the ground and the fault line
        house()
        office()   
        Draw.show(50)  
    
# Function that makes all of the components of the animation besides for the
# ground shake. 
# Meaning of the parameters:
# dx = amount of change for the x value of everything but the ground; 
# n = number of times the components shake; w = width of the fault line
def componentShake(dx,n,w):
    for i in range(n):
        # Draw all components normally:
        Draw.clear()
        tree()
        ground1()
        ground2()            
        house()
        office()
        # The w is needed here because it changes later: 
        faultLine(GROUND_X,GROUND_Y,w) 
        Draw.show(100)
        
        # Draw all components, except moving the tree, office, and house by dx 
        # (and dy for the house and office)
        Draw.clear()
        treeMove(dx)
        ground1()
        ground2() 
        structureMove(dx)     # moves the house and office
        # The w is needed here because it changes each time this function is 
        # invoked: 
        faultLine(GROUND_X,GROUND_Y,w) 
        Draw.show(100) 

# Function for the back button that appears in each animation:              
def backButton():
    back = "on"
    
    # Draw the rectangle for the button:
    Draw.setColor(Draw.VIOLET)
    Draw.filledRect(650,50,115,50)
    
    # Draw a string that fills the rectangle ("BACK"):
    Draw.setFontSize(30)
    Draw.setColor(Draw.BLACK)
    Draw.string("BACK",652,50)
    
    while back == "on":          # while the back button is on the screen:
        if Draw.mousePressed():  # if user clicks, log the x and y of the click
            newX = Draw.mouseX()        
            newY = Draw.mouseY()       
            
      # If the user clicks on the button, go back to the home screen:
            if ((newX >= 650 and newX <= 765) and
                (newY >= 50 and newY <= 100)):
                # The program no longer needs to check if the user clicked on
                # the button or not: 
                back = "off" 
                # Clear the screen and then show the home screen:
                Draw.clear()
                homeButtons()
                Draw.show() 
    
# Animation for an earthquake of magnitude 3:    
def animation1():  
    dx = 1
    n = 2
    
    # The maximum width for the fault line: 
    faultMax = 8
    
    # The width of the fault line is faultMax - 0.5 (because the faultWiden 
    # function increments by 0.5 and goes up to 0.5 before the actual maximum 
    # value): 
    faultWidth = faultMax - 0.5 
    
    # Draw the animation background:
    animationBackground()
    
    # Make the fault's width increase to the maximum established above (8):
    faultWiden(faultMax)
    
    # Make the second piece of the ground drop: w = faultWidth and dx = 4:
    groundDrop(faultWidth,4)
    
    # Make the ground shake: dx = 1, n = 2, w = faultWidth: 
    groundShake(dx,n,faultWidth)
    
    # Make the components shake: dx = 1, n = 2, w = faultWidth:
    componentShake(dx,n,faultWidth)
    Draw.show()
   
    # Information about earthquake of this magnitude:  
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(12)
    Draw.string("This is an earthquake of magnitude 3. These earthquakes are considered to be minor, \nas they are generally felt by many people but cause no damage. Earthquakes of this \nmagnitude are pretty common- they happen between 12,000-100,000 times per year. \nBecause they are so minor and cause so little damage, there is little data about the \naverage cost of damages.",10,10)  
    Draw.show(800)    # Wait a few seconds for the user to read the information 
    
    # Draw the back button for the user to return to the home screen:
    backButton()
    Draw.show()

# Animation for an earthquake of magnitude 6:    
def animation2():  
    dx = 5
    n = 4   
    
    # The maximum width for the fault line:     
    faultMax = 10 
    
    # The width of the fault line is faultMax - 0.5 (because the faultWiden 
    # function increments by 0.5 and goes up to 0.5 before the actual maximum 
    # value): 
    faultWidth = faultMax - 0.5     
    
    # Draw the animation background:    
    animationBackground() 
    
    # Make the fault's width increase to the maximum established above (10):    
    faultWiden(faultMax)
    
    # Make the second piece of the ground drop: w = faultWidth and dx = 6:
    groundDrop(faultWidth,6)
    
    # Make the ground shake: dx = 5, n = 4, w = faultWidth:     
    groundShake(dx,n,faultWidth)
    
    # Make the components shake: dx = 5, n = 4, w = faultWidth:    
    componentShake(dx,n,faultWidth)
    Draw.show() 
    
    # Information about earthquake of this magnitude    
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(12)
    Draw.string("This is an earthquake of magnitude 6. These earthquakes are categorized as strong, \nas they cause moderate damage in populated areas. They are not as common as \nearthquakes with lower magnitudes, happening between 20-200 times a year. An \nearthquake of this magnitude has historically cost from as little as $1 million to a \nwhopping $7.84 billion in damages, adjusting for inflation. This cost depends greatly \non the population density of the area, as well as how urban it is.",10,10)  
    Draw.show(800)   # Wait a few seconds for the user to read the information 
    
    # Draw the back button for the user to return to the home screen:    
    backButton()
    Draw.show()
    
# Animation for an earthquake of magnitude 9.5:   
def animation3():  
    dx = 10
    n = 9
    
    # The maximum width for the fault line:     
    faultMax = 12
    
    # The width of the fault line is faultMax - 0.5 (because the faultWiden 
    # function increments by 0.5 and goes up to 0.5 before the actual maximum 
    # value): 
    faultWidth = faultMax - 0.5     
    
    # Draw the animation background:    
    animationBackground()
   
    # Make the fault's width increase to the maximum established above (12):        
    faultWiden(faultMax)
    
    # Make the second piece of the ground drop: w = faultWidth and dx = 8:
    groundDrop(faultWidth,8)  
    
    # Make the ground shake: dx = 10, n = 9, w = faultWidth:     
    groundShake(dx,n,faultWidth)
    
    # Make the components shake: dx = 10, n = 9-3 (so it doesn't shake for too
    # long), w = faultWidth:
    componentShake(dx,n-3,faultWidth)
    
    # Draw three cracks- two on the office building and one on the house:
    # Numbers are arbitrary.
    Draw.picture("crack.gif",OFFICE_X+10,OFFICE_Y+OFFICE_H-35)
    Draw.picture("crack.gif",OFFICE_X+OFFICE_W-40,OFFICE_Y+5)
    Draw.picture("crack.gif",HOUSE_X+7,HOUSE_Y+60)
    Draw.show()  
    
    # Information about earthquake of this magnitude:
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(12)
    Draw.string("This is an earthquake of magnitude 9.5. Any earthquake above magnitude 8 is \nconsidered to be a great earthquake and involves severe destruction, as well as loss of \nlife over large areas. A 9.5 magnitude earthquake has only occurred once in recorded \nhistory- in Valdivia, Chile in 1960. Adjusting for inflation, it cost the Chilean government \n$9.39 billion. It caused 3000 injuries, 2000 deaths, and destroyed almost 60,000 houses.",10,10)  
    Draw.show(800)    # Wait a few seconds for the user to read the information 
    
    # Draw the back button for the user to return to the home screen:    
    backButton()
    Draw.show()

# Function that makes the buttons on the home screen functional and shows the 
# appropriate animation when clicked: 
def homeButtons():
    home = "on"
  
    while home == "on":    # While home screen is being shown:
        homescreen()       # Draw home screen 
        Draw.show()
        
        if Draw.mousePressed():  # if user clicks, log x and y of the click
            newX = Draw.mouseX()  
            newY = Draw.mouseY()  
            
            # If the user clicks on button 1: 
            if ((newX >= 50 and newX <= 250) and 
                (newY >= 350 and newY <= 500)):
                # Make buttons nonfunctional and clear home screen:                
                home = "off"
                Draw.clear()
                
                # Draw animation 1:
                animation1()
                Draw.show()
                
            # If the user clicks on button 2:
            elif ((newX >= 300 and newX <= 500) and 
                (newY >= 350 and newY <= 500)):
                # Make buttons nonfunctional and clear home screen:
                home = "off"
                Draw.clear()
                
                # Draw animation 2:
                animation2()               
                Draw.show()
                
            # If the user clicks on button 3:
            elif ((newX >= 550 and newX <= 750) and 
                (newY >= 350 and newY <= 500)):
                # Make buttons nonfunctional and clear home screen:                
                home = "off"
                Draw.clear()
                
                # Draw animation 3:
                animation3()
                Draw.show()                

# Main function that calls all the relevant functions for the code to run:      
def main():  
    Draw.setCanvasSize(CANVAS_W, CANVAS_H)  
    
    # Call the button function for the home screen (which ends up calling all 
    # the other functions):
    homeButtons() 
    
main()

## SOURCES: ##
# https://www.britannica.com/science/Richter-scale 
# https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/search 
