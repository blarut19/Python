import pygame
import math
pygame.init()

resX = 800
resY = 600

win = pygame.display.set_mode((resX, resY))
pygame.display.set_caption("Phi")

x = 400.0
y = 300.0
t = 0
f = 0.0
m = 0
o = 0
dx = 250
dy = 300
calc = 1
font = pygame.font.SysFont('arial', 30)
sunflower = pygame.image.load('sunflower.png')

class seed:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        

def collision(s1, s2):
    if math.sqrt((s1.x-s2.x)**2 + (s1.y-s2.y)**2) < (s1.size + s2.size)*1.5:
        return 1
    return 0

def mass_collision(f, s):
    i = len(f)-2
    while i > len(f)/3:
        if collision(f[i], s):
            return 1
        i -= 1
    return 0

def draw_seed(s):
    pygame.draw.circle(win, (204, 232, 42), (int(s.x), int(s.y)), s.size)

def show_sunflower():
    win.blit(sunflower, (440, 130))

def calc_flower():
    flower = [seed(dx, dy, 1)]
    
    x = dx
    y = dy
    
    i = 1

    while (x-dx)*(x-dx)+(y-dy)*(y-dy)<18000:
        x += math.cos(math.radians(t*360)*i)*i
        y += math.sin(math.radians(t*360)*i)*i
        s = seed(x, y, 2)
        flower.append(s)
        i += 1
    return flower

def draw_flower(f):
    i = 0
    while i < len(f):
        draw_seed(f[i])
        i += 1

#starting here
run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
#simulation started
#drawing
    win.fill((0,65,30))
    pygame.draw.circle(win, (155,40,0) ,(dx, dy), 150)
    pygame.draw.circle(win, (50,55,30) ,(dx, dy), 148)
    if calc:
        flower = calc_flower()
        calc = 0

    keys = pygame.key.get_pressed()

    x = 400.0
    y = 300.0

    #check user input
    if keys[pygame.K_ESCAPE]:
        run = False
    if not keys[pygame.K_SPACE]:
        t += f
    if keys[pygame.K_UP]:
        f += 0.00001
        calc = 1
    if keys[pygame.K_DOWN]:
        f -= 0.00001
        calc = 1
    if keys[pygame.K_r]:
        t += 0.0001
        calc = 1
    if keys[pygame.K_f]:
        t -= 0.0001
        calc = 1
    if keys[pygame.K_e]:
        t += 0.001
        calc = 1
    if keys[pygame.K_d]:
        t -= 0.001
        calc = 1
    if keys[pygame.K_w]:
        t += 0.01
        calc = 1
    if keys[pygame.K_s]:
        t -= 0.01
        calc = 1
    if keys[pygame.K_z]:
        f = 0.0
        calc = 1
    if keys[pygame.K_p]:
        t = 1.618033989
        calc = 1
    if keys[pygame.K_o]:
        o = not o
        pygame.time.delay(100)
    if f != 0:
        calc = 1

    if keys[pygame.K_m]:
        nt = '0.'
        m = 1
    if m:
        if keys[pygame.K_0]:
            nt += '0'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_1]:
            nt += '1'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_2]:
            nt += '2'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_3]:
            nt += '3'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_4]:
            nt += '4'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_5]:
            nt += '5'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_6]:
            nt += '6'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_7]:
            nt += '7'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_8]:
            nt += '8'
            pygame.time.delay(100)
            print(nt)
        if keys[pygame.K_9]:
            nt += '9'
            pygame.time.delay(100)
            print(nt)
            
        if keys[pygame.K_n]:
            t = float(nt)
            nt = '0.'
            pygame.time.delay(100)
            calc = 1

    if o:
        show_sunflower()

            
    textt = font.render('t = ' + str(t)[0:6], 1, (255,255,255))
    win.blit(textt, (50, 50))
        
    draw_flower(flower)

    pygame.display.update()
pygame.quit()
