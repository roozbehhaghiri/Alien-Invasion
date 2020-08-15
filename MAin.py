import os
import pygame
import math
from Enemy import ENEMY
from Bullet import BULLET
import random

pygame.init()

# Game screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("my first game")
background = pygame.image.load("Background.jpg").convert()

# Player details
playerimg = pygame.image.load("Player.png")
playerx = 370
playery = 480
playerx_change = 0


def player():
    screen.blit(playerimg, (playerx, playery))


# Enemy details
enemys = list()
level_enemys = 10
enemy_speed = 0.5
for i in range(0, level_enemys):
    enemys.append(ENEMY())


def enemy_add():
    screen.blit(enemy.enemyimg, (enemy.enemyx, enemy.enemyy))


# Bullet details
bullet = BULLET()
bullet_state = "ready"
bullety = 900
bullet_change = 3


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet.bulletimg, (x + 16, y + 10))


# Score
scort_result = 0
font = pygame.font.Font("Home.ttf", 32)

def showpoint():
    score = font.render("Score= " + str(scort_result), True, (199, 199, 199), )
    screen.blit(score, (10, 10))

# Level
level = 1
levelfont = pygame.font.Font("Home.ttf", 32)

def showlevel():
    levelnumber = font.render("Level: "+ str(level), True, (199, 199, 199))
    screen.blit(levelnumber, (700, 10))


# Collision
def iscollision(ex, bx, ey, by):
    if math.sqrt((math.pow(ex - bx, 2)) + (math.pow(ey - by, 2))) < 27:

        return True
    else:
        return False


running = True

# Icon of screen
icon = pygame.image.load("Umberela.png")
pygame.display.set_icon(icon)


# Gameover
def gameover(enemys):
    for enemy in enemys:
        if enemy.enemyy >= 416:
            return True


# Game Loop
while running:

    # Getting actions in the Game

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Movement of player and bullet if he press a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -1.3
            elif event.key == pygame.K_RIGHT:
                playerx_change = 1.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet.bulletx = playerx
                    bullety = playery
                fire_bullet(bullet.bulletx, bullety)

        # Movements end if he release the key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerx_change = 0

    # Screen color
    screen.fill((199, 199, 199))
    screen.blit(background, (0, 0))

    # Player position changes
    playerx += playerx_change
    if playerx > 736:
        playerx = 736
    if playerx <= 0:
        playerx = 0

    # Enemy postion change
    for enemy in enemys:
        if enemy.enemy_change:
            enemy.enemyx += enemy_speed
        else:
            enemy.enemyx -= enemy_speed

        if enemy.enemyx >= 736:
            enemy.enemy_change = False
            enemy.enemyy += 20
        elif enemy.enemyx <= 0:
            enemy.enemyy += 20
            enemy.enemy_change = True

    # Fire a bullet
    if bullet_state is "fire":
        fire_bullet(bullet.bulletx, bullety)
        bullety -= bullet_change
    if bullety <= 0:
        bullet_state = "ready"
        bullety = playery
        bullet.bulletx = playerx

    # Collision

    for i in range(0, len(enemys)):
        if iscollision(enemys[i].enemyx, bullet.bulletx, enemys[i].enemyy, bullety):
            del enemys[i]
            bullety = 900
            bullet_state = "ready"
            scort_result += 1
            break
    showpoint()
    showlevel()
    player()
    for enemy in enemys:
        enemy_add()

    pygame.display.update()

    if len(enemys) == 0:
        level += 1
        level_enemys += random.randint(2, 4)
        enemy_speed += 0.2
        for i in range(0, level_enemys):
            enemys.append(ENEMY())

    if gameover(enemys):
        break

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    # High Score
    hs = open("Highscore.txt", "r+")
    lhs = int(hs.read())
    if scort_result > lhs:
        hs.close()
        os.remove("Highscore.txt")
        hs =open("Highscore.txt", "w")
        hs.write(str(scort_result))
    # Screen color
    screen.fill((199, 199, 199))
    screen.blit(background, (0, 0))
    font = pygame.font.Font("Home.ttf", 80)
    fontscore = pygame.font.Font("Home.ttf", 50)
    highscore = fontscore.render("High Score: " + str(scort_result), True, (199, 199, 199))
    score = font.render("GAME OVER ", True, (199, 199, 199), )
    screen.blit(highscore, (300, 300))
    screen.blit(score, (250, 200))
    pygame.display.update()

