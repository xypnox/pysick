import tkinter as tk

root = tk.Tk()

l1 = tk.Label(root, text="User")
l2 = tk.Label(root, text="Password")

e1 = tk.Entry(root)
e2 = tk.Entry(root)

l1.grid(row=0)
l2.grid(row=1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = tk.Button(root, text="cool")

root.mainloop()
