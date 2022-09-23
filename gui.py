import  tkinter as tk

import face_detection
import weapon_detection
import  colour_picker
import numberplate
import algo_choise




def show_msg():
         messagebox.showinfo("Message","Hey There! I hope you are doing well.")

def weap():
  wp = weapon_detection
  wp.weapon()

def faaace():

    f = face_detection
    f.face()


def quite():
    print("hellow")



def color_cmd():

    cp = colour_picker
    cp.colour()


def remove_sim():
    rm_sim = algo_choise
    rm_sim.choises()

def car_plate():
    cpd = numberplate
    cpd.plate()


app = tk.Tk()
app.title("Image Extractor")

        #app.geometry('480*480')

app.minsize(300,400)
app.maxsize(400,300)
label = tk.Label(app, text="Choose Desired Input", font= ('Aerial 17 bold italic'),background="#808080",foreground="red")
label.pack()
        #message = Label(text="welcome to image extractor",font=("ArialBold",17))
        #message.pack
        #message.grid(column=5,row=1)


face = tk.Button(app,text="Face Image Extract",font=("Aerial 17 bold italic",18),foreground="blue",background="#808080",command=faaace)
face.pack(fill=tk.BOTH, expand=True)



weapon = tk.Button(app,text="Weapon Image Extract",font=("Aerial 17 bold italic",18),foreground="blue",background="#808080",command=weap)
weapon.pack(fill=tk.BOTH, expand=True)

no_plate = tk.Button(app,text="Car No. Plate",font=("Aerial 17 bold italic",18),foreground="blue",background="#808080",command=car_plate)
no_plate.pack(fill=tk.BOTH, expand=True)


Rm_similiar_img = tk.Button(app,text="Remove Images",font=("Aerial 17 bold italic",23),foreground="blue",background="#009999",command=remove_sim)
Rm_similiar_img.pack(fill=tk.BOTH, expand=True)

colour = tk.Button(app,text="Colour Picker",font=("Aerial 17 bold italic",18),foreground="blue",background="#009999",command=color_cmd)
colour.pack(fill=tk.BOTH, expand=True)

Quite = tk.Button(app,text="Quite",font=("Aerial 17 bold italic",23),foreground="blue",background="#009999",command=quite)
Quite.pack(fill=tk.BOTH, expand=True)





app.mainloop()


