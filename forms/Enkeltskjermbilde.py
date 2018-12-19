# Enkelt skjermbilde
from tkinter import *
#lag skjermbilde
# root =  Tk()
# root.title("Enkelt skjermbilde")
# root.geometry("200x100")

#start skjermbilde


master = Tk()
master.title("Enkelt skjermbilde")
master.geometry("200x100")

#master.mainloop()
MODES = [
    
        ("Monochrome", "1"),
        ("Grayscale", "L"),
        ("True color", "RGB"),
        ("Color separation", "CMYK"),
    ]

v = StringVar()
v.set("1") # initialize

for text, mode in MODES:
    b = Radiobutton(master, text=text,
                        variable=v, value=mode)
    b.pack(anchor=W)
print(b,"valgt verdi")
master.mainloop()    
    


# master = Tk()
# master.title("Skjembilde med knapper")
# master.geometry("300x300")
# 
# v = IntVar()
# 
# Radiobutton(master, text="Knapp nr1", variable=v, value=1).pack(anchor=W)
# Radiobutton(master, text="Knapp nr 2", variable=v, value=2).pack(anchor=W)
# 
# mainloop()