#Importing Image , Displaying Image Properties , Converting to Grayscale(using CV2 and Matplotlib) , displaying image , saving Output image.
#Source :https://pythonprogramming.net/loading-images-python-opencv-tutorial/
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\BATMAN\Desktop\Image Processing\Goku.jpg')
print("Image Properties :")
print(" - No.of Pixels :"+str(img.size))
print(" - Dimensions :"+str(img.shape))


img = cv2.imread(r'C:\Users\BATMAN\Desktop\Image Processing\Goku.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Display Image Using Matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()

#Saving Grayscale Image
cv2.imwrite('./Processed Images/GrayScale_goku.png',img)


