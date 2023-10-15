import pygame
import random

from ball_helper import blob

class bound:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def setParticles(allParticles,boundaries,radius,gap,rows,random_v):
    for j in range(0,rows):
        for i in range(1, 1 + int((boundaries.y - boundaries.x) / ( 2 * radius + gap ))):
            allParticles.append(blob([ boundaries.x + radius + gap + (i-1) * (2 * radius + gap) ,250 - j * (2 * radius + gap)],[ (1-random_v)*200 + random_v*random.randint(0,200)*random.randrange(-1,2,2),(1-random_v)*-200 + random_v*random.randint(0,400)*random.randrange(-1,2,2)],"Blob{}".format(i)))

    for i in allParticles:
        print(i.location)

def initialize(allParticles, screen, red_border, boundaries, radius, gap, rows, random_v):
    
    setParticles(allParticles,boundaries,radius,gap,rows,random_v)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255,0,0), pygame.Rect(red_border[0],red_border[0],red_border[1],red_border[1]),  2)
    
    for particles in allParticles:
        particles.drawBall(screen, radius)

    pygame.display.flip()

    print("Similutaion initialized.")

    pygame.time.wait(1000)

    print("Simulation start.")