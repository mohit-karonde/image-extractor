import  cv2
import numpy as np

class colour:
     def __init__(self):

        def cross(x):
            pass

        img = np.zeros((350,480,3),np.uint8)
        cv2.namedWindow("colourPicker")

        #create switch

        s1 = "0=off/1=on"
        cv2.createTrackbar(s1,"colourPicker",0,1,cross)

        #creating trackbar to detect the colour
        #creating rgb
        cv2.createTrackbar("b","colourPicker",0,255,cross)
        cv2.createTrackbar("g","colourPicker",0,255,cross)
        cv2.createTrackbar("r","colourPicker",0,255,cross)

        while True:
            cv2.imshow("colourPicker",img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
              break




            s = cv2.getTrackbarPos(s1,"colourPicker")

            b = cv2.getTrackbarPos("b", "colourPicker")
            g = cv2.getTrackbarPos("g", "colourPicker")
            r = cv2.getTrackbarPos("r", "colourPicker")

            if s == 0:
                img[:]=0
            else:
                img[:]=[r,g,b]

        cv2.destroyAllWindows()