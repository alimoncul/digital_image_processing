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

def turn_gray_level_to_bw(image_gray):
    m,n=image_gray.shape[0],image_gray.shape[1]
    image_bw = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if(image_gray[i,j]>128):
                image_bw[i,j]=1
            else:
                image_bw[i,j]=0
    return image_bw

im_1=mpimg.imread("test.jpg")
im_1.setflags(write=1)

im_2=turn_rgb_to_gray_level(im_1) #RGB to GRAYSCALE
im_3=turn_gray_level_to_bw(im_2) #GRAYSCALE to BLACK WHITE

plt.imshow(im_1)
plt.show()
plt.imshow(im_2,cmap='gray')
plt.show()
plt.imshow(im_3,cmap='gray') #cmap='gray' otomatik olarak sınır dışı değerleri eliyor siyah beyaz görüntü sağlıyor.
plt.show()





