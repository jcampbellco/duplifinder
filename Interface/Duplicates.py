from tkinter import Frame, Tk, Label, Grid, Canvas, CENTER
from PIL import ImageTk, Image


class Duplicates(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        Grid.rowconfigure(parent, 0, weight=1)
        Grid.columnconfigure(parent, 0, weight=1)
        self.current_duplicate = None
        self.grid(row=0, column=0, sticky='nsew')
        self.make_widgets()
        self.bind('<Configure>', lambda event: self.redraw_images())

    def make_widgets(self):
        # self.label_container = Frame(self)

        self.left_label = Label(self, borderwidth=1, relief="groove")
        self.left_label.grid(row=0, column=0)

        self.right_label = Label(self, borderwidth=1, relief="groove")
        self.right_label.grid(row=0, column=1)

        # self.label_container.grid(row=0, column=0, columnspan=2, sticky='n')

        self.left_image = Canvas(self, borderwidth=1, relief="groove")
        Grid.rowconfigure(self, 1, weight=2, minsize=50)
        Grid.columnconfigure(self, 0, weight=2, minsize=50)
        self.left_image.grid(row=1, column=0, sticky='nsew')

        self.right_image = Canvas(self, borderwidth=1, relief="groove")
        Grid.rowconfigure(self, 1, weight=2, minsize=50)
        Grid.columnconfigure(self, 1, weight=2, minsize=50)
        self.right_image.grid(row=1, column=1, sticky='nsew')

    def update_duplicates(self, dup, callback):
        self.current_duplicate = dup
        self.left_label.configure(text=dup[0])
        self.right_label.configure(text=dup[1])

        self.left_image.img = Image.open(dup[0])
        self.left_image.bind("<Button-1>", lambda e, path=dup[1]: callback(path))

        print("Opening image")

        self.right_image.img = Image.open(dup[1])
        self.right_image.bind("<Button-1>", lambda e, path=dup[0]: callback(path))

        self.redraw_images()

    def redraw_images(self):
        if not hasattr(self.left_image, 'img') or not hasattr(self.right_image, 'img'):
            return

        self.redraw_image(self.left_image, (self.left_image.winfo_width(), self.left_image.winfo_height()))
        self.redraw_image(self.right_image, (self.right_image.winfo_width(), self.right_image.winfo_height()))
        self.update()
        self.update_idletasks()

    def redraw_image(self, label, size):
        if not hasattr(label, 'img'):
            return

        label.delete('all')
        im = label.img.copy()
        im.thumbnail(size)
        tkpi = ImageTk.PhotoImage(im)
        label.create_image((size[0]/2, size[1]/2), anchor=CENTER, image=tkpi)
        label.tkpi = tkpi
