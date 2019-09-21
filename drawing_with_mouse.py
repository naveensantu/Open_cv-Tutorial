import cv2
import numpy as np

def draw(event,x,y,flags,param):

    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),3)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.line(img,(x,y),(20,10),(255,0,0),3)
    


cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing",draw)

img=np.zeros((512,512,3))

while True:
    cv2.imshow("my_drawing",img)

    if cv2.waitKey(delay=20) & 0xff ==27:
        break

cv2.destroyAllWindows()
