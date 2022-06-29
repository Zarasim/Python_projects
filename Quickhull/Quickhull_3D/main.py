#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:38:19 2021

@author: simone
"""


#from mpl_toolkits import mplot3d


from quickhull3D import * 
import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt
import time 
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(165)
points = np.random.rand(10, 3)   # 30 random points in 2-D


#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(points[:,0],points[:,1],points[:,2],marker = 'o',)
#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')
#
#print(points)

pts = [list(points[i]) for i in range(len(points))]

t0 = time.time()
res = quick(pts)
t1 = time.time()
print('Time spent by personal algorithm: ',t1-t0)


# Compute hull using Scipy package
t0 = time.time()
hull = ConvexHull(points) # hull.simplices are indexes in poins array of the convex hull
t1 = time.time()
print('Time spent by scipy algorithm: ',t1-t0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0],points[:,1],points[:,2],marker = '^',)
ax.scatter(res[:,0],res[:,1],res[:,2],marker = 'o',s=100,c='red')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


for simplex in hull.simplices:
    
    ax.plot3D(points[simplex, 0], points[simplex, 1],points[simplex, 2],'green')
    