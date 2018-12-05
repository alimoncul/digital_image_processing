#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt


def get_distance(v,w=[1/3,1/3,1/3]):   #w ağırlık değeri
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    #d=((a*w1)**2+(b*w2)**2+(c*w3)**2)**.5 #sqrt işlemi var
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d

def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im_2[i,j]=get_distance(im_1[i,j,:])
    return im_2

def convert_rgb_to_BW(image_gray_level):
    m=image_gray_level.shape[0]
    n=image_gray_level.shape[1]
    im_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j]==0:
                im_bw[i,j]=0
            else:
                im_bw[i,j]=1
    return im_bw


def flatlist(liste):
    flat=[]
    for i in range (len(liste)):
        for j in range (len(liste)):
            flat.append(liste[i][j])
    return flat

def apply_mask(liste,mask=[1,1,1,1,1,1,1,1,1]):
    liste2=flatlist(liste)
    result=0
    if liste2==mask:
        result=1
    return result

def eresion(resim):
    m=resim.shape[0]   # siyah 0  beyaz 1 
    n=resim.shape[1]
    im4=np.zeros((m,n))
    for i in range (0,m-2):
        for j in range(0,n-2):
            b=im3[i:i+3,j:j+3]
            im4[i,j]=apply_mask(b)
    plt.imshow(im4,cmap='gray')
    plt.show()
    return im4

im1=plt.imread("erosion.png")
im1.setflags(write="1")
plt.imshow(im1)
plt.show()
im2=convert_rgb_to_gray_level(im1)
im3=convert_rgb_to_BW(im2)
im5=eresion(im3)
print(im5.shape,im3.shape)


# In[ ]:




