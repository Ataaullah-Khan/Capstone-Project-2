# Game with 3 enemies, 1 player and 1 prize

import pygame                                                           # Imports game library
import random                                                           # Generates random numbers
pygame.init()                                                           # Initialize pygame

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))          # Create screen with width and height

pygame.display.set_caption("My First Game! ")                           # Customize window name


# create the player, prize and enemies and with the images found in this folder

player = pygame.image.load("player.png")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("enemy.png")
enemy3 = pygame.image.load("enemy.png")
prize = pygame.image.load("prize.png")

# Get the width and height of the images in order to do boundary detection

player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()


# Store the positions of the player, prize and enemy as variables.
# Widths and heights are minused to start all images on screen.


player_x = 0                                                            # Starts at midleft of the screen
player_y = screen_height / 2

prize_x = screen_width - (prize_width)                                  # Positioned at right of the screen with random height
prize_y = random.randint(0, screen_height - prize_height)

enemy1_x = (screen_width * 0.25) - (enemy1_width/2)                     # Starts between bottom left and mid bottom of the screen
enemy1_y = 0

enemy2_x = (screen_width *0.5) - (enemy2_width/2)                       # Starts at mid top of the screen
enemy2_y = screen_height - enemy2_height

enemy3_x = (screen_width *0.75) - (enemy3_width/2)                      # Starts between mid bottom and bottom right
enemy3_y = 0

key_up = False                                                          # Declare key variables
key_down = False
key_left = False
key_right = False

# The Game loop. Updates the screen to represent real time gameplay

while 1:    # Loops until told to stop

    screen.fill(0)                                                      # Clears the screen
    screen.blit(player, (player_x, player_y))                           # Draws the necessary game items at specified positions
    screen.blit(enemy1, (enemy1_x, enemy1_y))   
    screen.blit(enemy2, (enemy2_x, enemy2_y))
    screen.blit(enemy3, (enemy3_x, enemy3_y))
    screen.blit(prize, (prize_x, prize_y))

    pygame.display.flip()                                               # Updates the screen

    for event in pygame.event.get():                                    # Loops throught game events

        if event.type == pygame.QUIT:                                   # Quits the game
            pygame.quit()
            exit(0)

        # This event checks if the key is pressed down and changes boolean value.

        if event.type == pygame.KEYDOWN:                                

            if event.key == pygame.K_UP:
                key_up = True

            if event.key == pygame.K_DOWN:
                key_down = True

            if event.key == pygame.K_RIGHT:
                key_right = True

            if event.key == pygame.K_LEFT:
                key_left = True

        # This event checks if the key is released and changes boolean value.

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                key_up = False

            if event.key == pygame.K_DOWN:
                key_down = False

            if event.key == pygame.K_RIGHT:
                key_right = False

            if event.key == pygame.K_LEFT:
                key_left = False

    # check key pressed values and move player accordingly.

    if key_up == True:
        if player_y > 0 :
                player_y -= 1

    if key_down == True:
        if player_y < screen_height - player_height:
                player_y += 1

    if key_left == True:
        if player_x > 0:
                player_x -=1

    if key_right == True:
        if player_x < screen_width - player_width:
                player_x +=1

    # Create boxed around the images of the player, prize and enemies.
    # This is used to check for collisions.

    player_box = pygame.Rect(player.get_rect())
    player_box.top = player_y                                           # Updates the box postion, making it stay around the image.
    player_box.left = player_x

    enemy1_box = pygame.Rect(enemy1.get_rect())
    enemy1_box.top = enemy1_y
    enemy1_box.left = enemy1_x

    enemy2_box = pygame.Rect(enemy2.get_rect())
    enemy2_box.top = enemy2_y
    enemy2_box.left = enemy2_x

    enemy3_box = pygame.Rect(enemy3.get_rect())
    enemy3_box.top = enemy3_y
    enemy3_box.left = enemy3_x

    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = prize_y
    prize_box.left = prize_x

    # Detects collsion and executes the relevant code.

    if player_box.colliderect(enemy1_box):
        print("You were eaten")
        pygame.quit()
        exit(0)

    if player_box.colliderect(enemy2_box):
        print("You were eaten")
        pygame.quit()
        exit(0)

    if player_box.colliderect(enemy3_box):
        print("You were eaten")
        pygame.quit()
        exit(0)

    if player_box.colliderect(prize_box):
        print("You win!")
        pygame.quit()
        exit(0)


    # Moves the enemies along the X & Y axis. Player moves until it reaches the end of the screen.

    if enemy1_y < screen_height:
            enemy1_y += 0.1
            enemy1_x += 0.05

    if enemy2_y < screen_height:
            enemy2_y -= 0.05
            enemy2_x -= 0.15

    if enemy3_y < screen_height:
        enemy3_y += 0.075
        enemy3_x += 0.005

    if player_x < screen_width - player_width :
        player_x += 0.15
            
            

# References
# Free Icons made by www.freepik.com  & www.flaticon.com/authors/vectors-market
# https://www.youtube.com/watch?v=i6xMBig-pP4&t
