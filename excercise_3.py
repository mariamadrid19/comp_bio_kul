import cv2
import numpy as np

path = r'/Users/mariamadrid/Documents/Computational Biology/04-11-2022/c_elegans_noisy.jpg'
image = cv2.imread(path,0)

blured_image = cv2.blur(image, (5,5))
print(blured_image)
cv2.imshow('blured_image.jpg', blured_image)
array_worm = np.empty(np.shape(blured_image))

for i in range(0, blured_image.shape[0]):
    for j in range(0, blured_image.shape[1]):
        if blured_image[i][j] > 120:
            array_worm[i][j] = 255
        else:
            blured_image[i][j] = 0

cv2.imshow('blur_threshold_image.jpg', array_worm)
cv2.waitKey()