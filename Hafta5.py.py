
# coding: utf-8

# In[1]:

import numpy as np


# In[18]:

mask_0=np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)
mask_0=mask_0/9


# In[3]:

mask_1=np.random.randint(5,size=9).reshape(3,3)
mask_2=np.random.randint(5,size=9).reshape(3,3)
print(mask_1)
print("--------------")
print(mask_2)
print("--------------")
print(mask_1*mask_2)


# In[4]:

sum(mask_1*mask_2)


# In[9]:

sum(sum(mask_1*mask_0))


# In[10]:

def get_default_max():
    return np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)/9
def apply_mask(part_of_image):
    mask=get_default_mask_for_mean()
    return sum(sum(part_of_image*mask))


# In[26]:

apply_mask(im_2[1:4,1:4])


# In[11]:

import matplotlib.pyplot as plt


# In[29]:

def get_mean_filter(im_1)
  #im_1=plt.imread('')

m=im_1.shape[0]
n=im_1.shape[1]
im_2=np.zeros((m,n))
   for i in range(1,m-1):
    for j in range(1,n-1):
        poi=im_1[i-1:i+2,j-1:j+2]
        print(poi.shape)
        input("enes")
        im_2[i,j]=apply_mask(poi)
return im_2


# In[28]:

mask_1=np.random.randint(20,size=9).reshape(3,3)
mask_1


# In[16]:

mask_1[:,0:1]


# In[ ]:



