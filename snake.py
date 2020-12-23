import pygame
import time
import random
import threading

pygame.init()

# color definition
white = (255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,102)

# Definition of game boundaries
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.update()
pygame.display.set_caption("Snake Tutorial")

# Game variable definition

clock = pygame.time.Clock()
snake_block = 10
snake_speed=15

font_style = pygame.font.SysFont("bahnschrift",25)
score_font = pygame.font.SysFont(None, 35)

def score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def snake_logic(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
# message display function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop(): # Function declaration
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0
    # Prevent the player from killing themselves after reaching length > 3
    left_disable = False
    right_disable = False
    down_disable = False
    up_disable = False

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # scope is wrong with function, research
    def key_disable(key_input):
        if key_input == "RIGHT":
            left_disable = True
            up_disable = False
            down_disable = False
            print("left", left_disable)
        elif key_input == "LEFT":
            right_disable = True
            up_disable = False
            down_disable = False
            print("left", left_disable)
        elif key_input == "DOWN":
            left_disable = False
            right_disable = False
            up_disable = True
        elif key_input == "UP":
            left_disable = False
            right_disable = False
            down_disable = True

    while not game_over:

        while game_close == True:
            message("You Lost! Press Q to Quit or C to Play Again", blue)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not left_disable == True:
                    x1_change = -snake_block
                    y1_change = 0
                    key_disable("LEFT")
                elif event.key == pygame.K_RIGHT and right_disable != True:
                    x1_change = snake_block
                    y1_change = 0
                    key_disable("RIGHT")
                elif event.key == pygame.K_UP and up_disable != True:
                    y1_change = -snake_block
                    x1_change = 0
                    key_disable("UP")
                elif event.key == pygame.K_DOWN and down_disable != True:
                    y1_change = snake_block
                    x1_change = 0
                    key_disable("DOWN")

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
            
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        snake_logic(snake_block, snake_List)
        score(length_of_snake - 1)

        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()