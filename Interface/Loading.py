from tkinter import Frame, Tk, Label
from tkinter.ttk import Progressbar


class Loading(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.parent = parent
        self.winfo_toplevel().title("Hashing Images")
        self.make_widgets()

    def make_widgets(self):
        self.label = Label(self, text="Hashing image X of Y")
        self.label.pack()

        self.progressbar = Progressbar(self, orient="horizontal")
        self.progressbar.pack(fill='x', expand=1, padx=20, pady=20)
