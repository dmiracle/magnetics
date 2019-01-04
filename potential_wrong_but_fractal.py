# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:40:15 2018

@author: dylan
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m


def dippot(r0 = [0,0,0,1], r1 = [1,1,1,1]):
    zterm = 3 * r1[2]**2 / (r1[2]**2 + (r1[0]-r0[0])**2 + (r1[1]-r0[1])**2)**5/2
    rterm = 1 / (r1[2]**2 + (r1[0]-r0[0])**2 + (r1[1]-r0[1])**2)**5/2
    root = zterm - rterm
    if (r0[3]-r1[3]==0):
        return -1 * root
    elif (r0[3]+r1[3]==0):
        return root
    else:
        print("mu's aren't right")
        

MAGCONFIGR0=[[1, 0, 0, 1],
    [2, 0, 0, -1],
    [-1, 0, 0, 1],
    [-2, 0, 0, -1],
    [0, 1, 0, -1],
    [0, 2, 0, 1],
    [0,-1, 0, -1],
    [0, -2, 0, 1],
    [2*m.cos(3*m.pi/4), 2*m.sin(3*m.pi/4), 0, 1],
    [2*m.cos(7*m.pi/4), 2*m.sin(7*m.pi/4), 0, 1]]

MAGCONFIGR1=[[1, 0, 1, -1],
    [-1, 0, 1, -1],
    [0, 1, 1, 1],
    [0,-1, 1, 1],
    [2*m.cos(1*m.pi/4), 2*m.sin(3*m.pi/4), 1, -1],
    [2*m.cos(3*m.pi/4), 2*m.sin(7*m.pi/4), 1, 1],
    [2*m.cos(5*m.pi/4), 2*m.sin(3*m.pi/4), 1, -1],
    [2*m.cos(7*m.pi/4), 2*m.sin(7*m.pi/4), 1, 1]]

MAGCONFIGM0=[[1, 0, 0, 1],
    [2, 0, 0, -1],
    [-1, 0, 0, 1],
    [-2, 0, 0, -1],
    [0, 1, 0, -1],
    [0, 2, 0, 1],
    [0,-1, 0, -1],
    [0, -2, 0, 1],
    [2*m.cos(3*m.pi/4), 2*m.sin(3*m.pi/4), 0, 1],
    [2*m.cos(7*m.pi/4), 2*m.sin(7*m.pi/4), 0, 1]]

MAGCONFIGM1=[[1, 0, 1, -1],
    [-1, 0, 1, -1],
    [0, 1, 1, 1],
    [0,-1, 1, 1],
    [2*m.cos(1*m.pi/4), 2*m.sin(3*m.pi/4), 1, -1],
    [2*m.cos(3*m.pi/4), 2*m.sin(7*m.pi/4), 1, 1],
    [2*m.cos(5*m.pi/4), 2*m.sin(3*m.pi/4), 1, -1],
    [2*m.cos(7*m.pi/4), 2*m.sin(7*m.pi/4), 1, 1]]


def rotate(r, angle):
    R = [[m.cos(angle),-m.sin(angle),0,0],
          [m.sin(angle),m.cos(angle),0,0],
          [0,0,1,0],
          [0,0,0,1]]
    return np.matmul(r,R)

def totalU(r0, r1):
    UU = 0
    for i, R0 in enumerate(r0):
        for j, R1 in enumerate(r1):
            Utmp = dippot(R0, R1)
            UU += Utmp
            # print("%d, %d, %f" % (i, j, Utmp))
    return UU        

def potential_sweep(r0, r1, res=50):
    theta=np.linspace(0,2*m.pi, num=res)
    potential=[]
    for angle in theta:
        r1 = rotate(r1, angle)
        potential.append(totalU(r0, r1))
    return theta, potential
        
        