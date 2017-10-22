import tkinter as tk

from Interface.Duplicates import Duplicates
from Interface.Finished import Finished
from Interface.Loading import Loading
from Interface.Scanning import Scanning


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frames = {}
        self.current_frame = None

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.setup_frames(container)

    def setup_frames(self, container):
        for F in (Scanning, Loading, Duplicates, Finished):
            frame = F(container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        self.current_frame = self.frames[name]
        self.current_frame.tkraise()
        return self.current_frame

    def set_frame(self, frame: tk.Frame):
        self.frame = frame

    def get_frame(self):
        return self.current_frame
