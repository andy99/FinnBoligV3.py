import tkinter as tk
from tkinter import *
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

MODES = [
    
        ("Monochrome", "1"),
        ("Grayscale", "L"),
        ("True color", "RGB"),
        ("Color separation", "CMYK"),
    ]

v = StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = Radiobutton(myapp, text=text,
                        variable=v, value=mode)
    b.pack(anchor=W)


# start the program
myapp.mainloop()