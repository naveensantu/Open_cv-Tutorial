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

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text="first text on image", org=(10,500), fontFace=font, fontScale=3, color=(255,255,255), thickness=3, lineType=cv2.LINE_AA)
plt.imshow(blank_img)

new_blank=np.zeros(shape=(512,512,3))
plt.imshow(new_blank)

verticies = np.array([ [100,100],[100,400],[400,400],[400,100] ],dtype=np.int32)
pts=verticies.reshape((-1,1,2))

cv2.polylines(new_blank,[pts],isClosed=True, color=(255,0,0), thickness=5)

plt.imshow(new_blank)
