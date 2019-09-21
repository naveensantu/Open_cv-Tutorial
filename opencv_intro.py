import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

img = cv2.imread("D://Numpy practice//download.jpg")
type(img)

img.shape

plt.imshow(img)
img2=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
img_gray=cv2.imread("D://Numpy practice//download.jpg",cv2.IMREAD_GRAYSCALE)
img_gray.shape
plt.imshow(img_gray,cmap="gray")
img2.shape
img_new=cv2.resize(img2,(150,60))
plt.imshow(img_new)
w_ratio=0.5
h_ratio=0.5
img_new1=cv2.resize(img2,(0,0),img2,w_ratio,h_ratio)
plt.imshow(img_new1)
flip_img=cv2.flip(img2, -1)
plt.imshow(flip_img)

type(img2)
cv2.imwrite("D://Numpy practice//cv2_new.jpg",flip_img)
