import tkinter as tk

class  Window(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title("Hello world")
        self.label_text = tk.StringVar()
        self.label_text.set('Hello there')

        self.label = tk.Label(self,textvar = self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)


        hello_button = tk.Button(self, text='Say Hello', command=self.say_hello)
        hello_button.pack(side = tk.LEFT, padx = (20,0), pady=(0,20))

        goodbye_button = tk.Button(self, text="Good Bye", command=self.say_goodbye)
        goodbye_button.pack(side= tk.RIGHT,padx=(0,20), pady = (0,20))

    def say_hello(self):
        self.label_text.set('Hello again')

    def say_goodbye(self):
        self.label_text.set('Gooood bye')
        self.after(2000, self.destroy)






if __name__== '__main__':
    window = Window()
    window.mainloop()
