
# coding: utf-8

# In[5]:

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import imshow

img_1=plt.imread("Dock.jpg")

get_ipython().magic('matplotlib inline')
imshow(img_1)


# In[56]:

def rgb_grey_level(image_rgb):
    image_graylevel=plt.imread("Dock.jpg")
    m=image_rgb.shape[0]
    n=image_rgb.shape[1]
    for i in range (m):
        for j in range (n):
            deger=(image_rgb[i,j,0]**2+image_rgb[i,j,1]**2+image_rgb[i,j,2]**2)**.5
            if(deger>255):
                image_graylevel[i,j]=255
            else :
                image_graylevel[i,j]=deger
                
            
    return image_graylevel
            


# In[57]:

image_rgb = plt.imread("Dock.jpg")

image_graylevel=rgb_grey_level(image_rgb)
get_ipython().magic('matplotlib inline')
imshow(image_graylevel)


# In[58]:

def black_to_white(grey_level):
    image_black_white=plt.imread("Dock.jpg")
    m=grey_level.shape[0]
    n=grey_level.shape[1]
    for i in range (m):
        for j in range (n):
            if(grey_level[i,j,0]>127): 
                image_black_white[i,j,0]=255
                image_black_white[i,j,1]=255
                image_black_white[i,j,2]=255
            else :
                image_black_white[i,j,0]=0
                image_black_white[i,j,1]=0
                image_black_white[i,j,2]=0
            
    return image_black_white


# In[47]:

black_white=black_to_white(image_graylevel)
get_ipython().magic('matplotlib inline')
imshow(black_white)


# In[63]:

def constract(img_1):
    image_constract=plt.imread("Dock.jpg")
    m=img_1.shape[0]
    n=img_1.shape[1]
    for i in range (m):
        for j in range (n):
             
                image_constract[i,j,0]=255-img_1[i,j,0]
                image_constract[i,j,1]=255-img_1[i,j,1]
                image_constract[i,j,2]=255-img_1[i,j,2]
            
            
    return image_constract


# In[64]:

image_constract=constract(img_1)
get_ipython().magic('matplotlib inline')
imshow(image_constract)


# In[ ]:



