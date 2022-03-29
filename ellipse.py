import pygame
import math
pygame.init()

win = pygame.display.set_mode((1280 , 960))
pygame.display.set_caption("Ellipse")

font1 = pygame.font.SysFont('arial', 30)

X_RES = 1280
Y_RES = 960

CIRCLE_CENTER = (X_RES/2, Y_RES/2)
CIRCLE_RADIUS = 300

POINTS_NUMBER = 90

COLOR_1 = (255,165,0)
COLOR_2 = (0,128,128)

points = []

for a in range (0, POINTS_NUMBER):
    points.append((CIRCLE_CENTER[0]-CIRCLE_RADIUS*math.sin((360/POINTS_NUMBER)*a/180*math.pi),CIRCLE_CENTER[1]-CIRCLE_RADIUS*math.cos((360/POINTS_NUMBER)*a/180*math.pi)))

def line_by_2_points(x1, y1, x2, y2):
    if x1 == x2:
        return(0, 0)
    a = (y1-y2)/(x1-x2)
    b=y1-a*x1
    return (a, b)

def line_by_point_and_known_a(a, x, y):
    return (a, y-a*x)

#starting here
run = True

while run:
    pygame.time.delay(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#simulation started

#drawing
    win.fill((0,96,100))

    pygame.draw.circle(win, COLOR_2, CIRCLE_CENTER, CIRCLE_RADIUS)
    pygame.draw.circle(win, COLOR_1, CIRCLE_CENTER, 1)

    mouse = pygame.mouse.get_pos()

    for a in range (0, POINTS_NUMBER):
        (a_line, b_line) = line_by_2_points(points[a][0], points[a][1], mouse[0], mouse[1])
        if a_line != 0:
            (a_line, b_line) = line_by_point_and_known_a(-1/a_line, (mouse[0]+points[a][0])/2,(mouse[1]+points[a][1])/2)
            pygame.draw.line(win, COLOR_1, (0, b_line), (X_RES, a_line*X_RES+b_line))
    
    pygame.display.update()
pygame.quit()
