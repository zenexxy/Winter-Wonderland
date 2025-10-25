from pygame.locals import *
from ICS_Shapes import *   
import time                 # Import the time module for time-related functions
import math                 # Import the math module for calculations

# Constants for the game window and colors
WINDOW_WIDTH = 800      # The width of the game window (in pixels)
WINDOW_HEIGHT = 600     # The height of the game window (in pixels)
FPS = 120               # The maximum framerate for the game (in frames per second)

# RGB color to use throughout the code
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY = (128, 128, 255)
BLACK = (0, 0, 0)
BROWN = (92, 64, 51)
GREEN2 = (34, 139, 34)
ORANGE = (235, 137, 33)
YELLOW = (253, 184, 19)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Game state variable to control the main loop
gameOver = False

# Variables for timing and movement
now = time.time()            # Track the current time
horizontalMovement = 5  
verticalMovement = 0       
angleSun = 0               
angleMoon = 180              
image = pygame.image.load("moon.png")  # Load the moon image for rendering

# Main game loop
while not gameOver:
    
    random.seed(now) 
    
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user closes the window, end the game
            gameOver = True

    
    backgroundChange = 64 + math.sin(math.radians(angleMoon)) * 47.75
    def background():
        renderRectangle(window, 400, 150, 800, 300, (backgroundChange, backgroundChange, 254), 0)
    
    background()  # Call the background function to draw the sky

    # Star
    starChange = 191 + math.sin(math.radians(angleSun)) * 64
    starRadius = 1
    starRadius2 = 1
    def stars(x, y):
        renderCircle(window, x, y, starRadius2, (starChange, starChange, 255))  # Draw a star
    
    for i in range(1000):  # Generate 1000 random stars
        starX = random.randint(0, 800)
        starY = random.randint(0, 300)
        stars(starX, starY)
    
    # Sun movement settings
    sunRadius = 50
    centerX = 400
    centerY = 450
    sunOrbit = 400

    # Sun
    def sun(x, y, radius):
        renderCircle(window, x, y, radius, YELLOW)  # Render the sun as a yellow circle

    # Increment the sun's angle for orbital movement
    angleSun += 0.1
    for i in range(1):
        # Calculate the new position of the sun based on its orbit
        orbitX = math.cos(math.radians(angleSun)) * sunOrbit
        orbitY = math.sin(math.radians(angleSun)) * sunOrbit
        sunX = centerX + orbitX
        sunY = centerY + orbitY

        sun(sunX, sunY, sunRadius)  # Draw the sun

    # Moon movement settings
    moonRadius = 30
    mooncenterX = 400
    mooncenterY = 450
    moonOrbit = 400

    # Position and update the moon
    window.blit(image, (mooncenterX, mooncenterY))  # Draw the moon at its initial position
    angleMoon += 0.1
    for i in range(1):
        # Calculate the new position of the moon based on its orbit
        orbitX = math.cos(math.radians(angleMoon)) * moonOrbit
        orbitY = math.sin(math.radians(angleMoon)) * moonOrbit
        moonX = mooncenterX + orbitX
        moonY = mooncenterY + orbitY

    # Resize and redraw the moon at its new position
    image = pygame.transform.scale(image, (120, 70))
    window.blit(image, (moonX, moonY))

    # Draw the ground as a white rectangle
    renderRectangle(window, 400, 450, 800, 300, WHITE, 0)

    # Cloud
    radius = 0
    radius2 = 0
    cloudshape = 18
    horizontalMovement += 0.5
    def cloudBlack(window, x, y, radius):
        renderCircle(window, x + cloudshape, y, radius, BLACK)  # Render cloud outlines
        renderCircle(window, x - cloudshape, y, radius, BLACK)
        renderCircle(window, x, y + cloudshape, radius, BLACK)
        renderCircle(window, x, y - cloudshape, radius, BLACK)
        renderCircle(window, x, y, radius, BLACK)
    
    def cloudWhite(window, x, y, radius2):
        renderCircle(window, x + cloudshape, y, radius2, WHITE)  # Render cloud fill
        renderCircle(window, x - cloudshape, y, radius2, WHITE)
        renderCircle(window, x, y + cloudshape, radius2, WHITE)
        renderCircle(window, x, y - cloudshape, radius2, WHITE)
        renderCircle(window, x, y, radius2, WHITE)
    
    random.seed(now) 
    
    for i in range(20):  # Generate 15 black clouds with random positions and sizes
        
        radius = random.randint(20, 40)
        radius2 = radius - 1
        cloudx = random.randint(0, 800) + horizontalMovement
        while cloudx > 800:  # Wrap clouds around the screen
            cloudx -= 800
        
        cloudBlack(window, cloudx, random.randint(0, 250), radius)
    
    random.seed(now) 

    for i in range(20):  # Generate 15 white clouds with random positions and sizes
        
        radius = random.randint(20, 40)
        radius2 = radius - 1
        cloudx = random.randint(0, 800) + horizontalMovement
        while cloudx > 800:  # Wrap clouds around the screen
            cloudx -= 800
        
        cloudWhite(window, cloudx, random.randint(0, 250), radius2)


    # Tree
    treeLeaf = 40              # Distance between trees
    treeWidth = 150            # Initial width of the tree
    treeWidthDecrease = 10     # Amount by which the tree width decreases with each layer
    treeHeight = 90            # Height of each triangular tree layer
    treeTrunk = 50             # Height of the tree trunk
    treeOutline = 1            # Thickness of the tree outline
    
    def tree(window, x, y, treeWidth, height):
        # Render the tree outline as black triangles
        renderTriangle(window, x, y, treeWidth, height, BLACK, 0)
        renderTriangle(window, x, y - treeLeaf, treeWidth - treeWidthDecrease, height, BLACK, 0)
        renderTriangle(window, x, y - treeLeaf * 2, treeWidth - treeWidthDecrease * 2, height, BLACK, 0)
        renderTriangle(window, x, y - treeLeaf * 3, treeWidth - treeWidthDecrease * 3, height, BLACK, 0)

        # Render the tree fill as green triangles
        renderTriangle(window, x, y, treeWidth, height - treeOutline, GREEN2, 0)
        renderTriangle(window, x, y - treeLeaf, treeWidth - treeWidthDecrease - treeOutline, height - treeOutline, GREEN2, 0)
        renderTriangle(window, x, y - treeLeaf * 2, treeWidth - treeWidthDecrease * 2 - treeOutline, height - treeOutline, GREEN2, 0)
        renderTriangle(window, x, y - treeLeaf * 3, treeWidth - treeWidthDecrease * 3 - treeOutline, height - treeOutline, GREEN2, 0)

        # Render the tree trunk as a rectangle
        renderRectangle(window, x, y + treeTrunk, 20, 20, BLACK, 0)  # Trunk outline
        renderRectangle(window, x, y + treeTrunk, 18, 18, BROWN, 0)  # Trunk fill
    
    for i in range(8):  # Generate 8 random trees
        treeX = random.randint(0, 800)  # Random horizontal position for the tree
        treeY = random.randint(300, 350)  # Random vertical position for the tree
        tree(window, treeX, treeY, treeWidth, treeHeight)

    # Snowman rendering settings
    snowmanX = 75              # Vertical distance between snowman
    radiusDifference = 10      # Difference in radius between each snowman 
    radius = 60                # Radius of the base snowman 
    radiusBody = 5             # Radius of snowman buttons and eyes
    armWidth = 50              # Length of snowman arms
    armLength = 10             # Thickness of snowman arms
    
    def snowman(window, x, y, radius):
        # Render snowman arms as rectangles
        renderRectangle(window, x + radius, y - snowmanX, armWidth, armLength, BROWN, 35)  # Right arm
        renderRectangle(window, x - radius, y - snowmanX, armWidth, armLength, BROWN, 325) # Left arm

        # Render snowman body as circles with outlines and fills
        renderCircle(window, x, y, radius, BLACK)                  # Base outline
        renderCircle(window, x, y - snowmanX, radius - radiusDifference, BLACK)  # Middle outline
        renderCircle(window, x, y - snowmanX * 2, radius - radiusDifference * 2, BLACK)  # Head outline
        
        renderCircle(window, x, y, radius - 1, WHITE)             # Base fill
        renderCircle(window, x, y - snowmanX, radius - radiusDifference - 1, WHITE)  # Middle fill
        renderCircle(window, x, y - snowmanX * 2, radius - radiusDifference * 2 - 1, WHITE)  # Head fill

        # Render snowman buttons
        renderCircle(window, x, y - snowmanX, radiusBody, BLACK)  # Middle button
        renderCircle(window, x, y - snowmanX / 2, radiusBody, BLACK)  # Lower button
        renderCircle(window, x, y, radiusBody, BLACK)  # Base button

        # Render snowman eyes
        renderCircle(window, x - 20, y - snowmanX * 2.2, radiusBody, BLACK)  # Left eye
        renderCircle(window, x + 20, y - snowmanX * 2.2, radiusBody, BLACK)  # Right eye

        # Render snowman nose as a triangle
        renderTriangle(window, x, y - snowmanX * 1.8, 17, 32, BLACK, 180)   # Nose outline
        renderTriangle(window, x, y - snowmanX * 1.8, 15, 30, ORANGE, 180)  # Nose fill

    for i in range(4):  # Generate 4 random snowman
        randomSnowmanX = random.randint(0, 800)  # Random horizontal position
        randomSnowmanY = random.randint(500, 600)  # Random vertical position
        snowman(window, randomSnowmanX, randomSnowmanY, radius)

    # Snowfall rendering settings
    snowX = random.randint(0, 800)  # Random initial horizontal position
    snowY = 0  # Start snowflakes at the top of the screen
    verticalMovement += 0.5  # Increment vertical movement for snowflakes

    def snow(x, y):
        # Render a snowflake as a small white circle with a black outline
        renderCircle(window, x, y, 4, BLACK)  # Outline
        renderCircle(window, x, y, 3, WHITE)  # Fill

    for i in range(250):  # Generate 250 random snowflakes
        snowX = random.randint(0, 800)  # Random horizontal position
        snowY = random.randint(0, 600)  # Random vertical position
        while snowY + verticalMovement > 600:  # Wrap snowflakes back to the top
            snowY -= 600
        snow(snowX, snowY + verticalMovement)  # Draw the snowflake at its new position

    # Flip the display to render all elements on the screen
    pygame.display.flip()

    # Cap the game loop at the specified frames per second (FPS)
    pygame.time.Clock().tick(FPS)
