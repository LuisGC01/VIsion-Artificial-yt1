#!/usr/bin/env python
# coding: utf-8

# # HIstosgramas

# In[5]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[6]:


img=cv2.imread('img2.jpg',-1)
cv2.imshow('goku',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


color=('b','g','r')


# In[ ]:


for channel, col in enumerate(color):
    histr=cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.title('histo')
plt.show()
while True:
    k=cv2.waitKey(0) & 0xFF
    if k ==27 : break
cv2.destroyAllWindows()


# In[ ]:




