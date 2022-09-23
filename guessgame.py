import time
import random
import tkinter as tk

root = tk.Tk()
root.title("The Number Guessing Game")

count = guess = 0

label = tk.Label(root, text="The Number Guessing Game", font="Helvetica 20 italic")
label.pack(fill=tk.BOTH, expand=True)


def pick_number():
    global randomnum
    label.config(text="I am tkinking of a Number", fg="black")
    randomnum = random.choice(range(10000)) / 100
    entry.focus_force()


def main_game(guess):
    global count
    count = count + 1
    entry.delete("0", "end")
    if guess < randomnum:
        label["text"] = "Higher!"
    elif guess > randomnum:
        label["text"] = "Lower!"
    else:
        label.config(text=f"CORRECT! You got it in {count} tries", fg="red")
        root.update()
        time.sleep(4)
        pick_number()
        count = 0


def get(ev=None):
    guess = entry.get()
    if len(guess) > 0 and guess.lower() == guess.upper():
        guess = float(guess)
        main_game(guess)
    else:
        label["text"] = "MUST be A NUMBER"
        entry.delete("0", "end")


entry = tk.Entry(root, font="Helvetica 15 normal")
entry.pack(fill=tk.BOTH, expand=True)
entry.bind("<Return>", get)
b1 = tk.Button(root, text="Guess", command=get)
b1.pack(fill=tk.BOTH, expand=True)

pick_number()

root.geometry("470x110")
root.minsize(470, 110)

root.mainloop()
