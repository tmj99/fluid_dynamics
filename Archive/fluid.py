# make sure interpreter is at usr/local/Cellar/python/3.7.7/bin/python3
import pygame

import sys
sys.path.append('/Users/tianmj/repos/python_refresher/fluid_dynamics')

from run import running



gravity = 1

class blob:
    def __init__(self, location, velocity):
        self.location = location
        self.velocity = velocity

blob_a = blob([250,250],[0,0])

blob_loc_list = [blob_a]

for i in blob_loc_list:
    for j in i.location:
        print(j)

# runs the code 
running(blob_loc_list)