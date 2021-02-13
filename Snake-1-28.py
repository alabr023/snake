import pygame
import random
import time as t
 
pygame.init()


 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (100, 0, 255)
cyan = (0, 255, 255)



dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("sanserif", 35)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def message(msg, color, offset):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3 + offset])

def mainMenu(start):

    while not start:
        dis.fill(black)
        message("Welcome to Andy's Snake game!", cyan, 0)
        message("Press \"P\" to play", cyan, 50)
        message("Press \"Q\" to exit", cyan, 100)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return False
                if event.key == pygame.K_q:
                    return True

def chooseMode(chosen):

    while chosen == False: 
            dis.fill(black)
            message(" Press \"d\" for dark mode, \"l\" for light mode", white,0)
            
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        return [black, white, green, t.time()]
                    if event.key == pygame.K_l:
                        return [white, black, blue, t.time()]
    
def gameLoop():
    game_over = False
    game_close = False

    chosen = False   

    menu = False 
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    count = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    
    while not game_over:
 
        while game_close == True:
            dis.fill(game_color)
            message("You Lost! Press C-Play Again or Q-Quit", food_color,0)
 
            pygame.display.update()
 
            for event in pygame.event.get():
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
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        
        if menu == False:

            game_over = mainMenu(menu)

            menu = True

        if not chosen and not game_over:
            arr = chooseMode(chosen)

            game_color = arr[0]
            snake_color = arr[1]
            food_color = arr[2]
            temp = arr[3]

            chosen = True
        
        dis.fill(game_color)

        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List, snake_color)
 
        score = font_style.render("Score: " + str(Length_of_snake), True, food_color)
        dis.blit(score, [dis_width / 15, dis_height / 15])


        score = font_style.render("Time: " + str(int(t.time()) - int(temp)), True, food_color)
        dis.blit(score, [dis_width / 15, dis_height / 8])
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            count += 1
 
        clock.tick(snake_speed + count)
 
    pygame.quit()
    quit()
gameLoop()