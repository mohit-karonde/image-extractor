import cv2
print("Your OpenCV version is: " + cv2.__version__)

cap = cv2.VideoCapture(0);
cap.set(3,500)#height
cap.set(4,500)#weght
cap.set(10,50)#brightness




while True:
    success,img = cap.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break