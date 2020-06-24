import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(16,16))         # Declaring the output graph's size

#Converting Image to GrayScale
oimage = cv2.imread(r'./whipsplash.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'./gs_whipsplash.jpg',oimage)

# Apply canny edge detector algorithm on the image to find edges
edges = cv2.Canny(oimage,100,200)

# Plot the original image against the processed Image.
plt.subplot(121), plt.imshow(oimage)
plt.axis("off")
plt.title('Original Image')
plt.subplot(122),plt.imshow(edges)
plt.axis("off")
plt.title('Edge Detected Image')

#Just to show the processed Image
# plt.imshow(edges)
# plt.axis("off")

#Display Image
plt.show()