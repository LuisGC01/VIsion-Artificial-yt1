#!/usr/bin/env python
# coding: utf-8

# # Extraccion de contornos con canny

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


img = cv2.imread('img1.jpg',0)
edges = cv2.Canny(img,100,200)


# In[3]:


plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('imagen original'),plt.xticks([]),plt.yticks([])


# In[4]:


plt.subplot(121),plt.imshow(edges,cmap='gray')
plt.title('imagen edge')
plt.show()


# In[ ]:




