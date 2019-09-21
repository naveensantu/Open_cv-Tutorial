import numpy as np
import cv2



drawing = False
ix,iy = -1,-1

def draw(event,x,y,flags,params):

    global ix,iy,drawing

    if event== cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,255),3)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,255),3)


img = np.zeros((512,512,3),dtype="int32")
cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw)

while True:
    cv2.imshow("drawing",img)

    if cv2.waitKey(1) & 0xFF ==27:
        break

cv2.destroyAllWindows()
