import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Sanke Run')

pygame.display.update()


clock = pygame.time.Clock()

block = 10
FPS = 15

font = pygame.font.SysFont(None, 25)

def snake(block, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1], block,block])

def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [display_width/3, display_height/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block)/10.0)*10.0
    # print((randAppleX, randAppleY))

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("You loose, Press 'C' to play again or Press 'Q' to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = -block
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = block
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        appleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,appleThickness,appleThickness])
        # pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block,block])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del(snakeList[0])
        
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True


        snake(block, snakeList)
        pygame.display.update()

        if lead_x >= randAppleX and lead_x <= randAppleX + appleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + appleThickness:
                randAppleX = round(random.randrange(0, display_width-block)/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block)/10.0)*10.0
                snakeLength += 1
        clock.tick(FPS)

    pygame.quit()

    quit()

gameLoop()
