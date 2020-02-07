#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 07, 2020 07:12:45 PM +0330  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from PIL import Image, ImageTk

import page_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    page_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    page_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("764x612+321+82")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#1b5f8c")
        top.configure(highlightcolor="black")

        self.power_low = tk.Button(top)
        self.power_low.place(relx=0.144, rely=0.474, height=25, width=84)
        self.power_low.configure(activebackground="#d9d9d9")
        self.power_low.configure(text='''Decrease''')

        self.power_rise = tk.Button(top)
        self.power_rise.place(relx=0.144, rely=0.408, height=25, width=84)
        self.power_rise.configure(activebackground="#d9d9d9")
        self.power_rise.configure(text='''Increase''')

        self.freq_rise = tk.Button(top)
        self.freq_rise.place(relx=0.589, rely=0.408, height=25, width=84)
        self.freq_rise.configure(activebackground="#d9d9d9")
        self.freq_rise.configure(text='''Increase''')

        self.freq_low = tk.Button(top)
        self.freq_low.place(relx=0.589, rely=0.474, height=25, width=84)
        self.freq_low.configure(activebackground="#d9d9d9")
        self.freq_low.configure(text='''Decrease''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.223, rely=0.033, height=55, width=279)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#1b5f8c")
        self.Label1.configure(font="-family {bitstream charter} -size 14 -weight bold -slant italic")
        self.Label1.configure(foreground="#fff7fa")
        self.Label1.configure(text='''The LASER Control GUI''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.092, rely=0.163, height=27, width=118)
        self.Label2.configure(activebackground="#1b5f8c")
        self.Label2.configure(activeforeground="white")
        self.Label2.configure(background="#1b5f8c")
        self.Label2.configure(font="-family {bitstream charter} -size 14")
        self.Label2.configure(text='''Set the Power''')

        self.power_label = tk.Label(top)
        self.power_label.place(relx=0.157, rely=0.31, height=25, width=59)
        self.power_label.configure(activebackground="#f9f9f9")
        self.power_label.configure(text='''Label''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.288, rely=0.31, height=25, width=49)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(background="#1b5f8c")
        self.Label5.configure(text='''mJ''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.039, rely=0.31, height=25, width=49)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(background="#1b5f8c")
        self.Label6.configure(text='''Power:''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.393, rely=0.18, relheight=0.458)
        self.TSeparator1.configure(orient="vertical")

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.497, rely=0.163, height=27, width=198)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(background="#1b5f8c")
        self.Label2_1.configure(font="-family {bitstream charter} -size 14")
        self.Label2_1.configure(text='''Set the Frequency''')

        self.Label6_2 = tk.Label(top)
        self.Label6_2.place(relx=0.432, rely=0.31, height=25, width=119)
        self.Label6_2.configure(activebackground="#f9f9f9")
        self.Label6_2.configure(background="#1b5f8c")
        self.Label6_2.configure(text='''Frequency:''')

        self.Freq_label = tk.Label(top)
        self.Freq_label.place(relx=0.602, rely=0.31, height=25, width=59)
        self.Freq_label.configure(activebackground="#f9f9f9")
        self.Freq_label.configure(text='''Label''')

        self.Label5_4 = tk.Label(top)
        self.Label5_4.place(relx=0.733, rely=0.31, height=25, width=49)
        self.Label5_4.configure(activebackground="#f9f9f9")
        self.Label5_4.configure(background="#1b5f8c")
        self.Label5_4.configure(text='''Hz''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.471, rely=0.605, height=195, width=349)
        photo_location = os.path.join(prog_location,"./images.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img0)
        self.Label3.configure(text='''Label''')

if __name__ == '__main__':
    vp_start_gui()





