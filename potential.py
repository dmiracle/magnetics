# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:40:15 2018

@author: dylan
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
from mpl_toolkits.mplot3d import axes3d



MAGCONFIGR=[
    [1, 0, 0],
    [2, 0, 0],
    [-1, 0, 0],
    [-2, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [0,-1, 0],
    [0, -2, 0],
    [2*m.cos(1*m.pi/4), 2*m.sin(1*m.pi/4), 0],
    [2*m.cos(3*m.pi/4), 2*m.sin(3*m.pi/4), 0],
    [2*m.cos(5*m.pi/4), 2*m.sin(5*m.pi/4), 0],
    [2*m.cos(7*m.pi/4), 2*m.sin(7*m.pi/4), 0]] 

MAGCONFIGM=[[0, 0, 1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, -1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]]       

MAGCONFIGR0=[[1, 0, 0],
    [2, 0, 0],
    [-1, 0, 0],
    [-2, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [0,-1, 0],
    [0, -2, 0],
    [2*m.cos(3*m.pi/4), 2*m.sin(3*m.pi/4), 0],
    [2*m.cos(7*m.pi/4), 2*m.sin(7*m.pi/4), 0]]

MAGCONFIGR1=[[1, 0, 1],
    [-1, 0, 1],
    [0, 1, 1],
    [0,-1, 1],
    [2*m.cos(1*m.pi/4), 2*m.sin(1*m.pi/4), 1],
    [2*m.cos(3*m.pi/4), 2*m.sin(3*m.pi/4), 1],
    [2*m.cos(5*m.pi/4), 2*m.sin(5*m.pi/4), 1],
    [2*m.cos(7*m.pi/4), 2*m.sin(7*m.pi/4), 1]]

MAGCONFIGM0=[[0, 0, 1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, -1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1]]

MAGCONFIGM1=[[0, 0, -1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, -1],
    [0, 0, 1],
    [0, 0, -1],
    [0, 0, 1]]

'''
def fieldplot(vec_field, lbb, rtf, mesh): # left-bottom-back, right-top-front, x-y-z
    xmin = lbb[0]
    xmax = rtf[0]
    ymin = lbb[1]
    ymax = rtf[1]
    zmin = lbb[2]
    zmax = rtf[2]
    x = np.arange(xmin, xmax, mesh[0])
    y = np.arange(ymin, ymax, mesh[1])
    z = np.arange(zmin, zmax, mesh[2]))

'''    
    

def vnorm(r):
    return m.sqrt(np.dot(r,r))

def unit(r):
    return(np.divide(r,vnorm(r)))
    
def Bdip(r,m):
    C = 1 # mu_0 m / 4 pi
    R = vnorm(r)
    uR = unit(r)
    vterms = 3*(np.multiply(np.dot(m,uR),uR))-m # 3(m \cdot \hat{r})\hat{r} - m
    return C*np.divide(vterms,R**3)
    
def Bnorth(r):
    return Bdip(r,[0,0,1])

def Bsouth(r):
    return Bdip(r,[0,0,-1])

def dippot(r0, r1, m0, m1): # U = - m \cdot B
    r = np.subtract(r1,r0)
    B = Bdip(r,m1)
    return -1*np.dot(m0,B)
        
def rotate(r, angle):
    R = [[m.cos(angle),-m.sin(angle),0],
          [m.sin(angle),m.cos(angle),0],
          [0,0,1]]
    return np.matmul(r,R)

def totalU(r0, r1, m0, m1):
    UU = 0
    for i, R0 in enumerate(r0):
        for j, R1 in enumerate(r1):
            Utmp = dippot(R0, R1, m0[i], m1[j])
            UU += Utmp
            # print("%d, %d, %f" % (i, j, Utmp))
    return UU        

def potential_sweep(r0, r1, m0, m1, res=50):
    theta=np.linspace(0,2*m.pi, num=res)
    potential=[]
    for angle in theta:
        rtmp = rotate(r1, angle)
        potential.append(totalU(r0, rtmp, m0, m1))
    return theta, potential


def angle_sweep(r0, res=50):
    theta=np.linspace(0,2*m.pi, num=res)
    rx=[]
    for angle in theta:
        rtmp = rotate(r0, angle)
        rx.append(rtmp[0])
    return theta, rx  
        