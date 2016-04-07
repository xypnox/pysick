import tkinter as tk


class AdiButton:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        b1 = tk.Button(frame, text="I print stuff", command=self.printMessage)
        b1.pack(side=tk.LEFT)

        b2 = tk.Button(frame, text="Quit Me", command=frame.quit)
        b2.pack(side=tk.RIGHT)

    def printMessage(self):
        print("Message from donbal")

root = tk.Tk()
new = AdiButton(root)
root.mainloop()
