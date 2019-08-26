#!/usr/bin/env python
# coding: utf-8

# # operaciones aritmeticas con imagenes

# dado que las imagenes contienen valores numericos atravez de los pixeles se pueden realizar operaciones aritmeticas

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np


# In[5]:


image = cv2.imread('img1.jpg')
image2 = cv2.imread('img2.jpg')


# In[6]:


suma = image + image2


# In[7]:


plt.imshow(suma)


# In[8]:


resta = image - image2


# In[9]:


plt.imshow(resta)


# In[10]:


mult = image * image2


# In[11]:


plt.imshow(mult)


# In[ ]:




