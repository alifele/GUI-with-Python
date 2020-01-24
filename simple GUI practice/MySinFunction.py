'''
You can find more detailes how to get the value of an Entry from the following artice:
https://effbot.org/tkinterbook/entry.htm
'''


import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

class Sin:
    def __init__(self, master):
        self.maser = master

        #Amplitude Entry
        Amplitude_Entry = tk.Entry(master )
        self.Amplitude_Entry = Amplitude_Entry
        Amplitude_Entry_label = tk.Label(master, text = "The Amplitude:")


        #Freq Entry
        Freq_Entry = tk.Entry(master)
        self.Freq_Entry = Freq_Entry
        Freq_Entry_label = tk.Label(master, text = 'The Freq:')

        # Show Button
        Show_Button = tk.Button(master, text = 'Show the plot', command = self.show)
        #Show_Button.pack()


        #LAYOUT
        Amplitude_Entry_label.grid(row = 0, column = 0)
        Amplitude_Entry.grid(row =0, column=2)
        Freq_Entry_label.grid(row=1, column=0)
        Freq_Entry.grid(row=1, column=2)
        Show_Button.grid(row=2, column=0)


    #Show fucniton
    def show(self):
        Amp = int(self.Amplitude_Entry.get())
        Freq = int(self.Freq_Entry.get())
        x = np.arange(0,10,0.01)
        y = Amp*np.sin(Freq*x)
        plt.plot(x,y)
        plt.show()

root = tk.Tk()
sin = Sin(root)
root.mainloop()
