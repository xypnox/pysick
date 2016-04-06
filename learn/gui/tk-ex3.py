import tkinter as tk

root = tk.Tk()

l1 = tk.Label(root, text="User")
l2 = tk.Label(root, text="Password")

e1 = tk.Entry(root)
e2 = tk.Entry(root)

l1.grid(row=0, sticky=tk.E)
l2.grid(row=1, sticky=tk.E)
# E -> east
#      N
# <- S-+-E ->
#      W


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

c = tk.Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)
root.mainloop()
