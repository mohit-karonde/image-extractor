import cv2
import numpy as np

num_rows = 10
num_cols = 10
#Created an image (really an ndarray) with three channels
new_image = np.ndarray((3, num_rows, num_cols), dtype=int)

#Did manipulations for my project where my array values went way over 255
#Eventually returned numbers to between 0 and 255

#Converted the datatype to np.uint8
new_image = new_image.astype(np.uint8)

#Separated the channels in my new image
new_image_red, new_image_green, new_image_blue = new_image

#Stacked the channels
new_rgb = np.dstack([new_image_red, new_image_green, new_image_blue])


#Displayed the image
cv2.imshow("image", new_rgb)
cv2.imshow("new green image", new_image_green)
cv2.imshow("new blue image", new_image_blue)
cv2.imshow("new red image", new_image_red)

print(new_rgb.shape)
cv2.waitKey(0)