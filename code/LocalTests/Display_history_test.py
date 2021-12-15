import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import time
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
out = ['0' , '1']
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255,0,0)
purple = (128,0,128)
black = (0,0,0)
# assigning values to X and Y variable
X = 1000
Y = 1000

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
# pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 128)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render(out[0], True, purple, black)
mem = font.render(out[0], True, purple, black)
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)
 
textBuf = mem.get_rect()
textBuf.center = (64 , Y - 64)
buf = ""
# infinite loop
while True:
    # completely fill the surface object
    # with white color
    # display_surface.fill(black)
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    # print("Hi")
    display_surface.fill((0,0,0))
    # display_surface.blit(text, textRect)
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    event = pygame.event.Event(pygame.KEYUP, key=pygame.K_r)
    pygame.event.post(event)
    time.sleep(0.5)
    msg = out[random.randint(0,10)%2]
    text = font.render(msg, True, purple, black)
    display_surface.blit(text, textRect)
    buf += msg
    if len(buf) > 5:
        buf = buf[1:]
    text = font.render(buf, True, purple, black)
    display_surface.blit(text, textBuf)

    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()
            # quit the program.
            quit()
        # Draws the surface object to the screen.
        pygame.display.update()