from tkinter import *
import random
from os import system
from tkinter.font import ITALIC

class guessNum:

    def guiMain():

        root = Tk()

        easy = IntVar()
        medium = IntVar()
        hard = IntVar()

        root.geometry("400x400+120+120")
        
        label = Label(root, text="what's your guess?", font=("sans-serif", 14, ITALIC))
        label.pack()

        numEntry = Entry(root, width=20, font=("times new roman", 13))
        numEntry.pack()

        a = Checkbutton(root, text="Easy 1-2", variable=easy)
        a.pack()

        b = Checkbutton(root, text="Medium 1-5", variable=medium)
        b.pack()

        c = Checkbutton(root, text="Hard 1-10", variable=hard)
        c.pack()

        btn = Button(root, text="check", command=guessNum.some(numEntry.get(), 1))
        btn.pack()
        
        root.mainloop()

    def some(number, complex):

        hiddenNumber = complex

        if hiddenNumber == number:
            print(f"you guessed it right! its {number}")
        else:
            print(f"you guessed it wrong the number is {hiddenNumber}")
        system("pause")


guessNum.guiMain()