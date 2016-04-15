import tkinter as tk


def doNothing():
    print("The baddest guy in the world is adiUltra")

root = tk.Tk()

# Menu Bar

Mymenu = tk.Menu(root)
root.config(menu=Mymenu)

fileMenu = tk.Menu(Mymenu)
Mymenu.add_cascade(label='Files', menu=fileMenu)
fileMenu.add_command(label='New', command=doNothing)
fileMenu.add_command(label='Open', command=doNothing)
fileMenu.add_command(label='Save', command=doNothing)
fileMenu.add_command(label='Save As', command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)

editMenu = tk.Menu(Mymenu)
Mymenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=doNothing)
editMenu.add_command(label='Copy', command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Settings', command=doNothing)

# toolBar

toolBar = tk.Frame(root, bg='grey')

pbutton = tk.Button(toolBar, text="I am dumb", command=doNothing)
pbutton.pack(side=tk.LEFT)
pbutton2 = tk.Button(toolBar, text="I am dumberts", command=doNothing)
pbutton2.pack(side=tk.LEFT)

toolBar.pack(side=tk.TOP, fill='x')

root.mainloop()
