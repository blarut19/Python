import pygame
import math
import random
pygame.init()

win = pygame.display.set_mode((1280, 320))
pygame.display.set_caption("plane")

resX = 1280
resY = 320

color1 = (255,127,80)		# orange
color2 = (255,200,120)		# yellow
background_color = (0,96,100)	# teal

offsetx = 150
offsety = 120
widthx = 8
widthy = 8

file = open("input.txt")
data = file.read()
data = data.split("\n")
    
def decode(d):
    A = []
    for i in range(0, 128):
        A.append(i)
    for i in range(0, 7):
        if d[i] == "F":
            A = split(A)[0]
        else:
            A = split(A)[1]
    col = A[0]
    A = []
    for i in range(0, 8):
        A.append(i)
    for i in range(7, 10):
        if d[i] == "R":
            A = split(A)[1]
        else:
            A = split(A)[0]
    row = A[0]
    
    return col, row


def split(A):
    B = A[:len(A)//2]
    C = A[len(A)//2:]
    return B, C

def draw_seat(s):
    pygame.draw.rect(win, color1, (s[0]*widthx+offsetx, s[1]*widthy+offsety, widthx, widthy))

seats = []

col = -5
row = -5

#starting here
run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#started
    win.fill(background_color)
    
    keys = pygame.key.get_pressed()
    
    if data:
        seats.append(decode(data.pop(0)))
    if data:
        seats.append(decode(data.pop(0)))
    
    for i in range(0, len(seats)):
        draw_seat(seats[i])
        
    if keys[pygame.K_DOWN]:
        col = col + 1
        print("column:", col, "row:", row)
    if keys[pygame.K_UP]:
        col = col - 1
        print("column:", col, "row:", row)
    if keys[pygame.K_RIGHT]:
        row = row + 1
        print("column:", col, "row:", row)
    if keys[pygame.K_LEFT]:
        row = row - 1
        print("column:", col, "row:", row)
        
    pygame.draw.rect(win, color2, (row*widthx+offsetx, col*widthy+offsety, widthx, widthy))

    pygame.display.update()
pygame.quit()
