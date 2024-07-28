from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())

def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt",
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))

def quitApp():
    root.destroy()

def copy():
    TextArea.event_generate("<<Copy>>")

def cut():
    TextArea.event_generate("<<Cut>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad", "Notepad by Code with Abhishek")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("C:/Users/Abhishek/OneDrive/Documents/Pictures/Screenshots/icon.png")
    root.geometry("644x788")
    
    # Text Area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH, expand=True)

    # Let's create a menubar
    MenuBar = Menu(root)
    
    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu Ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help Menu Ends
    
    root.config(menu=MenuBar)
    
    # Adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
    root.mainloop()
