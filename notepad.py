from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfilename
import tkinter.messagebox as tmsg
import os

def save():
    file=asksaveasfile(defaultextension=".txt",filetypes=[("Text Documents","*.txt")])
    f=open(file.name,"w")
    f.write(TextArea.get('1.0',END))
    root.title(os.path.basename(file.name) + " - Notepad")
    tmsg.showinfo("File Saved")

def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def open():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


root=Tk()
root.geometry("634x434")
root.minsize(300,300)
root.title("Notepad")
MainMenu=Menu(root)

FileMenu=Menu(MainMenu,tearoff=0)
FileMenu.add_command(label="New",command=new)
FileMenu.add_command(label="Open",command=open)
FileMenu.add_command(label="Save")
FileMenu.add_command(label="Save as",command=save)

EditMenu=Menu(MainMenu,tearoff=0)
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)

HelpMenu=Menu(MainMenu,tearoff=0)
HelpMenu.add_command(label="Get Started")
HelpMenu.add_command(label="Reach out")

root.config(menu=MainMenu)
MainMenu.add_cascade(label="File",menu=FileMenu)
MainMenu.add_cascade(label="Edit",menu=EditMenu)
MainMenu.add_cascade(label="Help",menu=HelpMenu)

TextArea=Text(font=("Helventica",10))
TextArea.pack(expand=True,fill="both")

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
