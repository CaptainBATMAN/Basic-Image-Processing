import cv2
from scipy import misc
import numpy as np

ascent = misc.ascent()
import matplotlib.pyplot as plt
plt.axis("off")
plt.gray()
plt.imshow(ascent)
plt.show()

import scipy.misc
face = scipy.misc.face()
print(face.shape)
print(face.max)
print(face.dtype)
plt.axis("off")
plt.gray()
plt.imshow(face)
plt.show()


img = plt.imread(r'C:\Users\BATMAN\Desktop\Image Processing\whipsplash.jpg')
print(img[:3])
plt.axis("off")
plt.imshow(img)
plt.show()

#displaying Lum_img
lum_img = img[:,:,1]
print(lum_img)
plt.axis("off")
imgplot = plt.imshow(lum_img)
plt.show()

whip = plt.imread(r'C:\Users\BATMAN\Desktop\Image Processing\Naruto.jpg')
plt.axis("off")
plt.imshow(whip)
plt.show()

def tint(img , percent):
    tinted_img=img + (np.ones(img.shape)-img)*percent
    return tinted_img

percent=input("Enter Percentage to tint (0-1) :")
percent=float(percent)
tinted_img=tint(whip,percent)
plt.axis("off")
plt.imshow(tinted_img)
cv2.imshow("Tinted_img",tinted_img)
cv2.imwrite("./Processed Images/Tinted_Naruto.jpg",tinted_img)
plt.show()



def shade(img , percent):
    shaded_img=img *(1- percent)    
    return shaded_img

percent=input("Enter Percentage to shade (0-1) :")
percent=float(percent)
shaded_img=shade(whip,percent)
plt.axis("off")
plt.imshow(shaded_img)
cv2.imshow("shaded_img",shaded_img)
cv2.imwrite("./Processed Images/Shaded_Naruto.jpg",shaded_img)
plt.show()
