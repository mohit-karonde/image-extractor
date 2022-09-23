import cv2
import pafy
import datetime
import imutils
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Tk
class weapon:

    def __init__(self):

        # Import the required Libraries

        # Create an instance of Tkinter frame
        win = Tk()
        win.title("weapon_image_extractor")

        # Set the geometry of Tkinter frame
        win.geometry("750x250")

        win.configure(background="navy blue")
        def display_text():
            global entry

            strink = entry.get()

            label.configure(text=strink)

        def run_weapon():
            try:
              #  url = input("enter the link")
                data = pafy.new(entry.get())
                data = data.getbest(preftype='mp4')

                camera = cv2.VideoCapture(0)
                camera.open(data.url)

                gun_cascade = cv2.CascadeClassifier('resources/cascade_gun.xml')
                #camera = cv2.VideoCapture(0)

                firstFrame = None
                gun_exist = False
                count = 0
                scount = 0

                while True:

                    ret, frame = camera.read()

                    frame = imutils.resize(frame, width=500)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    gun = gun_cascade.detectMultiScale(gray, 1.1, 2, minSize=(100, 100))

                    if len(gun) > 0:
                        gun_exist = True

                    for (x, y, w, h) in gun:
                        frame = cv2.rectangle(frame,(x, y),(x + w, y + h), (255, 0, 0), 2)
                        roi_gray = gray[y:y + h, x:x + w]
                        roi_color = frame[y:y + h, x:x + w]

                        cv2.imwrite("/root/Documents/frames/imgN%d.jpg" % count,frame)  # save frame as JPEG file ,dont forget to add / before root
                        # camera.set(cv2.CAP_PROP_POS_MSEC, (count ** 100))  # used to hold speed of frane generation

                        print('Read a new frame:', count, ret)
                        count += 1

                        y1 = y + w  # y+y bhi chalenga
                        x1 = x + h

                        # crop image
                        cut_img = frame[y:y1, x:x1]

                        # save cropped images
                        cv2.imwrite("/root/Documents/frameswrap/imgN%d.jpg" % scount, cut_img)
                        print('Read a new frame: scout', scount, ret)
                        scount += 1

                    if firstFrame is None:
                        firstFrame = gray
                        continue


                    # draw the text and timestamp on the frame
                    cv2.putText(frame, datetime.datetime.now().strftime("% A % d % B % Y % I:% M:% S % p"),
                                (10, frame.shape[0] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.35, (0, 0, 255), 1)

                    cv2.imshow("Security Feed", frame)
                    key = cv2.waitKey(1) & 0xFF



                    if key == ord('q'):

                        break

                    if gun_exist:
                        print("gun detected")


                    else:
                        print("guns NOT detected")

                camera.release()
                cv2.destroyAllWindows()

            #solution to runtime erroer
            except Exception as e:
                print(e," the input you gave is ",entry.get())




        # Initialize a Label to display the User Input
        label = tk.Label(win, text="Enter Youtube Link Here", font=("Courier 22 bold"), background="#808080", foreground="red")
        label.pack()

        # Create an Entry widget to accept User Input
        entry = Entry(win, width=40)
        entry.focus_set()
        entry.pack()
        strink = entry.get()


        # Create a Button to validate Entry Widget
        button = tk.Button(win, text="Okay", font=("Courier 22 bold"),background="#808080",foreground="red",width=20, command=run_weapon).pack(pady=20)

        win.mainloop()
