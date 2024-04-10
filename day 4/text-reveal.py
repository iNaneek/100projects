import pygame
import time
import random

pygame.font.init() #initializes fonts
pygame.init()

win = pygame.display.set_mode((800, 800)) #window size
pygame.display.set_caption("pygame") #window title
testFont = pygame.font.Font(None, 50) #defines font type
#font = pygame.font.SysFont("Consolas", 50, bold=False, italic=False)
font = pygame.font.SysFont("Courier", 20, bold=True, italic=False)

t1 = time.time()
t2 = time.time()
strings = []


mousePos = (0, 0)
running = True
while running:
    pygame.time.delay(20) #time between frames (in ms)

    for event in pygame.event.get(): #when close button pushed, loop ends
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() #all pressed keys

    win.fill((35, 35, 35)) #fills screen background




    print(t2-t1)
    t1 = t2
    t2 = time.time()



    #This makes the rectangles on screen

    #pygame.draw.rect(win, (255, 255, 255), ((15, 10), (75, 50)))
    #rect(window, color in rgb, ((xpos top left, ypostopleft), (x-width, y-height)))
    if mousePos != pygame.mouse.get_pos():
        strings = []

        for i in range(20):
            x = ''
            for j in range(66):
                x += random.choice(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                                    'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'))
            strings.append(x)

    for index, i in enumerate(strings):
        win.blit(font.render(i, True, 'White'), (3, 30 * index))

    mousePos = pygame.mouse.get_pos()

    #pygame.draw.circle(win, (0, 0, 0), mousePos, 10)

    s = pygame.Surface()  # the size of your rect
    s.set_alpha(128)  # alpha level
    s.fill((255, 255, 255))  # this fills the entire surface
    win.blit(s, mousePos)



    if keys[pygame.K_SPACE]:
        pass #key input for space bar. K_a, K_b, K_c etc






    pygame.display.update()
pygame.quit() #when the loop ends it closes the window
