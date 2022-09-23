# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides
import tkinter

import  imutils
import cv2
import pafy
from tkinter import *
from tkinter import Tk , Entry
from tkinter import ttk
import tkinter as tk

import  numpy as np
# load the required trained XML classifiers
# https://github.com/Itseez/opencv/blob/master/
# data/haarcascades/haarcascade_frontalface_default.xml
# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.

class face:
	def __init__(self):

		# Import the required Libraries


		# Create an instance of Tkinter frame
		win = Tk()
		win.title("face_Image_Extractor")

		# Set the geometry of Tkinter frame
		win.geometry("750x250")
		win.configure(background="navy blue")


		def display_text():
			global entry

			strink= entry.get()

			label.configure(text=strink)

		def run_face():
			try:
				face_cascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

				# https://github.com/Itseez/opencv/blob/master
				# /data/haarcascades/haarcascade_eye.xml
				# Trained XML file for detecting eyes
				eye_cascade = cv2.CascadeClassifier('resources/haarcascade_eye.xml')
				#url = input("enter the link")

				data = pafy.new(entry.get())
				data = data.getbest(preftype='mp4')

				camera = cv2.VideoCapture(0)
				camera.open(data.url)
				# capture frames from a camera


				count = 0

				scount = 0

				# loop runs if capturing has been initialized.
				while 1:

					# reads frames from a camera
					ret, img = camera.read()

					# convert to gray scale of each frames
					gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

					# Detects faces of different sizes in the input image
					faces = face_cascade.detectMultiScale(gray,1.3,5)

					for (x,y,w,h) in faces:
						# To draw a rectangle in a face
						cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
						#cut_img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
						roi_gray = gray[y:y+h, x:x+w]
						roi_color = img[y:y+h, x:x+w]

						# Detects eyes of different sizes yin the input image
						eyes = eye_cascade.detectMultiScale(roi_gray)

						y1=y+w # y+y bhi chalenga
						x1= x+h

						#crop image
						cut_img = img[y:y1,x:x1]

                        #save croped images
						cv2.imwrite("/root/Documents/frameswrap/imgN%d.jpg" % scount,cut_img)
						print('Read a new frame: scout', scount, ret)
						scount += 1

						#To draw a rectangle in eyes
						for (ex,ey,ew,eh) in eyes:
							cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
							cv2.imwrite("/root/Documents/frames/imgN%d.jpg" % count, img)
							print('Read a new frame:', count, ret)
							count += 1






					# Display an image in a window
					cv2.imshow('image',img)

					# Wait for Esc key to stop
					k = cv2.waitKey(1) & 0xff
					if k == 27:
						break

				# Close the window
				camera.release()

				# De-allocate any associated memory usage
				cv2.destroyAllWindows()

			except Exception as e:
				print(entry.get(), e)



		# Initialize a Label to display the User Input
		label = tk.Label(win, text="Enter Youtube Link Here", font=("Courier 22 bold"),background="#808080",foreground="red")
		label.pack()

		# Create an Entry widget to accept User Input
		entry = tkinter.Entry(win,background="yellow",width=40)
		entry.focus_set()
		entry.pack()
		strink = entry.get()




		# Create a Button to validate Entry Widget
		button = tk.Button(win, text="Submit",font=("Courier 22 bold"),background="#808080",foreground="red", width=20, command=run_face).pack(pady=20)

		win.mainloop()




