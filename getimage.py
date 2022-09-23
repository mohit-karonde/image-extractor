import cv2
import numpy as np
img = cv2.imread("resources/IMG_3475-01.jpeg")
img =cv2.resize(img,(300,300)) #resize
cv2.imshow("first",img)
print(img.shape)#size of image
imageresize = cv2.resize(img,(400,400))
cv2.imshow("image",imageresize)

cv2.waitKey(10000)

