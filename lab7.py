#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

#A) 28x28 boyutlarında içeriği 0 ve 1 olan bir matris üretiniz.
#B) A'da üretilen matriste 1'leri içeren MBR dikdörtgeni üreten fonksiyonu yazınız.
#C) Kendisine aktarılan 2 vektörün benzerliğini döndüren fonksiyonu yazınız.
#D) A'da yazılan fonksiyonu kullanarak 100 farklı matris elde edip, 
#1. üretilen ile diğerlerini karşılaştırıp, yakınlığını ve benzerliğini listeleyiniz.

def randomMatrisGenerator(): #28x28 random array oluşturan fonksiyon
    return np.random.randint(0,2,(28,28))

def findMBR(array): #Verilen array'e göre min,max, X ve Y'yi bulan fonksiyon
    MBR ={"minX": 28,"maxX": 0,"minY": 28,"maxY": 0}
    satirsayisi,sutunsayisi=0,0
    for satir in array:
        for eleman in satir:
            if(eleman==1 and MBR["minX"]>sutunsayisi+1):
                MBR["minX"]=sutunsayisi+1
            if(eleman==1 and MBR["maxX"]<sutunsayisi+1):
                MBR["maxX"]=sutunsayisi+1
            if(eleman==1 and MBR["minY"]>satirsayisi+1):
                MBR["minY"]=satirsayisi+1
            if(eleman==1 and MBR["maxY"]<satirsayisi+1):
                MBR["maxY"]=satirsayisi+1
            sutunsayisi=sutunsayisi+1
        satirsayisi=satirsayisi+1
        sutunsayisi=0
    return MBR  

def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            if(character_a[i,j]==character_b[i,j]):
                my_similarity=my_similarity+1
    return my_similarity

for i in range(100):
    if(i==0):
        anaCharacter = randomMatrisGenerator()
        enBenzer = 0
    digerCharacter = randomMatrisGenerator()
    benzerlik = get_similarity(anaCharacter,digerCharacter)

    if(benzerlik>enBenzer):
        enBenzer = benzerlik
        enBenzerCharacter = digerCharacter
        
print("Benzerliği en yüksek karakter: ", enBenzer, " Oranı: ",round(enBenzer/784.0*100,2))
plt.imshow(anaCharacter,cmap='gray')
plt.show()
plt.imshow(enBenzerCharacter,cmap='gray')
plt.show()




# In[ ]:




