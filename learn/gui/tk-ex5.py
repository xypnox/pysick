import tkinter as tk

root = tk.Tk()


def leftClick(event):
    print("Left was clicked")


def middleClick(event):
    print("Middle was Clicked")


def rightClick(event):
    print("Right was Clicked")

frame = tk.Frame(root, height=200, width=280)

frame.bind('<Button-1>', leftClick)
frame.bind('<Button-2>', middleClick)
frame.bind('<Button-3>', rightClick)

frame.pack()

root.mainloop()
