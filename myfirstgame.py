# Comments will be used to explain the program step by step.
# This sis a very simple game coded with pygame.
# It contains 1 `player´ object, 3 `enemy´ objects and 1 `prize´ object.
# The player can be moved around by using the up, down, right and left arrows.
# If the player collides with any enemy object, they lose and the game ends.
# If the player collides with the prize object, they win and the game ends.

import os, sys
import pygame # Imports a game library
import random # Import to generate random numbers

pygame.init() # This initializes the pygame modules

# To display the screen, first we need to set the width and height, so we will assign them to variables:

x = 100
y = 100
velocity = 50
scr_width = 1100
scr_height = 800
screen = pygame.display.set_mode((scr_width,scr_height))

pygame.display.set_caption("First game")

# Now we need to create the player and the enemies.

player = pygame.image.load("player.jpg")
enemy = pygame.image.load("monster.jpg")
monster = pygame.image.load("monster.jpg")
villain = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")
# Now we need the width and height of the images.

player_height = player.get_height()
player_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
monster_height = monster.get_height()
monster_width = monster.get_width()
villain_height = villain.get_height()
villain_width = villain.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

# The position of the player.

playerXPosition = 50
playerYPosition = 25

#The enemies position.

enemyXPosition = 500
enemyYPosition = random.randint(0, scr_height - enemy_height)

monsterXPosition = scr_width/1.5
monsterYPosition = random.randint(0, scr_height - monster_height)

villainXPosition = scr_width
villainYPosition = random.randint(0, scr_height - villain_height)

# Now the prize position

prizeXPosition = scr_width * 1.5
prizeYPosition = random.randint(0, scr_height - prize_height)

# This checks if the up, down, right or left key is pressed.

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# Now we are entering the loop of the game.

while 1:  # This is a looping structure that will loop the indented code until you tell it to stop

    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))  # This draws the player image to the screen at the position that was specified
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    screen.blit(villain, (villainXPosition, villainYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    for event in pygame.event.get():

        # This event checks if the user quits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

        # After events are checked for in the for loop above and values are set,
        # check key pressed values and move player accordingly.


    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < scr_height - player_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyRight == True:
        if playerXPosition < scr_width - player_width:
            playerXPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1

        # Check for collision of the player with the enemies and the prize.
        # To do this we need bounding boxes around the images of the player, enemies and the prize.
        # We the need to test if these boxes intersect. If they do then there is a collision.

        # Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemies:

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    villainBox = pygame.Rect(villain.get_rect())
    villainBox.top = villainYPosition
    villainBox.left = villainXPosition

    # Now for the prize.

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:

    if playerBox.colliderect(enemyBox) or playerBox.colliderect(monsterBox) or playerBox.colliderect(villainBox):
        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    # If the player collides with the prize object, the user wins.

    if playerBox.colliderect(prizeBox):
        # Display winning status to the user:

        print("You win!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    # Make the enemies approach the player.

    enemyXPosition -= 0.15
    monsterXPosition -= 0.15
    villainXPosition -= 0.15
    prizeXPosition -= 0.15











