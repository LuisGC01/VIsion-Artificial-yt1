#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


img = cv2.imread("img1.jpg")
rows, cols = img.shape[:2]


# In[3]:


kernel_x=cv2.getGaussianKernel(cols,200)
kernel_y=cv2.getGaussianKernel(rows,200)
kernel=kernel_y*kernel_x.T
mask=255*kernel/np.linalg.norm(kernel)
output=np.copy(img)


# In[4]:


for i in range(3):
    output[:,:,i]=output[:,:,i]*mask
cv2.imwrite('filtrado.jpg',output)


# In[ ]:




