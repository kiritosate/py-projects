
from tkinter import *
import tkinter

class Main:
    def __init__(self) -> None:
        self.root = Tk()
        a = "username", "password"
        ents = self.MakeForms(a)

        self.root.bind('<Return>', (lambda e=ents: self.fetch(e)))   
        b1 = Button(self.root, text='Show',
                    command=(lambda e=ents: self.fetch(e)))
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(self.root, text='Quit', command=self.root.quit)
        b2.pack(side=LEFT, padx=5, pady=5)
        self.root.mainloop()

    def fetch(self, entries):
        for entry in entries:
            field = entry[0]
            text  = entry[1].get()
            print('%s: "%s"' % (field, text)) 
        
    def MakeForms(self, fields):
        entries = []

        for field in fields:
            row = Frame(self.root)
            lab = self.Label(row, text=field, a='w')
            if field.lower() == "password":
                ent = self.Entry(row, show='*')
            else:
                ent = self.Entry(row)
            row.pack(side=TOP, fill=X, padx=10, pady=10)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        return entries

    def Label(self, master, text, size=12, weight="", bg=None, color=None, a='w'):

            return Label(master, text=text, font=("sans-serif", size, weight), bg=bg, fg=color, anchor=a)
        
    def Entry(self, master, text=None, width=20, show=None, bg=None, size=12, color=None):

        return Entry(master, width=width, font=("sans-serif", size),show=show, bg=bg, fg=color)

Main()