import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

blank_img=np.zeros(shape=(512,512,3))
blank_img.shape
plt.imshow(blank_img)
cv2.rectangle(blank_img,pt1=(100,100),pt2=(400,400),color=(255,255,255),thickness=10)
plt.imshow(blank_img)
cv2.circle(blank_img,(250,250),50,(255,0,0),-10)
plt.imshow(blank_img)

cv2.line(blank_img, (40,40), (450,40), (255,255,0), thickness=10)
plt.imshow(blank_img)
