import tkinter as tk

root = tk.Tk()


def prt():
    print("Ouch! Fxn 1 was called")


def fxn2(event):
    'Note the usage of event'
    print("Oooh! Fxn 2 was called")


# Method 1 -> using command=fxnName |> Note that paranthese () are not used
b1 = tk.Button(root, text="Click me", command=prt)
b1.pack()

# Method 2 --> Function is passed an event and button is bound with the fxn
b2 = tk.Button(root, text="Click Anyme")
b2.bind('<Button-1>', fxn2)
b2.pack()

root.mainloop()
