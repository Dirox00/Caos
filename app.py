from tkinter import *

from PIL import ImageTk, Image

from Mandelbrot import *


class New_input:
    entries = []

    def __init__(self, name, default_text):
        self.entries.append(self)

        frame = Frame(inputs_frame, bg="white")
        frame.pack(fill=X)
        self.label = Label(frame, text=name+":", font=('Consolas', 14), bg="white")
        self.label.pack(side=LEFT, padx=20, pady=20,) #fill=X)
        self.inp = Entry(frame, width=15)
        self.inp.pack(side=RIGHT, padx=20)#fill=X, expand=True)
        self.inp.insert(END, str(default_text))

class New_info:
    info = []

    def __init__(self, name, default_text):
        self.info.append(self)

        frame = Frame(info_frame, bg="white")
        frame.pack(fill=X)
        self.label = Label(frame, text=name+":", font=('Consolas', 14), bg="white")
        self.label.pack(side=LEFT, padx=20, pady=20,) #fill=X)
        self.txt = Text(frame, width=20, height=1)
        self.txt.pack(side=RIGHT, padx=20)#fill=X, expand=True)
        self.txt.insert(INSERT, default_text)
    
    def insert_text(self, text):
        self.txt.delete('1.0', END)
        self.txt.insert(INSERT, text)


def show():
    img = ImageTk.PhotoImage(Image.open("try.png"))
    image_label.configure(image=img)
    image_label.image = img
    

window = Tk()  

window.geometry("1000x600")
window.title("Madelbrot set")

menu = Menu(window)
menu.config(bg="white")

filemenu = Menu(menu)
filemenu.config(bg="white")
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")

window.config(menu=menu, bg="white")

img = ImageTk.PhotoImage(Image.open("try2.png"))

image_label = Label(window, width=600, height=600, image=img, bg="white")
image_label.pack(side='left', fill='both', padx=5, pady=5, expand=True)


#-------------------------
right_frame = Frame(window, width=400, height=600, bg="white")
right_frame.pack(side='right', fill='both', padx=5, pady=5, expand=True)


inputs_frame = Frame(right_frame, width=300, height=300, bg="white")
inputs_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

New_input("Iterations", "50")
New_input("Image width", "600")
New_input("Image height", "600")

info_frame = Frame(right_frame, width=300, height=280, bg="white")
info_frame.pack(side='top', fill='both', padx=5, pady=5, expand=True)

New_info("Region", "-2,2,-2,-2")

buttons_frame = Frame(right_frame, width=300, height=20, bg="white")
buttons_frame.pack(side='bottom', fill='x', padx=5, pady=5)#, expand=True)

show_button = Button(buttons_frame, text="Show", command=show, width=10,font='Consolas', relief=RAISED, bg="white")
show_button.pack(side=RIGHT, padx=10, pady=10)

back_button = Button(buttons_frame, text= "<", command=show, width=1,font='Consolas', relief=RAISED, bg="white")
back_button.pack(side=LEFT, padx=10, pady=10)

fwd_button = Button(buttons_frame, text=">", command=show, width=1,font='Consolas', relief=RAISED, bg="white")
fwd_button.pack(side=LEFT, padx=10, pady=10)

window.mainloop()
