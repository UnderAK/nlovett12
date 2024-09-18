'''
schoolhouseHackathonProj.py
@author: Noah L. & Aarav T
created 9/16/24
'''
#theme: [ADD THEME HERE]
#ideas (general):
'''
 - connect it back to learning/schoolhouse?
 -
'''
#imports
import pygame
pygame.init()
#variables
playerSpeed = 5
location = [100, 100]
player = pygame.Rect(0,0,0,0)
isJumping = False
jumpCount = 0
#colors
white = (255, 255, 255)
black = (0, 0, 0)
#screen setup
screen = pygame.display.set_mode((600, 600))
TITLE = pygame.display.set_caption("GAME NAME GOES HERE")
onScreen = pygame.Rect(0, 0, screen.get_width(), screen.get_height())
#main
while True:
    #lets us exit game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill(white)
    #add player to screen (player is currently a black rectangle)
    player = pygame.Rect(location, (60, 40))
    pygame.draw.rect(screen, black, player)
    #gets which keys are pressed
    keys = pygame.key.get_pressed()
    #if WASD is pressed & not colliding w/ border, update player location by playerSpeed
    if keys[pygame.K_a] and player.left > onScreen.left:
        #move left
        location[0] -= playerSpeed
    if keys[pygame.K_d] and player.right < onScreen.right:
        #move right
        location[0] += playerSpeed
    if keys[pygame.K_SPACE] and not isJumping:
        isJumping = True
        jumpCount = 10  # Adjust this value for jump height
    if isJumping:
        # Simulate jump arc
        jumpCount -= 1
    else:
        jumpCount = 0
    if player.bottom > onScreen.bottom:  # Check for bottom collision
            isJumping = False
            jumpCount = 0  # Reset jump count
    location[1] -= jumpCount  # Move player up
    #screen lims
    if player.left < onScreen.left:
        location[0] = onScreen.left
    if player.right > onScreen.right:
        location[0] = onScreen.right - player.width
    if player.bottom > onScreen.bottom:
        location[1] = onScreen.bottom - player.height
    #update frame
    pygame.time.delay(50)
    pygame.display.update()
    
