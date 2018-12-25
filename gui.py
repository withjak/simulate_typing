from typing import type_now
from tkinter import *


root = Tk()
T = Text(root, height=50, width=80)
T.pack()

def retrieve_input():
    input = T.get("1.0",'end-1c')
    type_now(input)

B = Button(root, text = "simulate now", command = retrieve_input)
B.pack()

mainloop()
