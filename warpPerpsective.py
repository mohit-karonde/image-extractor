import cv2
import  numpy as np

img =cv2.imread("resources/card.jpg")
img=cv2.resize(img,(512,512))

width,height = 250,350

pt1 = np.float32([[290,118],[420,176],[221,342],[386,435]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pt1,pt2)

warp_image =cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("original image",img)
cv2.imshow("warp Image",warp_image)
cv2.waitKey(0)