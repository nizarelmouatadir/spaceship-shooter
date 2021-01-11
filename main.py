import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('background.png')

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 500
playerX_change = 0

enemyImg = pygame.image.load('enemy.png')
enemyX = 0
enemyY = 50
gameover = pygame.image.load('game-over.png')

bulletImg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 510
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

collision_state = False

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def collision(enemyX, enemyY, bulletX, bulletY) :
    if enemyX == bulletX and enemyY == bulletY :
        global collision_state
        collision_state = True

running = True
while running:


    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                if bullet_state is "ready" :
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0 :
        playerX = 0
    elif playerX >= 739 :
        playerX = 739

    enemyX += 2
    if enemyX == 0 or enemyX == 740 :
        enemyX = 0
        enemyY += 50

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
