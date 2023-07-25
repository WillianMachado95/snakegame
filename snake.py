import pygame
import time
import random

pygame.init()

DIS_WIDTH = 800
DIS_HEIGHT = 600

blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,102)

dis = pygame.display.set_mode((DIS_WIDTH,DIS_HEIGHT))
pygame.display.set_caption("Snake by Senai")

snakeBlock = 20

eat = pygame.mixer.Sound("eat.wav")
death = pygame.mixer.Sound("death.wav")


def foodLocation():
    global foodX, foodY
    
    foodX = round(random.randrange(0,DIS_WIDTH-snakeBlock)/snakeBlock)*snakeBlock
    foodY = round(random.randrange(0,DIS_HEIGHT-snakeBlock)/snakeBlock)*snakeBlock

def reset():
    global gameOver, gameClose
    global x1, y1
    global x1Change, y1Change
    global snakeLenght
    global snakeSpeed
    global snakeList

    gameOver = False
    gameClose = False
    x1 = DIS_WIDTH/2
    y1 = DIS_HEIGHT/2
    x1Change = y1Change = 0
    snakeLenght = 1
    snakeSpeed = 10
    snakeList = []

#    intro = pygame.mixer.music.load('intro.wav')
 #   pygame.mixer.music.play()
 #   if pygame.mixer.Channel(0).get_busy() ==False:
  #      music = pygame.mixer.music.load('music.wav')
   #     pygame.mixer.music.play(-1)

    foodLocation()

def drawSneak(snakeBlock, sneakelist):
    for x in sneakelist:
            pygame.draw.rect(dis,blue,[x[0],x[1],snakeBlock,snakeBlock])

def score(points):
    value = font_style.render("Score: " + str(points), True, black)
    dis.blit(value,[DIS_WIDTH/2-40,20])

reset()


clock=pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift",25)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[50,DIS_HEIGHT/2])

while not gameClose:
    while gameOver == True:
        dis.fill(black)
        message("You died! Press: Q-Quit or C-Play again",red)
        pygame.display.update()
        pygame.mixer.Sound.play('death.wav')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameClose = True
                    gameOver = False
                if event.key == pygame.K_c:
                    reset()
                break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameClose = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x1Change = -snakeBlock
                y1Change = 0
            if event.key == pygame.K_d:
                x1Change = snakeBlock
                y1Change = 0
            if event.key == pygame.K_w:
                x1Change = 0
                y1Change = -snakeBlock
            if event.key == pygame.K_s:
                x1Change = 0
                y1Change = snakeBlock

    x1 += x1Change #x1 = x1 + x1Change
    y1 += y1Change

    if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
        gameOver = True 


    snakeHead = []
    snakeHead.append(x1)
    snakeHead.append(y1)
    snakeList.append(snakeHead)

    if len(snakeList) > snakeLenght:
        del snakeList[0]
    
    for x in snakeList[:-1]:
        if x == snakeHead:
            gameOver = True

    dis.fill(white)

    drawSneak(snakeBlock,snakeList)
    score(snakeLenght*10)
    pygame.draw.rect(dis,green,[foodX,foodY,snakeBlock,snakeBlock])
    pygame.display.update()

    if x1 == foodX and y1 == foodY:
        foodLocation()
        snakeLenght += 1
        snakeSpeed += 1
        pygame.mixer.Sound.play(eat)


    clock.tick(snakeSpeed)

pygame.quit()
quit()