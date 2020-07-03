from tkinter import *
from tkinter import messagebox


class App():
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.attributes("-alpha", 0.5)
        self.frame = Frame(self.root, width=192, height=400,
                           borderwidth=0, relief=FLAT)
        self.frame.pack_propagate(False)
        self.frame.pack()
        self.bQuit = Button(self.frame, text="Quit",
                            command=self.root.quit)
        self.bQuit.pack(pady=20)
        self.bHello = Button(self.frame, text="Hello",
                             command=self.hello)
        self.bHello.pack(pady=20)

    def hello(self):
        messagebox.showinfo("Popup", "Hello!")


app = App()
app.root.mainloop()
