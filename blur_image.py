
import cv2
import numpy as np
kernal = np.ones((5,5),np.uint8,)

img = cv2.imread("resources/IMG_3458-01.jpeg")
img =cv2.resize(img,(300,300)) #resize
cv2.imshow("first",img)
print(img.shape) #size of image output will be on terminal


gray_image =cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb) #gray_image

cv2.imshow("gray image",gray_image)

image_blur = cv2.GaussianBlur(img,(7,7),0)#ksize should we always odd
cv2.imshow("Blur image",image_blur)

image_canny = cv2.Canny(img,200,300) #finding edges
cv2.imshow("image_canny",image_canny)

image_dialition = cv2.dilate(image_canny,kernal,iterations=1) #we defined kernal first in starting its a matrix using numpy
cv2.imshow("dialition image",image_dialition)

imageEroded = cv2.erode(image_dialition,kernal,iterations=1)
cv2.imshow("Eroded Image",imageEroded)

cv2.waitKey(10000)


