# # NumPy and Image Assessment
# **COMPLETE THE TASKS IN BOLD BELOW.**

# **TASK: Import NumPy**
import numpy as np


# **TASK: Create a 5 by 5 array where every number is a 10**
array=np.ones(shape=(5,5))*10
array

# **TASK: Run the cell below to create an array of random numbers and see if you can figure out how it works.**
# This line sets a "seed" so you get the same random numbers we do
np.random.seed(101)
# This line creates an array of random numbers
arr = np.random.randint(low=0,high=100,size=(5,5))
arr

# **TASK: What are the largest and smalled values in this array?**
arr.max()
arr.min()

# **TASK: Use PIL and matplotlib to read and display the ../DATA/00-puppy.jpg image.**
from PIL import Image
import matplotlib.pyplot as plt
%matplotlib inline
picture=Image.open("D://Numpy practice//download.jpg")

# **TASK: Convert the image to a NumPy Array**
picture_array=np.asarray(picture)
type(picture_array)
picture_array.shape


# **FINAL TASK: Use slicing to set the RED and GREEN channels of the picture to 0, then use imshow() to show the isolated blue channel**
pa_blue=picture_array.copy()
pa_blue[:,:,0]=0
pa_blue[:,:,1]=0
plt.imshow(pa_blue)

# ## Great Job!
