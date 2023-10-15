import pygame
import math
import random

from ball_helper import blob, lookAheadCheckCollision, resolvePhysicalCollision

from pygame_helper import initialize, bound

# Set up the drawing window
screen = pygame.display.set_mode([500,500])

# ball stuff:
radius = 5
dampen = 0.85

# border stuff:
boundaries = bound(30,470)
red_border = [boundaries.x,boundaries.y-boundaries.x]

running = True

# gap between particles
gap = 10
allParticles = []

gravity = 9.81*100 # 9.81m/s2

clock = pygame.time.Clock()

pygame.init()

initialize(allParticles,screen,red_border,boundaries,radius,gap)

clock.tick(500)

i = 0

while running:
    i += 1
    clock.tick(200)

    time_Elapsed = clock.get_time() / 1000 # in seconds
    print("Iteration",i,":",time_Elapsed,"s")
    # Calling all the physics portions
    
    for particles in allParticles:
        particles.locUpdate(time_Elapsed, gravity)
        particles.gravityUpdate(gravity, time_Elapsed)

        for otherPart in allParticles[ allParticles.index(particles) + 1 :]:

            # if checkCollision(particles, otherPart, radius):
            #     resolvePhysicalCollision(particles, otherPart)

            if lookAheadCheckCollision(particles, otherPart, radius, time_Elapsed, gravity):
                resolvePhysicalCollision(particles, otherPart)

        particles.resolveWallCollision(dampen, boundaries, radius)
        # print("Location:",particles.location,"| Velocity:",particles.velocity)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(red_border[0],red_border[0],red_border[1],red_border[1]),  2)
    
    for particle in allParticles:
        particle.drawBall(screen, radius)

    # Flip the display
    pygame.display.flip()

pygame.quit()