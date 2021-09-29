import pygame
import random

pygame.init()

#create game window
screen = pygame.display.set_mode((800, 600))

#title and icon
title = 'pumpkin shooter'
icon = pygame.image.load('data/alienn.png')
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

#background
bg = pygame.image.load('data/backgrounddd.png')

#player
player_img = pygame.image.load('data/rockett.png')
playerX = 368                                            #800-400[half screen]-32[half image]
playerY = 516                                            #600-64[size]-20[above the screen]

playerX_change = 0

# enemy
enemy_img = pygame.image.load('data/enemyy.png')
enemyX = random.randint(0,736)                                  #where enemy should be at X-axis
enemyY = random.randint(20,120)                                 #where enemy should at Y-axis


game_on = True
while game_on:
    #background RGB-red green blue  [0-255]
    #screen.fill((0, 0, 0))  -gives complete black
    #screen.fill((0, 255, 0)) -gives green
    screen.fill((45, 51, 71))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():           # pakka event,pygame in statement
        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:     # pakka event,pygame in statement
            if event.key == pygame.K_LEFT:   # pakka event,pygame in statement
                playerX_change = -0.2
               # print("left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
               # print("right arrow is pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #player movement
                   # playerX += 1    #moves rightside
                   # playerX += -1  # moves leftside
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:                  #800-64
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

#steps:
    #player_img with position points,changing points
    #create function
    #events/key
    #player movement
    #call functiom
