import numpy as np
import cv2
import imutils
from imutils.object_detection import non_max_suppression
import matplotlib.pyplot as plt


# In[2]:

cap=cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
	ret, imagen = cap.read()
	imagen=imutils.resize(imagen,width=400)
	(rectas,weights)=hog.detectMultiScale(imagen,winStride=(8,8),padding=(5,5),scale=1.05)
	rectas=np.array([[x,y,x+w,y+h] for (x,y,w,h) in rectas])
	eleccion=non_max_suppression(rectas,probs=None,overlapThresh=0.65)
	for (xA,yA,xB,yB) in eleccion:
		cv2.rectangle(imagen,(xA,yA),(xB,yB),(200,150,150),3)
	# if(len(eleccion)):
	# 	print("{} peatones encontrados".format(len(eleccion)))
	cv2.imshow("imagen de salida",imagen)
	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break
