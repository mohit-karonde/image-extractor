import cv2
import pafy
import datetime
import imutils
import face_detection
import weapon_detection
import  colour_picker
import numberplate

print("welcome to image extractor")

print(" 1 = face Image Extraction"
      + " \n2 = weapon ImageExtraction"
     +"\ n3 = colour picker "
      + " \npress Q to break")

while True:


    j = input("choose any one ")

    if j == "1":
        num = numberplate.plate()
    elif j == "2":
        weapon_obj = weapon_detection.weapon()
    elif j == "q":
        break
    elif j == "3":
        colour_obj = colour_picker.colour()

    else:
        print("please give right output")




