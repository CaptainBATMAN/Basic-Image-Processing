#pillow is used as PIL in general

from PIL import Image

img=Image.open(r'./L.jpg').convert('L')
img.rotate(45)
# img.size
# img.format
img.save(r'./Processed Images/L_45.png')

import cv2
im=cv2.imread(r'./whipsplash.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()