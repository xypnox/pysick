# This file serves as GUI for Enigma

import tkinter as tk
import enigma

inst = null


def start(mode, root):
    global inst
    if mode == "encrypt":
        inst = enigma.encrypt()
    elif mode == "decrypt":
        inst = enigma.decrypt()

root = tk.Tk()

toolBar = tk.Frame(root, bg='grey')

EncButton = tk.Button(toolBar, text="Encrypt", command=start("encrypt", root))
EncButton.pack(side=tk.LEFT)
DecButton = tk.Button(toolBar, text="Decrypt", command=start("decrypt", root))
DecButton.pack(side=tk.LEFT)

root.mainloop()
