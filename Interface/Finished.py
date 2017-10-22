from tkinter import Frame, Tk, Label


class Finished(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.label = Label(self, text="No more duplicates!")
        self.label.pack()
