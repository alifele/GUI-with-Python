import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

'''
this code will get an entity from the user and will print it
'''
class entry:
    def __init__(self,master):
        self.master = master

        e = tk.Entry(master)
        self.e = e
        e.pack()
        e.delete(0, tk.END)
        #e.insert(0, 'A default value')

        button = tk.Button(master, text = 'print', command = self.show)
        button.pack()

    def show(self):
        s = self.e.get()
        print(s)

root = tk.Tk()
my_gui = entry(root)
root.mainloop()
