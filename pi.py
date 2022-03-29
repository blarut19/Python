import pygame
import math
pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("pi")

resX = 1280
resY = 720
width = 40
x = 50
count = 0
wallx = 120
floorY = 550
BG = (0,96,100)
obj = color1 = (255,127,80)
WALL = obj
gscale = 15
font = pygame.font.SysFont('arial', 40)

#place for functions and classes

class body:
    def __init__(self, x, vel, mass):
        self.x = x
        self.vel = vel
        self.mass = mass

a = body(450.0, 0.0, 1)
b = body(550.0, -0.05, 10000)

def collision_check():
    if a.x+width > b.x :
        return 1
    return 0

def draw():
    pygame.draw.rect(win, obj, (int(a.x), floorY, width, width))
    pygame.draw.rect(win, obj, (int(b.x), floorY-x, width+x, width+x))
    pygame.draw.rect(win, WALL, (wallx, floorY+width, resX+30, 3))
    pygame.draw.rect(win, WALL, (wallx-3, 0, 3, floorY+width+3))
    texta = font.render("V1 = " + str(a.vel)[0:10], 1, obj)
    win.blit(texta, (800, 150))
    textb = font.render("V2 = " + str(b.vel)[0:10], 1, obj)
    win.blit(textb, (800, 200))

def move():
    a.x += a.vel
    b.x += b.vel
    if a.x < wallx:
        a.x = wallx
        a.vel *= -1
        return 1
    if collision_check():
        v1 = a.vel
        v2 = b.vel
        a.vel = (v1*(a.mass-b.mass)+2*b.mass*v2)/(a.mass+b.mass)
        b.vel = (v2*(b.mass-a.mass)+2*a.mass*v1)/(a.mass+b.mass)
        if b.x < wallx + width:
            b.x = wallx + width
            a.x = wallx
        return 1
    return 0

def graph():
    axisX = resX/2 - 350
    axisXl = 400
    axisY = 20
    axisYl = 400
    width = 1
    pygame.draw.line(win, obj, (int(axisX), int(axisYl*0.5+axisY)), (int(axisX+axisXl), int(axisYl*0.5+axisY)), width)
    pygame.draw.line(win, obj, (int(axisX+axisXl*0.5), int(axisY)), (int(axisX+axisXl*0.5), int(axisY+axisYl)), width)
    gX = int(axisX+axisXl*0.5)
    gY = int(axisY+axisYl*0.5)
    pygame.draw.circle(win, obj, (int(gX+b.vel*math.sqrt(b.mass/a.mass)*gscale), int(gY-a.vel*gscale)), 1, 0)
 

#starting here
run = True
win.fill(BG)
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#game started
    #win.fill(BG)
    pygame.draw.rect(win, BG, (0, 500-x, resX, resY))
    pygame.draw.rect(win, BG, (800, 0, resX, resY))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    pva = a.vel
    pvb = b.vel
    count += move()
    draw()
    #graph()

    textt = font.render(str(count), 1, obj)
    win.blit(textt, (800, 100))


    pygame.display.update()
pygame.quit()
