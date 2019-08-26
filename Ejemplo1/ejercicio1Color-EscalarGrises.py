#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importando bibliotecas
import cv2


# In[11]:


image = cv2.imread('img2.png')


# In[12]:


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[13]:


cv2.imwrite('img1Gray.png',gray_image)
cv2.imshow('color imagen',image)
cv2.imshow('gris imagen',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




