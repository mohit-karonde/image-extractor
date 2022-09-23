import  cv2

cap = cv2.VideoCapture("resources/hero.mp4")



while True:
    ret , video = cap.read()
    cv2.imshow("video",video)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()