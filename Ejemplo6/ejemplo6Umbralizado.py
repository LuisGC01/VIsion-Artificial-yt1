#!/usr/bin/env python
# coding: utf-8

# # Umbralizado de una imagen

# umbralizando una imagen

# In[1]:


import cv2
import numpy as np


# In[2]:


img = cv2.imread('img1.jpg')
escalaGris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# In[10]:


umbral = cv2.adaptiveThreshold(escalaGris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('origina',img)
cv2.imshow('umbralizada',umbral)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[ ]:




