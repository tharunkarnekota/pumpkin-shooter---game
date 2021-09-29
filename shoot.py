import pygame
import random
import math

pygame.init()

# create game window
screen = pygame.display.set_mode((800, 600))

# title and icon
title = 'pumpkin shooter'
icon = pygame.image.load('data/alienn.png')
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

# background
bg = pygame.image.load('data/backgrounddd.png')

# background music
pygame.mixer.music.load('data/preview.mp3')
pygame.mixer.music.play(-1)

# music
bullet_sound = pygame.mixer.Sound('data/Bulletshort.mp3')
explosion_sound = pygame.mixer.Sound('data/Bulletsound.mp3')

score = 0

#score font
score_font = pygame.font.Font('data/LibreBaskerville-Bold.ttf', 32)
scoreX = 10
scoreY = 10

#game over font
game_over_font = pygame.font.Font('data/LibreBaskerville-Bold.ttf', 64)
game_overX = 200
game_overY = 200  # 250

#restart font
restart_font = pygame.font.Font('data/LibreBaskerville-Bold.ttf', 32)
restartX = 180
restartY = 300


game_status = 'running'


def show_restart(x, y):
    restart_img = restart_font.render('To Restart The Game Press R', True, (255, 255, 255))  # rgb values
    screen.blit(restart_img, (x, y))


def show_game_over(x, y):
    global game_status
    game_over_img = game_over_font.render('GAME OVER', True, (255, 0, 0))  # rgb values
    screen.blit(game_over_img, (x, y))
    pygame.mixer.music.stop()
    game_status = 'end'  # its is local varable we need to make it global 58


def show_score(x, y):
    score_img = score_font.render('score: ' + str(score), True, (255, 255, 255))  # rgb values
    screen.blit(score_img, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def bullet(x, y):
    screen.blit(bullet_img, (x + 15, y + 5))

def iscollistion(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x2 - x1), 2)) + math.sqrt(math.pow((y2 - y1), 2))
    if distance < 30:
        return True
    else:
        return False

# player
player_img = pygame.image.load('data/rockett.png')
playerX = 368
playerY = 516

playerX_change = 0

# enemy
num_of_enemies = 6
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('data/enemyy.png'))
    enemyX.append(random.randint(0, 736))  # where enemy should be at X-axis
    enemyY.append(random.randint(20, 120))  # where enemy should at Y-axis
    enemyX_change.append(0.4)  # no need make append we can also make = as it is constant
    enemyY_change.append(30)  # no need make append we can also make = as it is constant

# bullet1
bullet_img = pygame.image.load('data/bullett.png')
bulletX = 0
bulletY = 516
bulletY_change = -0.8  # change value for increase or decrease of bullet speed
bullet_state = 'ready'

game_on = True
while game_on:
    # background RGB-red green blue  [0-255]
    # screen.fill((0, 0, 0))  -gives complete black
    # screen.fill((0, 255, 0)) -gives green
    screen.fill((45, 51, 71))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            # print("left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            # print("right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_state = 'fire'
                    bulletX = playerX
                    bullet(bulletX, bulletY)
                    bullet_sound.play()

            if event.key == pygame.K_r:
                if game_status == 'end':
                    game_status = 'running'
                    score = 0
                    playerX = 368
                    pygame.mixer.music.play(-1)
                    for i in range(num_of_enemies):
                        enemyX[i] = random.randint(0, 736)  # enemy default random location
                        enemyY[i] = random.randint(20, 120)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # bullet movement
    if bullet_state == 'fire':
        if bulletY < 10:
            bulletY = 516
            bullet_state = 'ready'
        bulletY += bulletY_change
        bullet(bulletX, bulletY)

    # enemy movement
    for i in range(num_of_enemies):

        # gameover
        if enemyY[i] > 466:
            show_game_over(game_overX, game_overY)
            show_restart(restartX, restartY)
            for j in range(num_of_enemies):
                enemyY[j] = 1200

        # * * *
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = 0.6  # enemy speed 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:  # 800-64
            enemyX[i] = 736
            enemyX_change[i] = -0.6  # enemy speed
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)

        # collection
        collision = iscollistion(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 516  # bullet default location
            bullet_state = 'ready'
            enemyX[i] = random.randint(0, 736)  # enemy default location
            enemyY[i] = random.randint(20, 120)
            score += 1
            explosion_sound.play()
            print(score)

    show_score(scoreX, scoreY)

        # playerX += 1    #moves rightside
        # playerX += -1    # moves leftside
    # player movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800-64
        playerX = 736

    player(playerX, playerY)

    pygame.display.update()


#keypoints:
    #.display.set_mode(length, breadth)
    #.image.load(address)
    #.display.set_caption                    #mw.title
    #.display.set_icon                       #mw.iconbitmap
    #.mixer.music.load
    #.mixer.music.play(-1)
    #.mixer.sound ,,, .play()
    #.font.Font('ttf address',size)


#steps:
    #import
    #create game window
    #title and icon
    #bg music
    #create variable1:
                    #bg
                    #bullet_sound
                    #explosion sound
    #create variable2_of_fonts:
                        #score_font
                        #restart_font
                        #gameover_font
    #assign_values[images]_for_fontVariable2 using function and display it on screen:
                                                                            #score_img
                                                                            #restart_img
                                                                            #gameover_img
    #create variable3 with values[images]:
                                       #player_img
                                       #enemy_img
                                       #bullet_img
    #display the variable3 on the screen using function
                                                    #bullet
                                                    #player
                                                    #enemy
    #only function for calculation
    #while:
        #screen
        #events:
            #quit
            #keydown:
                #k_left
                #k_right
                #k_space
                #k_r
            #keyup:
                #k_left
                #k_right
        #bullet_movement
        #enemy_movement:
                #gameover
                #enemy_movement
                #iscollision
        #show_score
        #player_movement
        #update