import pygame
import math
import random

from ball_helper import blob, lookAheadCheckCollision, resolvePhysicalCollision

from pygame_helper import initialize, bound

# Environment
screen = pygame.display.set_mode([500,500])
boundaries = bound(30,470)
red_border = [boundaries.x,boundaries.y-boundaries.x]
gravity = 981 #0  or 981

# ball stuff:

# big
# rows = 5
# radius = 10
#small
rows = 5
radius = 3
wall_dampen = 0.85
particle_dampen = 0.97
gap = 10
random_v = 1 # set to 1 for random velocities
allParticles = []
totalCollisions = 0

clock = pygame.time.Clock()

pygame.init()

initialize(allParticles,screen,red_border,boundaries,radius,gap,rows,random_v)

clock.tick(500)

i = 0

running = True

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
                totalCollisions += 1
                resolvePhysicalCollision(particles, otherPart, gravity, particle_dampen)

        particles.resolveWallCollision(wall_dampen, boundaries, radius)
        # print("Location:",particles.location,"| Velocity:",particles.velocity)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Ending simulation. Total collisions =", totalCollisions)
                running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(red_border[0],red_border[0],red_border[1],red_border[1]),  2)
    
    for particle in allParticles:
        particle.drawBall(screen, radius)

    # Flip the display
    pygame.display.flip()

pygame.quit()