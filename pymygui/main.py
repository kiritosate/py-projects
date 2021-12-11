from tkinter import *



class main:
    def __init__(self) -> None:
        
        self.root = Tk()
        self.root.title("my app")
        self.root.geometry("500x400")

        self.root.minsize(height=400, width=500)
        title = self.SomeLabel("Functions", 15, "bold")
        title.pack(pady=10)

        userLabel = self.SomeLabel("username", 12).pack()

        username = self.SomeEntry()
        username.pack()

        self.root.mainloop()
    
    def SomeLabel(self, text, size=12, weight="", bg=None, color=None):
        '''
            text = string
            size = int default is 12
            weight = string
            bg = string
            color = string
        '''
        return Label(self.root, text=text, font=("sans-serif", size, weight), bg=bg, fg=color)
    
    def SomeEntry(self, text=None, width=20, show=None, bg=None, size=12, color=None):

        return Entry(self.root, width=width, font=("sans-serif", size),show=show, bg=bg, fg=color)

        
    

if __name__ == "__main__":
    main()