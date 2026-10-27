from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='purple', foreground='white')
lbl.pack(anchor='center')
//new comment to check the merge conflicts
time()
root.mainloop()
//this is the new clock code in github for practice
