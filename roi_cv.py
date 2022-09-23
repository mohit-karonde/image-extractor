import cv2
import  numpy as np

img = cv2.imread("resources/IMG_3458-01.jpeg")
img = cv2.resize(img,(640,480))
img1 = cv2.resize(img,(640,480))
#(y1:y2) (x1:x2) = x1 -x2 = 152
roi =img1[100:355,200:352]
img1[100:355,362:514] = roi
cv2.imshow("printed image",img1)
cv2.imshow("cropped roi",roi)

cv2.imshow("image",img)
cv2.waitKey(0)