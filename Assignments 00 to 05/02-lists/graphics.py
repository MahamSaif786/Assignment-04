# graphics.py - Simple Graphics Library using Tkinter
from tkinter import *

class GraphWin:
    def __init__(self, title="Graphics Window", width=400, height=400):
        self.win = Tk()
        self.win.title(title)
        self.canvas = Canvas(self.win, width=width, height=height)
        self.canvas.pack()
    
    def setBackground(self, color):
        self.canvas.configure(bg=color)

    def getMouse(self):
        self.win.mainloop()

    def create_rectangle(self, x1, y1, x2, y2, color="black"):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def set_color(self, item, color):
        self.canvas.itemconfig(item, fill=color)
    
    def wait_for_click(self):
        self.win.mainloop()

    def close(self):
        self.win.destroy()
