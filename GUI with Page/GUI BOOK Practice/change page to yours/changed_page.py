import tkinter as tk


class Window(tk.Tk):
    def __init__(self):

        super().__init__()

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        self.geometry("600x450+354+171")
        self.minsize(1, 1)
        self.maxsize(1351, 738)
        self.resizable(1, 1)
        self.title("New Toplevel")
        self.label_text = tk.StringVar()
        self.label_text.set('Hello there')

        self.Button1 = tk.Button(self,command = self.say_hello)
        self.Button1.place(relx=0.267, rely=0.556, height=25, width=63)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Hello''')

        self.Button2 = tk.Button(self, command = self.say_goodbye)
        self.Button2.place(relx=0.617, rely=0.556, height=25, width=84)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Good Bye''')

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.3, rely=0.156, height=105, width=249)
        self.Label1.configure(text='''Hello there''')
        self.Label1.configure(textvar = self.label_text)


    def say_hello(self):
        self.label_text.set('Hello again')

    def say_goodbye(self):
        self.label_text.set('Gooooodbye')
        self.after(2000, self.destroy)


if __name__ =="__main__" :
    app = Window()
    app.mainloop()()
