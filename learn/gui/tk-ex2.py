import tkinter as tk

root = tk.Tk()

# create frames to put objects in
topFrame = tk.Frame(root)
topFrame.pack()

bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

b1 = tk.Button(topFrame, text="cool", fg="red")
b2 = tk.Button(topFrame, text="cool2", fg="blue")
b3 = tk.Button(topFrame, text="cool3", fg="green")
b4 = tk.Button(bottomFrame, text="cool4", fg="purple")

b1.pack(side=tk.LEFT)
b2.pack(side=tk.LEFT)
b3.pack(side=tk.LEFT)
b4.pack(side=tk.BOTTOM)

root.mainloop()
