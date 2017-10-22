import os
from tkinter import Frame


class Filescan:
    def __init__(self, path):
        self.path = path
        self.images = []

    def scan(self, frame: Frame):
        os.chdir(self.path)
        for root, dirs, files in os.walk(self.path):
            for file in files:
                self.images.append(os.path.join(root, file))
                frame.label.configure(text="Found %s images" % len(self.images))

        return self.images
