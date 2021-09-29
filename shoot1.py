import pygame

pygame.init()

#create game window
screen = pygame.display.set_mode((800, 600))

#title and icon
title = 'pumpkin shooter'
icon = pygame.image.load('data/alienn.png')
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

