import cv2
import pafy
import  datetime

url = "https://youtu.be/Fj1tGvMmdFY"
data = pafy.new(url)
data = data.getbest(preftype='mp4')

cap = cv2.VideoCapture()
cap.open(data.url)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("/root/Documents/mohit.avi",fourcc,20.0,(640,360))
"""put first width and height carefully  else it will not play after storing the video because video coming in some other
size and you are trying to grab in some other size you gave it week dont forgot"""


while(cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'height ' + str(cap.get(4)) + 'width ' +str(cap.get(3))
        date = 'date' + str(datetime.datetime.now())

        frame = cv2.putText(frame,text,(10,20),font,0.5,(0,155,255),1,cv2.LINE_AA)
        frame=cv2.putText(frame,date,(10,35),font,0.5,(255,224,33),1,cv2.LINE_AA)

        gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("colour video",frame)
        cv2.imshow("gray video",gray_scale)
       # frame = cv2.flip(frame,0) to flip the frame it will affect when you sav eit
        output.write(frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
output.release()
cv2.destroyAllWindows()