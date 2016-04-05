import tkinter as tk

root = tk.Tk()  # main window

theLabel = tk.Label(root, text="I am so cool")
# creates a label to display text
# first parameter is where we want the label
# second is text="string" which is what is inside the label
theLabel.pack()
# packs the label, fills it to the main window

root.mainloop()
# main loop; without it the program runs once and exits
