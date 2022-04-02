import math
import random
import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))

pygame.display.set_caption("Balloon Ace")

player = pygame.image.load('plane.png')
playerX = 0
playerY = 250
playerY_change = 0

ydot = []
ydotX = []
ydotY = []
ydotX_change = []
num_of_y = 6
for i in range(num_of_y):
    ydot.append(pygame.image.load('ydot.png'))
    ydotX.append(random.randint(700, 800))
    ydotY.append(random.randint(100, 500))
    ydotX_change.append(-0.2)
    pygame.display.update()


gdot = []
gdotX = []
gdotY = []
gdotX_change = []
num_of_g = 6
for i in range(num_of_g):
    gdot.append(pygame.image.load('gdot.png'))
    gdotX.append(random.randint(700, 800))
    gdotY.append(random.randint(100, 500))
    gdotX_change.append(-0.2)


def player1(x, y):
    screen.blit(player, (x, y))


def ydot1(x, y, i):
    screen.blit(ydot[i], (x, y))


def gdot1(x, y, i):
    screen.blit(gdot[i], (x, y))


missed_values = 0
font = pygame.font.Font('freesansbold.ttf', 32)
mtextX = 10
mtextY = 50


def missed_value(x, y):
    missed = font.render("Yellows Missed :" + str(missed_values), True, (0, 0, 0))
    screen.blit(missed, (x, y))


point_values = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def point_value(x, y):
    points = font.render("Points :" + str(point_values), True, (0, 0, 0))
    screen.blit(points, (x, y))


def isgCollision(gdotX, gdotY, playerX, playerY):
    distance = math.sqrt((math.pow(gdotX-playerX, 2))+(math.pow(gdotY-playerY, 2)))
    if distance < 50:
        return True
    else:
        return False


def isyCollision(ydotX, ydotY, playerX, playerY):
    distance = math.sqrt((math.pow(ydotX-playerX, 2))+(math.pow(ydotY-playerY, 2)))
    if distance < 50:
        return True
    else:
        return False


running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = -.15
            if event.key == pygame.K_UP:
                playerY_change = .15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerY += playerY_change
    for i in range(num_of_y):
        gdotX[i] += gdotX_change[i]
        ydotX[i] += ydotX_change[i]

        ycollision = isyCollision(ydotX[i], ydotY[i], playerX, playerY)
        if ycollision:
            ydotX[i] = random.randint(700, 800)
            ydotY[i] = random.randint(0, 600)

        gcollision = isgCollision(gdotX[i], gdotY[i], playerX, playerY)
        if gcollision:
            point_values += 1
            gdotX[i] = random.randint(700, 800)
            gdotY[i] = random.randint(0, 600)

    ydot1(ydotX[i], ydotY[i], i)
    gdot1(gdotX[i], gdotY[i], i)

    if playerY <= 0:
        playerY = 0
    elif playerY >= 530:
        playerY = 530

    if ydotX[i] <=0:
        missed_values += 1
        ydotX[i] = (random.randint(700, 800))
        ydotY[i] = random.randint(100, 500)


    if gdotX[i] <= 0:
        gdotX[i] = (random.randint(700, 800))
        gdotY[i] = random.randint(100, 500)

    player1(playerX, playerY)
    point_value(textX, textY)
    missed_value(mtextX, mtextY)
    pygame.display.update()





