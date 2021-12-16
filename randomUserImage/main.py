
from typing import List
import urllib.parse, urllib.request
from tkinter import *
from PIL import Image, ImageTk
import io
from randomUser import RandomUserData as rUser


class MyApp:

    usersImage = []

    def __init__(self) -> None:
        
        self.tkRoot = Tk()
        self.tkRoot.geometry("700x500")
        self.tkRoot.minsize(height=500, width=700)
        self.tkRoot.title("random user app")

        self.scrollbar = Scrollbar(self.tkRoot)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.myList = Listbox(self.tkRoot, yscrollcommand=self.scrollbar.set)
        self.userName(100)
        self.myList.pack(side=LEFT, fill=BOTH)
        self.scrollbar.config(command=self.myList.yview)

        self.tkRoot.mainloop()

    def showImage(self, image_link):
        self.raw_image = None
        self.toBytesImage = None

        self.raw_image = urllib.request.urlopen(image_link).read()
        self.toBytesImage = Image.open(io.BytesIO(self.raw_image))

        return ImageTk.PhotoImage(self.toBytesImage)
    
    def refresh(self, time=1):

        for i in range(time):

            user = rUser._userdata()
            image = self.showImage(user[4][0])
            l2 = Label(self.tkRoot,image=image)
            l2.image = image
            l2.grid(column=i, sticky=W)

    def userName(self, time=1):

        for i in range(time):

            user = rUser._userdata()
            self.myList.insert(END, user[0])


MyApp()
