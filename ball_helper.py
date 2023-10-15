import pygame
import math

totalCollisions = 0

class blob:
    def __init__(self, location, velocity, name):
        self.location = location
        self.velocity = velocity
        self.name = name
    
    def locUpdate(self, time, gravity):
        self.location[0] += self.velocity[0] * time 
        self.location[1] += self.velocity[1] * time + 0.5 * gravity * time**2

    def forwardLocUpdate(self, time, gravity):
        return (self.location[0] + self.velocity[0] * time, self.location[1] + self.velocity[1] * time + 0.5 * gravity * time**2)

    def gravityUpdate(self,gravity,time):
        self.velocity[1] += gravity * time

    def resolveWallCollision(self, dampen, boundaries, radius):
        if self.location[0] > boundaries.y - radius:
            self.velocity[0] = -1 * abs(self.velocity[0]) * dampen
            self.location[0] = boundaries.y - radius
        if self.location[0] < boundaries.x + radius:
            self.velocity[0] = abs(self.velocity[0]) * dampen
            self.location[0] = boundaries.x + radius
        if self.location[1] > boundaries.y - radius:
            self.velocity[1] = -1 * abs(self.velocity[1]) * dampen
            self.location[1] = boundaries.y - radius
        if self.location[1] < boundaries.x  + radius:
            self.velocity[1] = abs(self.velocity[1]) * dampen
            self.location[1] = boundaries.x + radius

    def drawBall(self, screen, radius):
        pygame.draw.circle(screen, (0, 0, 255), (self.location[0], self.location[1]), radius)

def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def checkCollision(blob1, blob2, radius):
    if pythagoras(blob1.location[0],blob2.location[0],blob1.location[1],blob2.location[1]) < radius * 2:
        # print(blob1.name,"and",blob2.name,'collided')
        return True
    else:
        pass

def lookAheadCheckCollision(blob1, blob2, radius, time_Elapsed, gravity):
    a, b = blob1.forwardLocUpdate(time_Elapsed, gravity)
    x, y = blob2.forwardLocUpdate(time_Elapsed, gravity)
    if pythagoras(a,b,x,y) < radius * 2:
        # print(blob1.name,"and",blob2.name,'collided')
        return True
    else:
        pass

def resolvePhysicalCollision(blob1,blob2, gravity ,dampen):
    a, b = blob1.forwardLocUpdate(0.001, gravity)
    x, y = blob2.forwardLocUpdate(0.001, gravity)
    if pythagoras(a,b,x,y) < pythagoras(blob1.location[0],blob1.location[1],blob2.location[0],blob2.location[1]):
        for i in [0,1]:
            blob1.velocity[i] , blob2.velocity[i] = dampen*blob2.velocity[i] , dampen*blob1.velocity[i]