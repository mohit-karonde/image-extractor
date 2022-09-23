import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
img[0:100,0:200]=255,0,255

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
cv2.rectangle(img,(100,200),(200,350),(200,5,1),3)
cv2.circle(img,(300,300),7,(155,122,5),2)
cv2.putText(img,"mohit baba",(300,200),cv2.FONT_ITALIC,1,(50,20,11),2)
cv2.imshow("created image",img)
cv2.waitKey(10000)