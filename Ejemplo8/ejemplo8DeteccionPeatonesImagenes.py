#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import imutils
from imutils.object_detection import non_max_suppression
import matplotlib.pyplot as plt


# In[2]:


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# In[3]:


ruta_img = 'img4.jpg'
imagen=cv2.imread(ruta_img)
image=imutils.resize(imagen,width=min(400,imagen.shape[1]))


# In[4]:


(rectas,weights)=hog.detectMultiScale(imagen,winStride=(1,1),padding=(4,4),scale=1.05)


# In[5]:


rectas=np.array([[x,y,x+w,y+h] for (x,y,w,h) in rectas])
eleccion=non_max_suppression(rectas,probs=None,overlapThresh=0.65)


# In[6]:


for (xA,yA,xB,yB) in eleccion:
    cv2.rectangle(imagen,(xA,yA),(xB,yB),(0,255,0),3)


# In[7]:


imagen=cv2.cvtColor(imagen,cv2.COLOR_RGB2BGR)
plt.imshow(imagen)


# In[ ]:




