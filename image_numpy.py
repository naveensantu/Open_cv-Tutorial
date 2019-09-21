import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from PIL import Image
pic=Image.open("D://Computer Vision with OpenCV and Deep Learning//Computer-Vision-with-Python//DATA//00-puppy.jpg")
type(pic)
pic
pic_arr=np.asarray(pic)
type(pic_arr)
pic_arr.shape
plt.imshow(pic_arr)
pic_red=pic_arr.copy()
plt.imshow(pic_red)

pic_red.shape
plt.imshow(pic_red[:,:,0],cmap='gray')
plt.imshow(pic_red[:,:,1],cmap='gray')
plt.imshow(pic_red[:,:,2],cmap='gray')
pic_red[:,:,1]=0
pic_red[:,:,2]=0
plt.imshow(pic_red)
