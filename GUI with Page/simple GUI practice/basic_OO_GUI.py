import numpy as np
from tkinter import Tk, Label, Button
from tkinter import LEFT, RIGHT, W, StringVar
import matplotlib.pyplot as plt




class  MyFirstGUI:
    LABEL_TEXT =[
    'this is my text',
    'hello there',
    'I am here',
    'Good buy'
    ]
    def __init__(self, master):
        self.master = master
        master.title('my first GUI')

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()
        #self.label.pack(side = LEFT)   #we have used this to position it inside the parent window
        #self.label.grid(columnspan=2, sticky=W)


        self.greet_button = Button(master, text= "plot sin function", command = self.greet)
        self.greet_button.pack(side = RIGHT)
        #self.greet_button.grid(row=1)

        self.close_button = Button(master, text = "Close", command=master.quit)
        self.close_button.pack()
        #self.close_button.grid(row=1, column=1)

    def greet(self):
        x = np.arange(0,10,0.1)
        y = np.sin(x)
        plt.plot(x,y)
        plt.show()

    def cycle_label_text(self, event):
        self.label_index +=1
        self.label_index %= len(self.LABEL_TEXT)
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
