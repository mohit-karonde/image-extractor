import cv2
import numpy as np

video = cv2.VideoCapture(0)
#video.set(3,240)
#video.set(4,480)

#XVID,
fourcc = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("/root/Documents/output.avi",fourcc,20.0,(640,480))
while video.isOpened():
    success ,vid = video.read()
    if success == True:

        #vid = cv2.resize(vid,(300,300),)
        cv2.imshow("video",vid)
        gray_video = cv2.cvtColor(vid,cv2.COLOR_BGR2YCrCb)
        cv2.imshow("gray_vide0",gray_video)
        output.write(vid)

        if cv2.waitKey(1)& 0xff == ord("q"):
            break

video.release()
output.release()
cv2.destroyAllWindows()
