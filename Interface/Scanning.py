from tkinter import Frame, Label, PhotoImage, Tk


class Scanning(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.parent = parent
        self.get_frames()
        self.make_widgets()

    def get_frames(self):
        self.frames = [PhotoImage(file='loading.gif', format='gif -index %i' % i) for i in range(8)]

    def update_loading(self, ind=0):
        if ind >= len(self.frames):
            ind = 0
        frame = self.frames[ind]
        ind += 1
        self.loading.configure(image=frame)
        self.after(100, self.update_loading, ind)

    def make_widgets(self):
        self.label = Label(self, text="Select Directory")
        self.label.pack()

        self.loading = Label(self)
        self.loading.pack()

        self.after(0, self.update_loading, 0)

    def update_label(self, label):
        self.label.configure(text=label)
