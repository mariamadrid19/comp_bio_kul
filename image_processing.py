import cv2
import numpy as np

path = r'/Users/mariamadrid/Documents/Computational Biology/04-11-2022/checkerboard_18x18.png'
image = cv2.imread(path, 0)

cv2.imshow('view', image) 
cv2.waitKey()
cv2.destroyAllWindows()

# Size of image
print("Image size is ", image.shape)
# Data-type of image
print("Data type is ", image.dtype)
# Print the image pixel values
print(image)

#Change the middle pixels from black to white
## Read pixel
image[0][0]
# Add white pixels
img_copy = image.copy()
img_copy[9][9] = (255)
 
for cols_index in range(6,12):
    img_copy[6][cols_index] = 255
    img_copy[7][cols_index] = 255
    img_copy[8][cols_index] = 255
    img_copy[9][cols_index] = 255
    img_copy[10][cols_index] = 255
    img_copy[11][cols_index] = 255

print(img_copy)
     
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

path_2 = r'/Users/mariamadrid/Documents/Computational Biology/04-11-2022/Lake.jpg'
image_2 = cv2.imread(path_2)

cv2.imshow('view', image_2) 
cv2.waitKey()
cv2.destroyAllWindows()

(b,g,r) = cv2.split(image_2)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)

path_3 = r'/Users/mariamadrid/Documents/Computational Biology/04-11-2022/c_elegans_noisy.jpg'
image_3 = cv2.imread(path_3,0)

array_worm = np.empty(np.shape(image_3))
print(array_worm)
print(image_3.shape)
print(image_3.dtype)
print(image_3)

#Define your threshold at 120. Then set the pixels with value above the treshold to 255 and those 
#with value below the threshold to 0. Save the resulting image
for i in range(0, image_3.shape[0]):
    for j in range(0, image_3.shape[1]):
        if image_3[i][j] > 120:
            array_worm[i][j] = 255
        else:
            array_worm[i][j] = 0

print(array_worm)
cv2.imwrite('treshold_image.jpg', array_worm)
cv2.imshow('treshold_image.jpg', array_worm)
cv2.waitKey()

#Blur images using a 5x5 kernel
treshold_image_3 = cv2.threshold(image_3, 120, 255, cv2.THRESH_BINARY)
blured_image_3 = cv2.blur(image_3, (5,5))
Gaussian_blured_image_3 = cv2.GaussianBlur(image_3, (5,5), 0)
cv2.imshow('blured_image_3.jpg', blured_image_3)
cv2.imshow('Gaussian_blured_image_3.jpg', Gaussian_blured_image_3)
cv2.waitKey()

blured_threshold_image_3 = cv2.threshold(blured_image_3, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('blured_threshold_image_3.jpg', blured_threshold_image_3)
cv2.waitKey()
cv2.destroyAllWindows()