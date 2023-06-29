import pygame
import time
import  sys, os.path
from random import randint
maxdiff = int(input("Max lvl (standard = 30): "))
pygame.font.init()
x = 1800
y = 1000
fontlist = pygame.font.get_fonts()
screen = pygame.display.set_mode((x, y))
myfont = pygame.font.SysFont('Comic Sans MS', 60)
clicked = False
live = [pygame.image.load("live1.png"), pygame.image.load("live2.png"), pygame.image.load("live3.png")]
list = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","9.png"]
powerup1 = pygame.image.load("powerup.png")
powerup2 = pygame.image.load("watch.png")
good1 = pygame.image.load(list[randint(0,7)])
good2 = pygame.image.load(list[randint(0,7)])
good3 = pygame.image.load(list[randint(0,7)])
good4 = pygame.image.load(list[randint(0,7)])
evil1 = pygame.transform.flip(pygame.image.load(list[randint(0,7)]), True, False)

background_colour = (50, 0, 75)
gx1= randint(0 + 100, x - 100)
gy1= randint(0 + 100, y - 100)
gx2= randint(0 + 100, x - 100)
gy2= randint(0 + 100, y - 100)
gx3= randint(0 + 100, x - 100)
gy3= randint(0 + 100, y - 100)
gx4= randint(0 + 100, x - 100)
gy4= randint(0 + 100, y - 100)
ex1= randint(0 + 100, x - 100)
ey1= randint(0 + 100, y - 100)

px1= randint(-150, -150)
py1= randint(-150, -150)
px2= randint(-150, -150)
py2= randint(-150, -150)

goodh1 = pygame.Rect(gx1, gy1, 100, 100)
goodh2 = pygame.Rect(gx2, gy2, 100, 100)
goodh3 = pygame.Rect(gx3, gy3, 100, 100)
goodh4 = pygame.Rect(gx4, gy4, 100, 100)
evilh1 = pygame.Rect(ex1, ey1, 100, 100)
poweruph1 = pygame.Rect(px1, py1, 100, 100)
poweruph2 = pygame.Rect(px2, py2, 100, 100)
score = 0
health = 2
timer = 10
start_time = time.time()
timertxt = myfont.render(str(timer), False, (255, 0, 255))


def chill_over(rect1, rect2):
    collide = rect1.colliderect(rect2)
    return True if collide else False   
def is_over(rect, pos):
  return True if rect.collidepoint(pos[0], pos[1]) else False
running = True

while running:   
#for loop through the event queue  
    for event in pygame.event.get():
      
        #Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
    m = pygame.mouse.get_pos()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if clicked == False:
        if is_over(goodh1, m):
            clicked = True
            health = health - 1
            background_colour = (randint(0,255), randint(0,255), randint(0,255))
    if event.type == pygame.MOUSEBUTTONDOWN:
      if clicked == False:
        if is_over(goodh2, m):
            clicked = True
            health = health - 1
            background_colour = (randint(0,255), randint(0,255), randint(0,255))
    if event.type == pygame.MOUSEBUTTONDOWN:
      if clicked == False:
        if is_over(goodh3, m):
            clicked = True
            health = health - 1
            background_colour = (randint(0,255), randint(0,255), randint(0,255))
    if event.type == pygame.MOUSEBUTTONDOWN:
      if clicked == False:
        if is_over(goodh4, m):
            clicked = True
            health = health - 1
            background_colour = (randint(0,255), randint(0,255), randint(0,255))

    if event.type == pygame.MOUSEBUTTONDOWN:
      if clicked == False:
        if is_over(evilh1, m):
            clicked = True
            timer += 1.5
            score += 1
            background_colour = (200, 200, 100)

            good1 = pygame.image.load(list[randint(0,7)])
            good2 = pygame.image.load(list[randint(0,7)])
            good3 = pygame.image.load(list[randint(0,7)])
            good4 = pygame.image.load(list[randint(0,7)])
            evil1 = pygame.transform.flip(pygame.image.load(list[randint(0,7)]), True, False)


            gx1= randint(0 + 100, x - 100)
            gy1= randint(0 + 100, y - 100)
            gx2= randint(0 + 100, x - 100)
            gy2= randint(0 + 100, y - 100)
            gx3= randint(0 + 100, x - 100)
            gy3= randint(0 + 100, y - 100)
            gx4= randint(0 + 100, x - 100)
            gy4= randint(0 + 100, y - 100)
            ex1= randint(0 + 100, x - 100)
            ey1= randint(0 + 100, y - 100)

            if randint(1,25) == 1:
                px1= randint(0 + 100, x - 100)
                py1= randint(0 + 100, y - 100)
                poweruph1 = pygame.Rect(px1, py1, 100, 100)

            if randint(1, 20) == 1:
                px2= randint(0 + 100, x - 100)
                py2= randint(0 + 100, y - 100)
                poweruph2 = pygame.Rect(px2, py2, 100, 100)

            goodh1 = pygame.Rect(gx1, gy1, 100, 100)
            goodh2 = pygame.Rect(gx2, gy2, 100, 100)
            goodh3 = pygame.Rect(gx3, gy3, 100, 100)
            goodh4 = pygame.Rect(gx4, gy4, 100, 100)
            evilh1 = pygame.Rect(ex1, ey1, 100, 100)
            
            if chill_over(evilh1, goodh1) or is_over(evilh1, goodh2) or is_over(evilh1, goodh3) or is_over(evilh1, goodh4):
                while chill_over(evilh1, goodh1) or is_over(evilh1, goodh2) or is_over(evilh1, goodh3) or is_over(evilh1, goodh4):
                    gx1= randint(0 + 100, x - 100)
                    gy1= randint(0 + 100, y - 100)
                    gx2= randint(0 + 100, x - 100)
                    gy2= randint(0 + 100, y - 100)
                    gx3= randint(0 + 100, x - 100)
                    gy3= randint(0 + 100, y - 100)
                    gx4= randint(0 + 100, x - 100)
                    gy4= randint(0 + 100, y - 100)
                    ey1= randint(0 + 100, y - 100)
                    goodh1 = pygame.Rect(gx1, gy1, 100, 100)
                    goodh2 = pygame.Rect(gx2, gy2, 100, 100)
                    goodh3 = pygame.Rect(gx3, gy3, 100, 100)
                    goodh4 = pygame.Rect(gx4, gy4, 100, 100)
                    evilh1 = pygame.Rect(ex1, ey1, 100, 100)

    if event.type == pygame.MOUSEBUTTONDOWN:
      if clicked == False:
        if is_over(poweruph1, m):
            clicked = True
            if health < 2:
                health += 1
            background_colour = (255, 255, 200)
            px1 = -150
            py1 = -150

    if event.type == pygame.MOUSEBUTTONDOWN:
      if clicked == False:
        if is_over(poweruph2, m):
            clicked = True
            timer += 15
            background_colour = (255, 100, 200)
            px2 = -150
            py2 = -150

    if event.type == pygame.MOUSEBUTTONDOWN:
       clicked = True
    else:
       clicked = False



    screen.fill(background_colour)
    screen.blit(live[health], (10, 0))
    screen.blit(timertxt, (1700, 0))
    screen.blit(good1, (gx1, gy1))
    screen.blit(good2, (gx2, gy2))
    screen.blit(good3, (gx3, gy3))
    screen.blit(good4, (gx4, gy4))
    screen.blit(evil1, (ex1, ey1))
    screen.blit(powerup1, (px1, py1))
    screen.blit(powerup2, (px2, py2))
    
    


    if score <= maxdiff:
        timer = timer - ((time.time() - start_time) * (score / 20))
    else:
       timer = timer - ((time.time() - start_time) * (maxdiff / 20))
    start_time = time.time()
    timertxt = myfont.render(str(round(timer)), False, (255, 0, 255))

    pygame.display.flip()
    if timer <= 0:
       print("Died of time", "\n" + "score:" + str(score))
       running = False
    if health <= -1:
       print("Died of health", "\n" +  "score:" + str(score))
       running = False

