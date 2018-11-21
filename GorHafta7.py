
# coding: utf-8

# In[1]:

print("enes")


# In[14]:

# a sorusunun cevabi
import numpy as np
import random
def matris_create():
    my_matris=np.zeros(shape=(28,28))
    for i in range(28):
        for j in range(28):
            my_matris[i,j]=random.randint(0,1)
    return my_matris


# In[17]:

# b sorusu
def MBR_create_28_by_28_with_0_1(matrix_a):
    m=matrix_a.shape[0]
    n=matrix_a.shape[1]
    x_min=m
    x_max=0
    y_min=n
    y_max=0
    for i in range(m):
        for j in range(n):
            if(matrix_a[i,j]==1 and x_min>i):
                x_min=i
            if(matrix_a[i,j]==1 and x_max<i):
                x_max=i
            if(matrix_a[i,j]==1 and y_min>i):
                y_min=i
            if(matrix_a[i,j]==1 and y_max<i):
                y_max=i
    return (x_min,x_max,y_min,y_max)
# c sorusu

def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity + character_a[i,j] * character_b[i,j]
    return my_similarity


# In[19]:

c_1=matris_create()
matris=matris_create()
get_similarity(matris,c_1)


# In[20]:

# d sorusu
def get_similarity_for_100_characters(kac_karakter=100):
    characters=[]
    for i in range(kac_karakter):
        new_char=matris_create()
        characters.append(new_char)
    for i in range(kac_karakter):
        benzerlik=get_similarity(characters[0],characters[i])
        print("0 -- "+str(i)+"  ",benzerlik)


# In[21]:

c_1=matris_create()
matris=matris_create()
get_similarity(matris,c_1)
get_similarity_for_100_characters(10)


# In[ ]:



