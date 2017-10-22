from tkinter import filedialog
import os
import Filescan
import Hasher
import Database
from Interface.Duplicates import Duplicates
from Interface.Finished import Finished
from Interface.Loading import Loading
from Interface.Scanning import Scanning
from Interface.Window import Window


interface = Window()
interface.show_frame(Scanning)

db = Database.Database()

filename = filedialog.askdirectory(initialdir=".", title="Select Directory")

scanner = Filescan.Filescan(filename)
images = scanner.scan(interface.get_frame())
image_count = len(images)

loading = interface.show_frame(Loading)
loading.progressbar.configure(length=image_count, value=0)

for index, image in enumerate(images):
    db.add_img(image, Hasher.Hasher.hash(image))
    loading.label.configure(text="Hashing %s of %s" % (index, image_count))
    loading.progressbar.configure(value=index)
    loading.progressbar.update()
    loading.progressbar.update_idletasks()

duplicates = interface.show_frame(Duplicates)

dup_list = db.get_duplicates()


def remove_img(path):
    os.remove(path)
    for dup in dup_list[:]:
        if dup[0] == path or dup[1] == path:
            dup_list.remove(dup)

    show_next_duplicate()


def show_next_duplicate():
    if len(dup_list) <= 0:
        interface.show_frame(Finished)
        return

    dup = dup_list.pop()
    duplicates.update_duplicates(dup, remove_img)
    duplicates.winfo_toplevel().title("Resolving Duplicates | %s Left" % len(dup_list))


show_next_duplicate()
interface.mainloop()
