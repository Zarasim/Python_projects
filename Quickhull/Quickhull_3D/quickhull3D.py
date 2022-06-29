#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:35:27 2021

@author: simone

Consider list of points [x,y,z] and convert in numpy array only at the end 
by flattening with pandas.core

"""

import numpy as np
import math
from pandas.core.common import flatten


def centroidpython(points):
    
    centroid_x = np.mean(points[:,0])
    centroid_y = np.mean(points[:,1])
    centroid_z = np.mean(points[:,2])

    return centroid_x,centroid_y,centroid_z


def distance_point_line(pt,line):
    
    v1 = [a - b for a, b in zip(line[1], line[0])]
    v2 = [a - b for a, b in zip(line[1], pt)]
    
    return np.linalg.norm(np.cross(v1,v2))/np.linalg.norm(v1)


def initial_plane(pts):
     
    minX = pts[0][0]
    maxX = pts[0][0]
    
    minXPoint = pts[0]
    maxXPoint = pts[0]
    
    for pt in pts:
        if pt[0] < minX:
            minX = pt[0]
            minXPoint = pt
        if pt[0] > maxX:
            maxX = pt[0]
            maxXPoint = pt
    
    # Find last point as the farthest from the line created by minXPoint and  maxXPoint 
    line = [minXPoint,maxXPoint]
    
    farthest_dist = 0
    
    for pt in pts:
        dist = distance_point_line(pt,line)
        if dist > farthest_dist:
            farthest_dist = dist
            pt3 = pt
    
    plane = [minXPoint,maxXPoint,pt3]
    
    return plane


def coeff_plane(plane):
    
    # FInd first coefficient a,b,c,d defining the plane ax + by + cz + d = 0
    v1 = [a - b for a, b in zip(plane[1], plane[0])]
    v2 = [a - b for a, b in zip(plane[2], plane[0])]
    
    a,b,c = np.cross(v1,v2)
    
    d = -(a*plane[0][0] + b*plane[0][1] + c*plane[0][2])
    
    return a,b,c,d


def distance_pt_plane(pt,plane):
    
    a,b,c,d = coeff_plane(plane)
    
    return (abs(a*pt[0] + b*pt[1] + c*pt[2] + d))/(np.sqrt(a**2 + b**2 + c**2))


def PointSide(pt, plane):
        
    coeff = coeff_plane(plane)
    d = np.dot(coeff,[pt[0],pt[1],pt[2],1])
    
    #print(d)
    if abs(d) < 1e-16:
        return 0
    elif d > 0:
        return 1
    elif d < 0:  
        return -1


def PointsOutside(points, plane):
 
    ret = []
    for pt in points:
        if (PointSide(pt,plane)) > 0:   
            ret.append(pt)
    return ret

def PointsInSide(points, plane):
    
    ret = []
    for pt in points:
        if (PointSide(pt,plane)) < 0:
            ret.append(pt)
    return ret


def PointFarthest(points, plane):
    
    if len(points) == 0:
        return None
    
    far = points[0]
    max_dist = distance_pt_plane(far,plane)
    
    for pt in points:
        dist = distance_pt_plane(pt,plane)
        if dist > max_dist:
            far = pt
            max_dist = dist
            
    return far


def GetNextPointOut(plane,ptsOut):
    
    if len(ptsOut) == 0:
        return plane
    
    farPoint = PointFarthest(ptsOut, plane)

    face1 = [plane[0],plane[1],farPoint]
    face2 = [plane[1],plane[2],farPoint]
    face3 = [plane[2],plane[0],farPoint]
    
    restOfPoints1 = PointsOutside(ptsOut,face1)
    restOfPoints2 = PointsOutside(ptsOut,face2)
    restOfPoints3 = PointsOutside(ptsOut,face3)
    
    r1 = GetNextPointOut(face1,restOfPoints1)
    r2 = GetNextPointOut(face2,restOfPoints2)
    r3 = GetNextPointOut(face3,restOfPoints3)
 
    return [r1,r2,r3]

def GetNextPointIn(plane,ptsIn):
    
    if len(ptsIn) == 0:
        return plane
    
    farPoint = PointFarthest(ptsIn, plane)

    face1 = [plane[0],plane[1],farPoint]
    face2 = [plane[1],plane[2],farPoint]
    face3 = [plane[2],plane[0],farPoint]
    
    restOfPoints1 = PointsOutside(ptsIn,face1)
    restOfPoints2 = PointsOutside(ptsIn,face2)
    restOfPoints3 = PointsOutside(ptsIn,face3)
    
    r1 = GetNextPointOut(face1,restOfPoints1)
    r2 = GetNextPointOut(face2,restOfPoints2)
    r3 = GetNextPointOut(face3,restOfPoints3)
 
    return [r1,r2,r3]

def quick(pts):
    
    #determining points with min and max X coordinate
    plane = initial_plane(pts)
    
    #print(plane)

    ptsOut = PointsOutside(pts,plane)
    ptsIn = PointsInSide(pts,plane)
  
    #print(ptsOut)
    #print(ptsIn)
    
    
    resultOut = GetNextPointOut(plane,ptsOut)
    resultIn = GetNextPointOut(plane,ptsIn)
    
    result= [resultOut,resultIn]
    res = list(flatten(result))
    res = np.array(res).reshape(-1,3)

    return np.unique(res,axis=0)


