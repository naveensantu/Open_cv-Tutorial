# # Image Basics Assessment
import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib inline

# #### TASK: Open the *dog_backpack.jpg* image from the DATA folder and display it in the notebook. Make sure to correct for the RGB order.
image=cv2.imread(r"D:\Computer Vision with OpenCV and Deep Learning\Computer-Vision-with-Python\DATA\dog_backpack.jpg")
image_cvt=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_cvt)
image_cvt2=image_cvt.copy()

# #### TASK: Flip the image upside down and display it in the notebook.
image_flipped=cv2.flip(image_cvt, 0)
plt.imshow(image_flipped)

# #### TASK: Draw an empty RED rectangle around the dogs face and display the image in the notebook.
rectangle=cv2.rectangle(image_cvt,(200,750),(625,350),(255,0,0), thickness=7)
plt.imshow(image_cvt)

# #### TASK: Draw a BLUE TRIANGLE in the middle of the image. The size and angle is up to you, but it should be a triangle (three sides) in any orientation.
verticies=np.array([[250,700],[400,400],[650,700]],np.int32)
pts=verticies.reshape(-1,1,2)


triangle=cv2.polylines(image_cvt, [pts], isClosed=True, color=(0,0,255), thickness=10)
plt.imshow(image_cvt)


# ### BONUS TASK. Can you figure our how to fill in this triangle? It requires a different function that we didn't show in the lecture! See if you can use google search to find it.
cv2.fillPoly(image_cvt2, [pts], (0,0,255))
plt.imshow(image_cvt2)

# #### TASK:Create a script that opens the picture and allows you to draw empty red circles whever you click the RIGHT MOUSE BUTTON DOWN.

def create_circle(event,x,y,flag,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,0,255), thickness=10)

img = cv2.imread(r"D:\Computer Vision with OpenCV and Deep Learning\Computer-Vision-with-Python\DATA\dog_backpack.jpg")
cv2.namedWindow(winname="circle_on_dog")
cv2.setMouseCallback("circle_on_dog",create_circle)

while True:
    cv2.imshow("circle_on_dog",img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
