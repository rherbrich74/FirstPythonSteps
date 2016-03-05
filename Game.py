import pygame
import sys
from random import randrange


# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

def initialize():
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.init()
    return screen

def drawGameScreen(screen):
    screen.fill(BLACK)
    y_offset = 0
    x_offset = 0
    done = True
    # while not done:
#         for i in range(50):
#             x = randrange(0, 500)
#             y = randrange(0, 500)
#             pygame.draw.rect(screen, WHITE, [x, y, 5, 5])
    # while y_offset < 360:
    #     # Background
    #     pygame.draw.line(screen, (135,103, 230), [0 + x_offset, 0], [0 + x_offset, 500],5)
    #     pygame.draw.line(screen, (191, 255, 0), [0 + x_offset + 10, 0], [0 + x_offset + 10, 500],5)
    #     y_offset += 10
    #     x_offset += 20

def game():
    screen = initialize()
    y_offset_ob = 50
    x_offset_ob = 50
    y_speed = 5
    x_speed = 5
    done = False
    is_blue = True
    clock = pygame.time.Clock()
    pygame.display.set_caption("Spiel")
    colorlist = ['999','999']
    m = len(colorlist)     
    s = 1
    # =================
    # = Main Programm =
    # =================

    while not done:
        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("The game was quit")
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print ("Color changed")
                is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y_offset_ob -= y_speed
            #print ("Up Key was pressed")
        if pressed[pygame.K_DOWN]:
            y_offset_ob += y_speed
            #print ("Down Key was pressed")
        if pressed[pygame.K_LEFT]:
            x_offset_ob -= x_speed
            #print ("Left Key was pressed")
        if pressed[pygame.K_RIGHT]:
            x_offset_ob += x_speed
            #print ("Rigth Key was pressed")
        if (y_offset_ob > 450) or (y_offset_ob < 0):
            y_speed = y_speed * -1
            #print("Wechsel")
        if (x_offset_ob > 650) or (x_offset_ob < 0):
            x_speed = x_speed * -1
            #print("Wechsel")
        
        drawGameScreen(screen)
        
        if is_blue:
            color = (207, 27, 30)
            s += 1
            red = randrange(0, 255)
            green = randrange(0, 255)
            blue = randrange(0, 255)         
            color2 = (red, green, blue)
            colorlist.append(color2)
            # print (colorlist[s])
#             print (len(colorlist))
#             print (s)
        else:
            color = colorlist[s]
            print ("The Color: ", colorlist[s])
    
        pygame.draw.rect(screen, WHITE, [x_offset_ob, y_offset_ob, 70, 70])
        pygame.draw.rect(screen, color, [x_offset_ob + 10, y_offset_ob + 10, 50, 50])
        pygame.display.flip()
        clock.tick(60)

game()