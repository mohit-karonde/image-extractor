import cv2
import numpy as np

path = input("Enter the image path")
img = cv2.imread(path,0)
img = cv2.resize(img,(500,400))

cv2.imshow("image",img)

k = cv2.waitKey(0)

if k == ord("s"):
        cv2.imwrite("/root/Documents/mohit.png",img)
else:
        cv2.destroyAllWindows()
