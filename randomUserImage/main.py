
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
        
        for i in range(0,4):
            user = rUser._userdata()
            image = self.showImage(user[4])
            l2 = Label(self.tkRoot,image=image)
            l2.pack()

        self.tkRoot.mainloop()

    def showImage(self, image_link):
        
        self.raw_image = urllib.request.urlopen(image_link).read()
        self.toBytesImage = Image.open(io.BytesIO(self.raw_image))

        return ImageTk.PhotoImage(self.toBytesImage)
    
    def refresh(self):

        user = rUser._userdata()
        image = self.showImage(user[4])
        l2 = Label(self.tkRoot,image=image)
        l2.pack()


MyApp()
