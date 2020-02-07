import tkinter as tk
import tkinter.ttk as ttk
import sys
import os
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font11 = "-family {bitstream charter} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {bitstream charter} -size 14 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.geometry("764x612+321+82")
        self.minsize(1, 1)
        self.maxsize(1351, 738)
        self.resizable(1, 1)
        self.title("New selflevel")
        self.configure(background="#1b5f8c")

        self.power_val = tk.IntVar()
        self.power_val.set(0)
        self.freq_val = tk.IntVar()
        self.freq_val.set(0)


        self.power_low = tk.Button(self, command = self.power_low_func)
        self.power_low.place(relx=0.17, rely=0.644, height=25, width=84)
        self.power_low.configure(activebackground="#d9d9d9")
        self.power_low.configure(text='''Decrease''')

        self.power_rise = tk.Button(self,command = self.power_rise_func)
        self.power_rise.place(relx=0.17, rely=0.556, height=25, width=84)
        self.power_rise.configure(activebackground="#d9d9d9")
        self.power_rise.configure(text='''Increase''')

        self.freq_rise = tk.Button(self, command = self.freq_rise_func)
        self.freq_rise.place(relx=0.694, rely=0.556, height=25, width=84)
        self.freq_rise.configure(activebackground="#d9d9d9")
        self.freq_rise.configure(text='''Increase''')

        self.freq_low = tk.Button(self, command = self.freq_low_func)
        self.freq_low.place(relx=0.694, rely=0.644, height=25, width=84)
        self.freq_low.configure(activebackground="#d9d9d9")
        self.freq_low.configure(text='''Decrease''')

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.302, rely=0.304, height=55, width=279)
        self.Label1.configure(background="#1b5f8c")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#fff7fa")
        self.Label1.configure(text='''The LASER Control GUI''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.108, rely=0.222, height=27, width=118)
        self.Label2.configure(activebackground="#1b5f8c")
        self.Label2.configure(activeforeground="white")
        self.Label2.configure(background="#1b5f8c")
        self.Label2.configure(font=font11)
        self.Label2.configure(text='''Set the Power''')

        self.power_label = tk.Label(self)
        self.power_label.place(relx=0.185, rely=0.422, height=25, width=59)
        self.power_label.configure(textvar=self.power_val)

        self.Label5 = tk.Label(self)
        self.Label5.place(relx=0.34, rely=0.422, height=25, width=49)
        self.Label5.configure(background="#1b5f8c")
        self.Label5.configure(text='''mJ''')

        self.Label6 = tk.Label(self)
        self.Label6.place(relx=0.046, rely=0.422, height=25, width=49)
        self.Label6.configure(background="#1b5f8c")
        self.Label6.configure(text='''Power:''')

        self.TSeparator1 = ttk.Separator(self)
        self.TSeparator1.place(relx=0.463, rely=0.444, relheight=0.322)
        self.TSeparator1.configure(orient="vertical")

        self.Label2_1 = tk.Label(self)
        self.Label2_1.place(relx=0.626, rely=0.222, height=27, width=198)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(background="#1b5f8c")
        self.Label2_1.configure(font="-family {bitstream charter} -size 14")
        self.Label2_1.configure(text='''Set the Frequency''')

        self.Label6_2 = tk.Label(self)
        self.Label6_2.place(relx=0.509, rely=0.422, height=25, width=119)
        self.Label6_2.configure(activebackground="#f9f9f9")
        self.Label6_2.configure(background="#1b5f8c")
        self.Label6_2.configure(text='''Frequency:''')

        self.Freq_label = tk.Label(self)
        self.Freq_label.place(relx=0.71, rely=0.422, height=25, width=59)
        self.Freq_label.configure(activebackground="#f9f9f9")
        self.Freq_label.configure(textvar=self.freq_val)

        self.Label5_4 = tk.Label(self)
        self.Label5_4.place(relx=0.864, rely=0.422, height=25, width=49)
        self.Label5_4.configure(activebackground="#f9f9f9")
        self.Label5_4.configure(background="#1b5f8c")
        self.Label5_4.configure(text='''Hz''')


        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.28, rely=0, height=195, width=280)
        photo_location = os.path.join(prog_location,"./images.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img0)
        self.Label3.configure(text='''Label''')




    def power_low_func(self):
        val = self.power_val.get()
        val -=100
        self.power_val.set(val)

    def power_rise_func(self):
        val = self.power_val.get()
        val +=100
        self.power_val.set(val)

    def freq_low_func(self):
        val = self.freq_val.get()
        val -=1
        self.freq_val.set(val)

    def freq_rise_func(self):
        val = self.freq_val.get()
        val +=1
        self.freq_val.set(val)













if __name__ == "__main__":
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    app = App()
    app.mainloop()
