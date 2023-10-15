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

def checkCollision(blob1, blob2, radius):
    if math.sqrt((blob1.location[0]-blob2.location[0])**2 + (blob1.location[1]-blob2.location[1])**2) < radius * 2:
        # print(blob1.name,"and",blob2.name,'collided')
        return True
    else:
        pass

def lookAheadCheckCollision(blob1, blob2, radius, time_Elapsed, gravity):
    future_x = blob1.location[0] + blob1.velocity[0] * time_Elapsed
    future_y = blob1.location[1] + (blob1.velocity[1] + 0.5 * gravity * (time_Elapsed)**2) * time_Elapsed
    if math.sqrt((future_x-blob2.location[0])**2 + (future_y-blob2.location[1])**2) < radius * 2:
        # print(blob1.name,"and",blob2.name,'collided')
        return True
    else:
        pass

def resolvePhysicalCollision(blob1,blob2,dampen):
    for i in [0,1]:
        blob1.velocity[i] , blob2.velocity[i] = dampen*blob2.velocity[i] , dampen*blob1.velocity[i]