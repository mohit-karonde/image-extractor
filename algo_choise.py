
from tkinter import Tk

import tkinter as tk
import  algo_remove_similar
import remove_similar


def rm_sim_1():
	al1 = algo_remove_similar
	al1.rmduplicate()


def rm_sim_2():
	al2 = remove_similar
	al2.rmduplicates()


class choises:

		def __init__(self):


			#Import the required Libraries


			# Create an instance of Tkinter frame
			win = Tk()
			win.title("face_Image_Extractor")

			# Set the geometry of Tkinter frame
			win.geometry("750x250")
			win.configure(background="navy blue")



			# Create a Button to validate Entry Widget
			button1 = tk.Button(win, text="COMPARE ONE TO All",font=("Courier 22 bold"),background="#808080",foreground="red", width=20, command=rm_sim_2).pack(pady=20)

			# Create a Button to validate Entry Widget
			button = tk.Button(win, text="COMPARE ONE TO NEXT 11", font=("Courier 22 bold"), background="#808080", foreground="red",width=20, command=rm_sim_1).pack(pady=20)

			win.mainloop()




