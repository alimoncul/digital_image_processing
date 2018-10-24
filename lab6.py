#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    return math.sqrt((a**2)*w1 + (b**2)*w2 + (c**2)*w3)

def turn_rgb_to_gray_level(image_rgb):
    m,n=image_rgb.shape[0],image_rgb.shape[1]
    image_gray_level = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            image_gray_level[i,j]=get_distance(image_rgb[i,j,:])
    return image_gray_level

def grayscale_to_bw(image_gray):
    m,n=image_gray.shape[0],image_gray.shape[1]
    image_bw = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if(image_gray[i,j]==0):
                image_bw[i,j]=0
            else:
                image_bw[i,j]=1
    return image_bw

def pixel_compare(pixels):
    global internal
    global external
    siyah,beyaz=0,0
    for i in range(2):
        for j in range(2):
            if(pixels[i,j]==1):
                beyaz=beyaz+1
            else:
                siyah=siyah+1
    if(siyah>beyaz and beyaz>0):
        internal=internal+1      
    elif(beyaz>siyah and siyah>0):
        external=external+1

    
im_1=plt.imread("characters.png")
plt.show()
plt.imshow(im_1)
im_2=turn_rgb_to_gray_level(im_1)
im_3=grayscale_to_bw(im_2)

m,n=im_3.shape[0],im_3.shape[1]
internal,external=0,0


for i in range(1,m-1):
    for j in range(1,n-1):
            poi=im_3[i:i+2,j:j+2]
            pixel_compare(poi)
            
print("İç köşe sayısı: ",internal)
print("---")
print("Dış köşe sayısı: ",external)
print("---")
print("Nesne sayısı: ",math.fabs(internal-external)/4.0)
                




