import pygame
import math
pygame.init()

win = pygame.display.set_mode((1024,640))
pygame.display.set_caption("Luk")

x = 920
y = 430
width = 30
length = 40
count = 0

MAX_VELOCITY = 5
MAX_REVERSE_VELOCITY = -3
ROTATION_SPEED = 0.7
BRAKES_CLASS = 1.2
DRAG = 0.995

Fail = pygame.image.load('Fail.png')

rotation = 180.0
velocity = 0
collision = False

def distance(x, y, Ox, Oy):
    return math.sqrt((Ox-x)*(Ox-x)+(Oy-y)*(Oy-y))

run = True

while run:
    
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #check for what keys are being pressed
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and velocity < MAX_VELOCITY:
        velocity += 0.7
    if keys[pygame.K_SPACE]:
        velocity *= 1/BRAKES_CLASS
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and velocity <= 1 and velocity > MAX_REVERSE_VELOCITY:
        velocity -= 0.5
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        rotation -= ROTATION_SPEED*velocity
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        rotation += ROTATION_SPEED*velocity

    #change velocity
    x += velocity * math.cos(math.radians(rotation))
    y += velocity * math.sin(math.radians(rotation))
    velocity = velocity*DRAG

    collision = False
    
    class wheel:
        lf=[x+length*math.cos(math.radians(rotation))+0.5*width*math.sin(math.radians(rotation)), y+length*math.sin(math.radians(rotation))-0.5*width*math.cos(math.radians(rotation))]
        rf=[x+length*math.cos(math.radians(rotation))-0.5*width*math.sin(math.radians(rotation)), y+length*math.sin(math.radians(rotation))+0.5*width*math.cos(math.radians(rotation))]
        lr=[x+0.5*width*math.sin(math.radians(rotation)), y-0.5*width*math.cos(math.radians(rotation))]
        rr=[x-0.5*width*math.sin(math.radians(rotation)), y+0.5*width*math.cos(math.radians(rotation))]

    #check if any wheel is outside the arc
    if 350>wheel.lf[0]>290 and 350>wheel.lr[0]>290 and 350>wheel.rf[0]>290 and 350>wheel.rr[0]>290:
        collision = False
    if wheel.lf[1] > 460 or wheel.lf[1] < 400 or wheel.lr[1] > 460 or wheel.lr[1] < 400 or wheel.rf[1] > 460 or wheel.rf[1] < 400 or wheel.rr[1] > 460 or wheel.rr[1] < 400:
        collision = True
    if distance(wheel.lf[0], wheel.lf[1], 400, 350)<110 and distance(wheel.lr[0], wheel.lr[1], 400, 350)<110 and distance(wheel.rf[0], wheel.rf[1], 400, 350)<110 and distance(wheel.rr[0], wheel.rr[1], 400, 350)<110:
        collision = False
    if distance(wheel.lf[0], wheel.lf[1], 460, 290)<110 or distance(wheel.lr[0], wheel.lr[1], 460, 290)<110 or distance(wheel.rf[0], wheel.rf[1], 460, 290)<110 or distance(wheel.rr[0], wheel.rr[1], 460, 290)<110:
        collision = True
    if wheel.lf[1]<160 or wheel.lr[1]<160 or wheel.rf[1]<160 or wheel.rr[1]<160 or wheel.lf[0]>1000 or wheel.lr[0]>1000 or wheel.rf[0]>1000 or wheel.rr[0]>1000:
        collision = True
    if 350>wheel.lf[0]>290 and 350>wheel.lr[0]>290 and 350>wheel.rf[0]>290 and 350>wheel.rr[0]>290 and 360>wheel.lf[1]>160 and 360>wheel.lr[1]>160 and 360>wheel.rf[1]>160 and 360>wheel.rr[1]>160:
        collision = False

    #draw the scene
    win.fill((33,33,33))
    pygame.draw.rect(win, (140,140,140), (400, 400, 600, 60))
    pygame.draw.circle(win, (140,140,140), (400, 350), 110)
    pygame.draw.circle(win, (33,33,33), (460, 290), 110)
    pygame.draw.rect(win, (33,33,33), (350, 200, 50, 100))
    pygame.draw.rect(win, (33,33,33), (460, 350, 100, 50))
    pygame.draw.rect(win, (140,140,140), (290, 160, 60, 200))

    #draw the car
    pygame.draw.rect(win, (0,150,105), (x, y, 5, 5))
    pygame.draw.rect(win, (0,150,105), (x+length*math.cos(math.radians(rotation)), y+length*math.sin(math.radians(rotation)), 5, 5))
    pygame.draw.rect(win, (255,0,0), (wheel.lr[0], wheel.lr[1], 5, 5))
    pygame.draw.rect(win, (255,0,0), (wheel.rr[0], wheel.rr[1], 5, 5))
    pygame.draw.rect(win, (255,0,0), (wheel.lf[0], wheel.lf[1], 5, 5))
    pygame.draw.rect(win, (255,0,0), (wheel.rf[0], wheel.rf[1], 5, 5))
    
    if (collision):
        win.blit(Fail, (120, 50))
        count += 1

    #reset if car is outside the arc for too long
    if count>40:
        x = 920
        y = 430
        rotation = 180.0
        velocity = 0
        collision = False
        count = 0
      
    pygame.display.update()     
    
pygame.quit()
