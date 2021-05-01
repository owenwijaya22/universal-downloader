from tkinter import *
def print_input(*args):
    for entry in entries:
        print(entry.get())
root = Tk()
entries = [Entry(root) for _ in range(2)]
for entry in entries:
    entry.pack()

btn = Button(root, text="Print", command=print_input)
root.mainloop()