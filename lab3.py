#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew

im_1=plt.imread("test.jpg")
im_1.setflags(write=1)

def my_function(x):
    return 255-x

def inverse(image):
    image[:,:,0]=my_function(image[:,:,0])
    image[:,:,1]=my_function(image[:,:,1])
    image[:,:,2]=my_function(image[:,:,2])
    
def mean(image):
    print("Kirmizi icin renk ortalamasi : ",np.mean(im_1[:,:,0]))
    print("Yesil icin renk ortalamasi : ",np.mean(im_1[:,:,1]))
    print("Mavi icin renk ortalamasi : ",np.mean(im_1[:,:,2]))
    
def median(image):
    print("Kirmizi icin medyan : ",np.median(im_1[:,:,0]))
    print("Yesil icin medyan : ",np.median(im_1[:,:,1]))
    print("Mavi icin medyan : ",np.median(im_1[:,:,2]))
    
def mode(image):
    print("Kirmizi icin mod  : ",stats.mode(im_1[:,:,0]))
    print("Yesil icin mod  : ",stats.mode(im_1[:,:,1]))
    print("Mavi icin mod  : ",stats.mode(im_1[:,:,2]))
    
def histogram(image):  
    H_R={}
    for i in range (image.shape[0]):
        for j in range (image.shape[1]):
            if(image[i,j,0] in H_R.keys()):
                H_R[image[i,j,0]]=H_R[image[i,j,0]]+1
            else:
                H_R[image[i,j,0]]=1
                
    H_G={}
    for a in range (image.shape[0]):
        for b in range (image.shape[1]):
            if(image[a,b,1] in H_G.keys()):
                H_G[image[a,b,1]]=H_G[image[a,b,1]]+1
            else:
                H_G[image[a,b,1]]=1
                
    H_B={}
    for x in range (image.shape[0]):
        for y in range (image.shape[1]):
            if(image[x,y,2] in H_B.keys()):
                H_B[image[x,y,2]]=H_B[image[x,y,2]]+1
            else:
                H_B[image[x,y,2]]=1
    
    plt.bar(list(H_R.keys()), list(H_R.values()), color='r')
    plt.show()
    
    plt.bar(list(H_G.keys()), list(H_G.values()), color='g')
    plt.show()
    
    plt.bar(list(H_B.keys()), list(H_B.values()), color='b')
    plt.show()
            
def ceyreklik(image):
    print("Kirmizi icin Q1 degeri = ",np.percentile(image[:,:,0],25))
    print("Kirmizi icin Q2 degeri = ",np.percentile(image[:,:,0],50))
    print("Kirmizi icin Q3 degeri = ",np.percentile(image[:,:,0],75))
    print("Yesil icin Q1 degeri = ",np.percentile(image[:,:,1],25))
    print("Yesil icin Q2 degeri = ",np.percentile(image[:,:,1],50))
    print("Yesil icin Q3 degeri = ",np.percentile(image[:,:,1],75))
    print("Mavi icin Q1 degeri = ",np.percentile(image[:,:,2],25))
    print("Mavi icin Q2 degeri = ",np.percentile(image[:,:,2],50))
    print("Mavi icin Q3 degeri = ",np.percentile(image[:,:,2],75))
    print("Kirmizi icin iqr degeri = ",iqr(image[:,:,0]))
    print("Yesil icin iqr degeri = ",iqr(image[:,:,1]))
    print("Mavi icin iqr degeri = ",iqr(image[:,:,2]))
    
def ss(image):
    print("Kirmizi icin skewness degeri = ",skew(image[:,:,0]))
    print("Yesil icin skewness degeri = ",skew(image[:,:,1]))
    print("Mavi icin skewness degeri = ",skew(image[:,:,2]))


#mean(im_1)
#mode(im_1)
#median(im_1)
#histogram(im_1)
#ceyreklik(im_1)
#ss(im_1)
#inverse(im_1)
 



